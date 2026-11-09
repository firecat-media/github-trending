**Give the agent you already use a memory you control.** GBrain stores explicit facts with their sources, supports corrections and withdrawal, and makes the same memory available across your agents. Start with keyless memory and keyword retrieval; add semantic search, synthesis, and background enrichment when you need them.

GBrain is MIT-licensed and free to self-host; gbrain.io is optional paid hosting.

> [!TIP]
> **Need hosted? First time running an agent?** Try **[gbrain.io](https://gbrain.io/?ref=readme)**, hosted GBrain, for the easiest experience: one brain for you and your team, connected to ChatGPT, Claude and Cursor, with nothing to install or keep online. Stuck? Email support@gbrain.io and a person will set it up with you, free.

**Keep skills beside knowledge.** New local brains include memory skills in their
content root. Agents can join an authorized catalog; only approved editors can
publish. Managed coding-agent installs add an owned native router; restart and
real-use verification are separate steps. Staged migration preserves sharing
choices and personal edits. See [shared brain skills](docs/guides/shared-brain-skills.md).

## Choose your setup

1. **Add GBrain to my existing agent — recommended.** Keep your agent's identity and save memory inside its environment. No new personal-agent identity or private repository is required. Start with the guide for **[Grok Bot](docs/guides/grok-bot.md)**, **[Muse](docs/guides/muse.md)**, or **[Codex / Claude Code](docs/tutorials/connect-coding-agent.md)**. [Other harnesses](#connect-gbrain-to-your-ai-client-mcp).
2. **Use the brain on my own computer from everywhere.** One command publishes it over MCP on your Tailscale tailnet and keeps it running: `gbrain mcp expose` (add `--funnel` for cloud agents such as Grok Bot, Muse and ChatGPT). Follow **[use your brain from anywhere over MCP](docs/guides/remote-mcp.md)**. **Say to your agent:** *"use my brain over mcp"* — *"put my brain on tailscale"*.
3. **Connect my existing hosted brain.** Follow **[hosted harness access](docs/guides/hosted-harness-access.md)** to choose native OAuth or a private machine connection. For dashboard login, clients, and permissions, use **[MCP administration](docs/mcp/ADMIN.md)** with the server's separate owner credential. Delegation is an explicit choice.

Grok **Bot** and Grok **Build** are different products. Muse's personal agent and **Muse Code** are different products too. Muse already has native editable memory; GBrain adds an explicit, portable record with provenance and shared access. See each guide's dated evidence and remaining verification steps.

I'm Garry Tan, President and CEO of Y Combinator. I built GBrain to run my own AI agents. It's the production brain behind my OpenClaw and Hermes deployments: **155,795 pages, 24,589 people, 5,340 companies**, 66 cron jobs running autonomously. My agent ingests meetings, emails, tweets, voice calls, and original ideas while I sleep. It enriches every person 
