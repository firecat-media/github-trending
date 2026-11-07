#!/usr/bin/env python3
"""Zet de verzamelde data om naar documenten voor het dashboard.

Gebruikt door de dagelijkse Claude-taak.

  todo   welke repo's nog een Nederlandse uitleg nodig hebben
  build  combineer data + uitleg tot dashboard-documenten

Uitleg die al in het dashboard staat wordt gelezen uit een export van
de dashboard-database (map met JSON-bestanden), zodat niets dubbel
geschreven hoeft te worden.
"""
import argparse
import datetime as dt
import json
import pathlib
import re
import sys
from zoneinfo import ZoneInfo

TZ = ZoneInfo("Europe/Amsterdam")
CATEGORIES = [
    "AI-agents en automatisering",
    "AI-modellen en onderzoek",
    "Programmeren en ontwikkeltools",
    "Websites en apps",
    "Video, beeld en audio",
    "Data en databases",
    "Beveiliging en privacy",
    "Servers en infrastructuur",
    "Leren en naslag",
    "Overig",
]
FITS = ["Firecat.AI", "Firecat.Media", "Beide", "Geen van beide"]
CHUNK_BYTES = 200_000     # documenten mogen maximaal 256 KiB zijn
BATCH_BYTES = 850_000     # een batch mag maximaal 1 MiB zijn


def load(path, default=None):
    try:
        return json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        if default is None:
            raise
        return default


def size(obj):
    return len(json.dumps(obj, ensure_ascii=False, separators=(",", ":")).encode())


def tidy(text):
    text = (text or "").replace("—", ",").replace("–", "-")
    text = re.sub(r"\s+,", ",", text)
    return " ".join(text.split())


def existing_items(db_dir):
    """Alle repo-items uit een export van de dashboard-database."""
    found = {}
    if not db_dir:
        return found
    for path in sorted(pathlib.Path(db_dir).rglob("*.json")):
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            continue
        body = doc.get("data", doc) if isinstance(doc, dict) else {}
        for item in body.get("items", []) if isinstance(body, dict) else []:
            if isinstance(item, dict) and item.get("n"):
                found[item["n"]] = item
    return found


def enriched(item):
    return bool(item and item.get("d") and item.get("cat") in CATEGORIES
                and item.get("fit") in FITS and item.get("why"))


def cmd_todo(args):
    data = pathlib.Path(args.data)
    repos = load(data / "repos.json")
    stars = load(data / "stars.json", {})
    have = existing_items(args.db)
    todo = []
    for full in sorted(repos, key=lambda k: (repos[k].get("first_seen", ""), k), reverse=True):
        if enriched(have.get(full)):
            continue
        r = repos[full]
        readme_path = data / "readme" / (full.replace("/", "__") + ".md")
        readme = readme_path.read_text(encoding="utf-8")[:1500] if readme_path.exists() else ""
        todo.append({
            "repo": full,
            "url": "https://github.com/" + full,
            "description": r.get("description", ""),
            "language": r.get("language"),
            "topics": r.get("topics", []),
            "homepage": r.get("homepage"),
            "stars": (stars.get(full) or [[None, None]])[-1][1],
            "readme": readme,
        })
    todo = todo[: args.max]
    pathlib.Path(args.out).write_text(json.dumps(todo, ensure_ascii=False, indent=1), encoding="utf-8")
    template = {t["repo"]: {"d": "", "cat": "", "fit": "", "why": ""} for t in todo}
    pathlib.Path(args.template).write_text(json.dumps(template, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(todo)} repo's hebben nog een uitleg nodig -> {args.out}")
    print(f"Vul {args.template} in en geef het mee aan 'build --new'.")


def cmd_build(args):
    data = pathlib.Path(args.data)
    repos = load(data / "repos.json")
    stars = load(data / "stars.json", {})
    collector = load(data / "status.json", {})
    have = existing_items(args.db)
    new = load(args.new, {}) if args.new else {}

    problems = []
    for full, e in new.items():
        if full not in repos:
            problems.append(f"{full}: onbekende repo")
        if e.get("cat") not in CATEGORIES:
            problems.append(f"{full}: categorie '{e.get('cat')}' bestaat niet")
        if e.get("fit") not in FITS:
            problems.append(f"{full}: Firecat-label '{e.get('fit')}' bestaat niet")
        if not e.get("d") or not e.get("why"):
            problems.append(f"{full}: uitleg of reden ontbreekt")
    if problems:
        print("Niet gebouwd, los dit eerst op:\n  " + "\n  ".join(problems), file=sys.stderr)
        sys.exit(2)

    stamp = dt.datetime.now(TZ).isoformat(timespec="minutes")
    latest = collector.get("date") or max(
        (t[0] for r in repos.values() for t in r.get("trending", [])), default="")
    items = []
    for full, r in repos.items():
        old = have.get(full, {})
        e = new.get(full) or {k: old.get(k) for k in ("d", "cat", "fit", "why", "ed")}
        item = {
            "n": full,
            "d": tidy(e.get("d")),
            "cat": e.get("cat") or "",
            "fit": e.get("fit") or "",
            "why": tidy(e.get("why")),
            "ed": e.get("ed") or (stamp[:10] if full in new else ""),
            "en": (r.get("description") or "")[:240],
            "lang": r.get("language"),
            "first": r.get("first_seen"),
            "last": r.get("last_seen"),
            "t": r.get("trending", []),
            "s": stars.get(full, []),
            "sf": r.get("stars_first"),
        }
        if r.get("status") and r["status"] != "actief":
            item["st"] = r["status"]
        if r.get("renamed_to"):
            item["rn"] = r["renamed_to"]
        items.append(item)
    items.sort(key=lambda i: (i["first"] or "", i["n"]))

    out = pathlib.Path(args.out)
    (out / "repos").mkdir(parents=True, exist_ok=True)
    (out / "meta").mkdir(parents=True, exist_ok=True)
    for old_file in (out / "repos").glob("*.json"):
        old_file.unlink()

    chunks, current = [], []
    for item in items:
        if current and size({"items": current + [item]}) > CHUNK_BYTES:
            chunks.append(current)
            current = []
        current.append(item)
    if current:
        chunks.append(current)

    writes = []
    for i, part in enumerate(chunks):
        doc_id = f"c{i:03d}"
        body = {"chunk": doc_id, "updated": stamp, "items": part}
        path = out / "repos" / f"{doc_id}.json"
        path.write_text(json.dumps(body, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        writes.append({"collection": "repos", "doc_id": doc_id, "file_path": str(path.resolve()),
                       "bytes": path.stat().st_size})

    today = sorted(
        ((t[1], i["n"]) for i in items for t in i["t"] if t[0] == latest),
        key=lambda x: (x[0] or 999))
    status = {
        "updated_at": stamp,
        "date": latest,
        "chunks": [w["doc_id"] for w in writes],
        "repos_total": len(items),
        "enriched": sum(1 for i in items if enriched(i)),
        "today": [n for _, n in today],
        "collector": collector,
        "categories": CATEGORIES,
        "fits": FITS,
    }
    spath = out / "meta" / "status.json"
    spath.write_text(json.dumps(status, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    writes.append({"collection": "meta", "doc_id": "status", "file_path": str(spath.resolve()),
                   "bytes": spath.stat().st_size})

    # Groepeer in batches onder de limiet; status altijd in de laatste batch.
    batches, cur, cur_bytes = [], [], 0
    for w in writes:
        if cur and cur_bytes + w["bytes"] > BATCH_BYTES:
            batches.append(cur)
            cur, cur_bytes = [], 0
        cur.append(w)
        cur_bytes += w["bytes"]
    batches.append(cur)

    stale = sorted(set(f"c{i:03d}" for i in range(len(chunks), 200))
                   & {doc for doc in existing_chunk_ids(args.db)})
    manifest = {"batches": batches, "stale_chunks": stale, "summary": {
        "repos": len(items), "chunks": len(chunks), "today": len(today),
        "enriched": status["enriched"], "new_enrichments": len(new)}}
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(manifest["summary"], ensure_ascii=False))
    print(f"{len(batches)} batch(es) klaar in {out / 'manifest.json'}")


def existing_chunk_ids(db_dir):
    if not db_dir:
        return set()
    return {p.stem for p in pathlib.Path(db_dir).rglob("c[0-9][0-9][0-9].json")}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("todo")
    t.add_argument("--data", required=True)
    t.add_argument("--db")
    t.add_argument("--out", default="todo.json")
    t.add_argument("--template", default="new.json")
    t.add_argument("--max", type=int, default=60)
    b = sub.add_parser("build")
    b.add_argument("--data", required=True)
    b.add_argument("--db")
    b.add_argument("--new")
    b.add_argument("--out", required=True)
    args = ap.parse_args()
    {"todo": cmd_todo, "build": cmd_build}[args.cmd](args)


if __name__ == "__main__":
    main()
