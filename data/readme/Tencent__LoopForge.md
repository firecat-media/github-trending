English  ·  简体中文 

   Two ways to work  ·
   Quick start  ·
   SOPs  ·
   Features  ·
   Local  ·
   FAQ  ·
   Docs 

https://github.com/user-attachments/assets/8af401d9-1aae-427c-b4bc-455c12d17beb

  80-second product tour (1080p, with sound).  

**LoopForge** is a self-hosted workspace where your team ships software with coding agents. Describe what you need to **Main Bot** in chat: it opens a Docker sandbox, checks out your repositories, delegates to project roles, and opens the PR. When a way of working proves itself, save it as an **SOP** (a standard workflow of agents, scripts and human gates) so the next requirement is delivered the same way, with review and approval built in.

Coding-agent CLIs do the work: CodeBuddy, Codex, Claude Code, OpenCode, Cursor CLI, Antigravity, Kimi Code, Pi, DeepSeek Harness and ZCode. LoopForge adds the roles, sandboxes, checkpoints and history around them, all on your own infrastructure under the MIT license.

## Two ways to work

| | **Chat with Main Bot** | **Run an SOP** |
| --- | --- | --- |
| Best for | Exploring, quick fixes, iterating with the agent | Repeatable delivery with fixed stages and sign-off |
| How it runs | Main Bot opens a [conversation workspace](docs/conversation-workspaces.md) (a Docker sandbox with your repos) on demand and calls project roles as subagents | The engine runs Agent, Script, Human-gate and sub-SOP nodes in order, in their own sandbox |
| You stay in control by | Queuing or steering messages mid-reply, and pausing, resuming or taking over a running SOP from chat | Approving at human gates, sending work back to a chosen step, retrying or rerunning from any node |
| Delivers | A PR/MR, or a direct merge into a shared branch (`mode=direct`) | Documents, code or a PR, plus per-node artifacts and logs |

Both paths track the same **requirements**, so every change, whether made in chat or by an SOP, links back to what was asked for and counts toward delivery and cost reports.

  The chat home. Type a request,  @  a role, skill, requirement, SOP or repository, and pick the executor, model and permission mode per conversation.  

## Why LoopForge

Ask a coding agent to "fix this bug" and the result depends on that run. It might skip the plan, forget the tests, review its own code, or stop halfway without anyone noticing. That's fine for a demo, but it isn't how a team ships.

- **Repeatable.** Same SOP, same stages, same checks for every requirement. Start from built-in backend, frontend, bug-fix and product SOPs.
- **Separated roles.** Planning, implementation, review and testing each get their own prompt, executor, model, rules, Skills and MCP tools. A role works as an SOP node or as a subagent in chat.
- **Human in the loop.** Approval gates where they matter. Read the report, approve, or send the work back to a chosen step.
- **Observable and resumable.** Node status, tool traces, logs and artifacts in one place. Pause, retry a failed step, or rerun from any node.
- **Your st
