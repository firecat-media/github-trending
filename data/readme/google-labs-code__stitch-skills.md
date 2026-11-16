# Stitch Design Skills

A collection of agent skills and plugins for [Google Stitch](https://stitch.withgoogle.com), following the [Agent Skills](https://agentskills.io) open standard. Compatible with coding agents such as Codex, Antigravity, Gemini CLI, Claude Code, Cursor, and OpenCode (manual install).

## Quick Start

### 1. Install Plugins (Recommended)
The fastest way to set up the full Stitch plugin suite globally.

#### Codex

Add the Stitch Skills marketplace, then install the plugins you need.

  Via CLI  (recommended) 

```bash
codex plugin marketplace add google-labs-code/stitch-skills --ref main \
  --sparse .agents/plugins \
  --sparse plugins/stitch-design \
  --sparse plugins/stitch-build \
  --sparse plugins/stitch-utilities
```

> [!TIP]
> The `--sparse` flags are optional — they limit the checkout to only the
> listed paths for a faster clone. Omit them to pull the entire repository.

  Via the Codex UI  

Navigate to **Settings → Plugin Marketplaces → Add** and fill in:

| Field | Value |
|---|---|
| **Source** | `https://github.com/google-labs-code/stitch-skills` |
| **Git ref** | `main` |
| **Sparse paths** | *(optional)* `.agents/plugins`, `plugins/stitch-design`, `plugins/stitch-build`, `plugins/stitch-utilities` |

Once the marketplace is registered, install any combination of:

- **`stitch-design`** — design-focused skills
- **`stitch-build`** — build and component skills
- **`stitch-utilities`** — utility and helper skills

#### Claude Code & Cursor

```bash
# Claude Code — installs into the current project
npx plugins add google-labs-code/stitch-skills --scope project --target claude-code
```

```bash
# Cursor — installs into the current workspace
npx plugins add google-labs-code/stitch-skills --scope workspace --target cursor
```

#### OpenCode

OpenCode does **not** use `npx plugins` / `npx skills` or the Codex/Claude marketplace layout.
Install skills and the Stitch MCP server manually:

**1. Skills** — copy the skill folders you need into a discoverable path:

```bash
# Project-local (recommended)
mkdir -p .opencode/skills
cp -R plugins/stitch-design/skills/generate-design .opencode/skills/generate-design
# repeat for other skills under plugins/*/skills/
```

OpenCode also discovers `.claude/skills/` and `.agents/skills/` (see [OpenCode skills docs](https://opencode.ai/docs/skills/)).

> **Naming:** OpenCode requires skill `name` frontmatter to be lowercase kebab-case and match the directory name. Skills that use `stitch::…` names (or other non-kebab forms) need the `name` field and folder renamed before OpenCode will load them. Extra frontmatter such as `allowed-tools` is ignored.

**2. Stitch MCP** — add a remote MCP entry in project `opencode.json` or `~/.config/opencode/opencode.json` after completing the [Stitch MCP setup](https://stitch.withgoogle.com/docs/mcp/setup/):

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "stitch": {
      "type": "remote",
      "url": "YOUR_STITCH_MCP_UR
