# claude-bughunter

> A self-contained Claude skill bundle for bug hunting and external red-team work · **83 skills** · 15 slash commands · **681 disclosed-report patterns** (433 now individually cited & auditable) across 24 core vulnerability classes · enterprise identity + infrastructure attack matrices · engagement-folder scaffolding · Burp MCP integration · battle-tested across authorized red-team and bug-hunting engagements, plus public training platforms (DVWA, OWASP Juice Shop, Hacker101, testphp.vulnweb.com).

Built by **[Sachin Sharma](https://www.linkedin.com/in/sachinsharma8080/)** — Bug Hunting & GenAI Security Research.

   SPONSORED BY 

  &nbsp;&nbsp;&nbsp;&nbsp;

---

## What is this?

`claude-bughunter` is a drop-in skill bundle for the [Claude Code skills system](https://docs.claude.com/en/docs/claude-code/skills). Install once and Claude Code stops being a chatbot and starts behaving like a senior bug-hunting researcher or red-team operator: it knows the techniques, the chain templates, the VRT mappings, the platform CVE chains, and the hygiene — and it stays in scope.

Four layers stack:

- **Think** — `bb-methodology` + `redteam-mindset`: the 5-phase non-linear workflow, critical-thinking framework, and red-team operator discipline.
- **Hunt webapps** — 58 `hunt-*` skills curated from 681 disclosed HackerOne reports: per-class detection patterns, payloads, bypass tables, and chain templates.
- **Hit the perimeter** — enterprise platform chains (M365/Entra, Okta, vCenter, SSL-VPN appliances, SharePoint, cloud IAM): current 2024–2026 CVE chains + post-credential escalation.
- **Ship it** — `triage-validation` + reporting + `evidence-hygiene`: the 7-Question Gate, VRT-aware severity, OOS rebuttals, PII redaction, and red-team deliverables.

All triggered automatically by topic — describe what you're testing in plain English and the relevant skill loads. No invocation by name.

---

## Quickstart

**Option A — install as a Claude Code plugin (recommended).** From inside Claude Code:

```text
/plugin marketplace add elementalsouls/Claude-BugHunter
/plugin install claude-bughunter@elementalsouls
```

All 83 skills + 15 commands load namespaced under `claude-bughunter:` and update when you bump the plugin version — no files copied into `~/.claude/`.

**Option B — copy install (no plugin system / pin to a clone):**

```bash
git clone https://github.com/elementalsouls/Claude-BugHunter.git
cd Claude-BugHunter
```

```bash
# macOS / Linux
bash scripts/install.sh

# Windows (PowerShell)
pwsh ./scripts/install.ps1
```

Both copy the skills + commands into `~/.claude/` (macOS/Linux) or `%USERPROFILE%\.claude\` (Windows) and wire the `hunt` engagement scaffolder.

**What each install path gives you:**

| Path | 83 skills + 15 slash commands | `cbh` CLI | `hunt` scaffolder |
|---|---|---|---|
| **A — plugin** | ✅ namespaced under `claude-bughunter:` | ➕ separate `pipx install` | ❌ clone-only |
| **B — copy install** | ✅ copied into `~/.claud
