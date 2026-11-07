#!/usr/bin/env python3
"""Dagelijkse verzamelaar voor GitHub trending.

Draait in GitHub Actions en schrijft:
  data/trending/JJJJ-MM-DD.json   de trending-lijst van die dag
  data/repos.json                 elke repo die ooit trending was
  data/stars.json                 sterrenverloop per repo (compact)
  data/readme/<owner>__<repo>.md  stuk README van nieuwe repo's
  data/status.json                samenvatting van de laatste run

Zonder GITHUB_TOKEN (lokaal testen) worden sterren alleen van de
trending-pagina gehaald en worden README's overgeslagen.
"""
import datetime as dt
import json
import os
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request
from zoneinfo import ZoneInfo

from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
TRENDING_URL = "https://github.com/trending?since=daily"
TZ = ZoneInfo("Europe/Amsterdam")
UA = "github-trending-collector (GitHub Actions)"
README_CHARS = 3000
BATCH = 50


def load(path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return default


def save(path, obj, compact=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    if compact:
        text = json.dumps(obj, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    else:
        text = json.dumps(obj, ensure_ascii=False, indent=1, sort_keys=True)
    path.write_text(text + "\n", encoding="utf-8")


def http(url, data=None, headers=None, tries=3):
    headers = {"User-Agent": UA, **(headers or {})}
    for attempt in range(1, tries + 1):
        try:
            req = urllib.request.Request(url, data=data, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as err:
            if err.code == 404 or attempt == tries:
                raise
        except urllib.error.URLError:
            if attempt == tries:
                raise
        time.sleep(3 * attempt)
    raise RuntimeError("onbereikbaar: " + url)


def to_int(text):
    digits = re.sub(r"[^\d]", "", text or "")
    return int(digits) if digits else None


def clean(text):
    return " ".join((text or "").split())


def parse_trending(page):
    """Lees de repo's van de trending-pagina, in volgorde."""
    soup = BeautifulSoup(page, "html.parser")
    items = []
    for art in soup.select("article.Box-row"):
        link = art.select_one("h2 a[href]")
        if not link:
            continue
        full = link["href"].strip("/")
        if full.count("/") != 1:
            continue
        desc = art.select_one("p")
        lang = art.select_one('[itemprop="programmingLanguage"]')
        stars = art.select_one('a[href$="/stargazers"]')
        forks = art.select_one('a[href$="/forks"]')
        today = re.search(r"([\d,.]+)\s+stars?\s+(today|this week|this month)",
                          art.get_text(" ", strip=True))
        items.append({
            "rank": len(items) + 1,
            "repo": full,
            "description": clean(desc.get_text(" ")) if desc else "",
            "language": clean(lang.get_text()) if lang else None,
            "stars": to_int(stars.get_text()) if stars else None,
            "forks": to_int(forks.get_text()) if forks else None,
            "stars_today": to_int(today.group(1)) if today else None,
        })
    return items


def graphql(query, token):
    body = json.dumps({"query": query}).encode()
    raw = http("https://api.github.com/graphql", data=body, headers={
        "Authorization": "bearer " + token,
        "Content-Type": "application/json",
    })
    return json.loads(raw)


def fetch_live(names, token):
    """Sterren en metadata van alle repo's, 50 per GraphQL-vraag.

    Geeft {repo: node} terug; node is None als GitHub de repo niet
    (meer) kent. Repo's uit een mislukte vraag ontbreken in de uitkomst.
    """
    out = {}
    for start in range(0, len(names), BATCH):
        part = names[start:start + BATCH]
        fields = []
        for i, full in enumerate(part):
            owner, name = full.split("/", 1)
            fields.append(
                f"r{i}: repository(owner: {json.dumps(owner)}, name: {json.dumps(name)}) "
                "{ nameWithOwner stargazerCount isArchived description homepageUrl "
                "repositoryTopics(first: 8) { nodes { topic { name } } } }")
        try:
            body = graphql("query { " + " ".join(fields) + " }", token)
        except Exception as err:  # één mislukte vraag mag de rest niet stoppen
            print(f"GraphQL-fout bij blok {start}: {err}", file=sys.stderr)
            continue
        data = body.get("data") or {}
        for i, full in enumerate(part):
            out[full] = data.get(f"r{i}")
    return out


def fetch_readme(full, token):
    try:
        text = http(f"https://api.github.com/repos/{full}/readme", headers={
            "Authorization": "bearer " + token,
            "Accept": "application/vnd.github.raw+json",
        })
    except Exception:
        return None
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)  # plaatjes en badges
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    return text.strip()[:README_CHARS]


def compact(points, today):
    """Laatste 30 dagen per dag, tot een jaar per week, daarna per maand."""
    keep = {}
    for day, count in sorted(points, reverse=True):
        d = dt.date.fromisoformat(day)
        age = (today - d).days
        if age <= 30:
            key = day
        elif age <= 365:
            year, week, _ = d.isocalendar()
            key = f"w{year}-{week:02d}"
        else:
            key = day[:7]
        keep.setdefault(key, [day, count])
    return sorted(keep.values())


def main():
    now = dt.datetime.now(TZ)
    today = now.date()
    day = today.isoformat()
    stamp = now.isoformat(timespec="minutes")

    page = http(TRENDING_URL)
    items = parse_trending(page)
    if len(items) < 5:
        save_path = DATA / "debug" / f"trending-{day}.html"
        save_path.parent.mkdir(parents=True, exist_ok=True)
        save_path.write_text(page, encoding="utf-8")
        print(f"FOUT: maar {len(items)} repo's gevonden, pagina bewaard in {save_path}",
              file=sys.stderr)
        sys.exit(1)

    save(DATA / "trending" / f"{day}.json",
         {"date": day, "fetched_at": stamp, "source": TRENDING_URL, "items": items})

    repos = load(DATA / "repos.json", {})
    for it in items:
        r = repos.setdefault(it["repo"], {"first_seen": day, "trending": []})
        r["last_seen"] = day
        r["description"] = it["description"]
        r["language"] = it["language"]
        r["trending"] = sorted([t for t in r["trending"] if t[0] != day]
                               + [[day, it["rank"], it["stars_today"]]])

    token = os.environ.get("GITHUB_TOKEN")
    live = fetch_live(sorted(repos), token) if token else {}
    scraped = {it["repo"]: it["stars"] for it in items}
    stars = load(DATA / "stars.json", {})
    updated = not_found = 0

    for full, r in repos.items():
        count = scraped.get(full)
        if full in live:
            node = live[full]
            if node is None:
                r["status"] = "niet gevonden"
                not_found += 1
            else:
                count = node["stargazerCount"]
                r["status"] = "gearchiveerd" if node["isArchived"] else "actief"
                r["topics"] = [n["topic"]["name"] for n in node["repositoryTopics"]["nodes"]]
                if node.get("homepageUrl"):
                    r["homepage"] = node["homepageUrl"]
                if not r.get("description") and node.get("description"):
                    r["description"] = clean(node["description"])
                if node["nameWithOwner"].lower() != full.lower():
                    r["renamed_to"] = node["nameWithOwner"]
        if count is None:
            continue
        r.setdefault("stars_first", count)
        pts = [p for p in stars.get(full, []) if p[0] != day] + [[day, count]]
        stars[full] = compact(pts, today)
        updated += 1

    readmes = 0
    if token:
        for full in sorted(repos):
            path = DATA / "readme" / (full.replace("/", "__") + ".md")
            if path.exists() or repos[full].get("status") == "niet gevonden":
                continue
            text = fetch_readme(full, token) or ""
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text + "\n", encoding="utf-8")  # leeg = geen README, niet opnieuw proberen
            readmes += bool(text)

    save(DATA / "repos.json", repos)
    save(DATA / "stars.json", stars, compact=True)
    status = {
        "last_run": stamp,
        "date": day,
        "trending_count": len(items),
        "repos_total": len(repos),
        "stars_updated": updated,
        "not_found": not_found,
        "readmes_added": readmes,
        "live_stars": bool(token),
    }
    save(DATA / "status.json", status)
    print(json.dumps(status, ensure_ascii=False))


if __name__ == "__main__":
    main()
