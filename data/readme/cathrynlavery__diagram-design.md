**An agent skill that draws diagrams as one self-contained HTML + SVG file, in your brand. 51 diagram types. No shadows. No Mermaid slop.**

[ ](https://github.com/cathrynlavery/diagram-design/stargazers)
[ ](https://skills.sh/cathrynlavery/diagram-design/diagram-design)
[ ](https://github.com/cathrynlavery/diagram-design/actions/workflows/ci.yml)
[ ](CHANGELOG.md)
[ ](LICENSE)

**[Website](https://diagramdesign.dev) · [Gallery](https://cathrynlavery.github.io/diagram-design/) · [Changelog](CHANGELOG.md)**

[Install](#install) · [What it makes](#what-it-makes) · [Quickstart](#quickstart) · [Match your brand](#onboarding-make-it-look-like-your-brand) · [Import](#import-from-drawio-mermaid-excalidraw-or-plantuml) · [Export](#export-to-png--svg) · [Contributing](#contributing)

 npx skills add cathrynlavery/diagram-design 

Ask your agent in plain words:

- *"Make me an architecture diagram of my app: frontend, backend, database, Redis cache."*
- *"I need a quadrant showing Q2 projects by impact vs effort."*
- *"Give me a sequence of a bearer call with token refresh on 401."*
- *"Onboard diagram-design to https://yoursite.com"* (pulls your palette and fonts so every diagram after this one matches your site)

The agent picks the type, states its plan, and writes one `.html` file you can open by double-clicking.

---

## Install

Works with any host that reads Agent Skills, including Cursor, Claude Code, Codex, Qoder, GitHub Copilot, Gemini CLI, Cline, Windsurf and Amp:

```bash
npx skills add cathrynlavery/diagram-design
```

In Claude Code, the plugin marketplace gets you updates and the slash commands:

```text
/plugin marketplace add cathrynlavery/diagram-design
/plugin install diagram-design@diagram-design
```

Official builds come only from this repository. LittleMight, Cathryn Lavery's company, publishes the plugin directory listings; a listing under any other name is an unofficial copy. [PRIVACY.md](PRIVACY.md) lists what the skill sends over the network.

  Claude Code : turn on auto-update 

After installing, run `/plugin`, open **Marketplaces**, select **diagram-design**, and choose **Enable auto-update**. Claude Code disables auto-update by default for third-party marketplaces; after this toggle, it refreshes the marketplace and installed plugin in the background after startup. Run `/reload-plugins` when prompted, or let the next session load the update.

  Cursor , Cline, Gemini CLI, Windsurf, Amp, Zed, Warp, Roo, Kilo and other Agent Skills hosts 

The cross-agent [`skills` CLI](https://skills.sh) resolves this repository, detects `skills/diagram-design/SKILL.md`, and installs the whole skill (`references/`, `assets/`, `scripts/`) into every host root you select, including Cursor's:

```bash
npx skills add cathrynlavery/diagram-design
```

When the selected roots resolve to more than one skills directory, the CLI asks for an installation method and recommends **Symlink**: one canonical copy, linked into each root, so a later update reach
