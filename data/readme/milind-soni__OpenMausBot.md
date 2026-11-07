# OpenMausBot

**The open-source Grok Bot alternative: your own team of AI bots, in a chat app.**

[**openmausbot.com**](https://www.openmausbot.com) &nbsp;·&nbsp; [Download](https://www.openmausbot.com/download) &nbsp;·&nbsp; [Open source Grok Bot alternative, compared](https://www.openmausbot.com/blog/grok-bot-vs-openmausbot)

 OpenMausBot is an open-source Grok Bot alternative: an independent project inspired by **Grok Bot**, and the open-source alternative to **Meta Muse**, **OpenAI dots** and **Cue by Manus** — bring-your-own-agent, local-first, on the models you already have. Also known as **MausBot**; formerly **OpenGrokBot**. Not affiliated with xAI, Meta, OpenAI or Manus. 

Every bot in the sidebar is a real agent — Claude or Codex running locally under the hood — with its own
personality, its own model, its own cloud computer, and its own connected apps.
Talk to them like contacts. Watch them work. Approve what matters.

[ ](https://github.com/milind-soni/OpenMausBot/releases/latest)

&nbsp;

&nbsp;

&nbsp;

 [latest release](https://github.com/milind-soni/OpenMausBot/releases/latest) &nbsp;·&nbsp; macOS: Apple silicon & Intel · signed & notarized .dmg &nbsp;·&nbsp; Windows: x64 installer &nbsp;·&nbsp; Ubuntu 24.04 x64: .deb or AppImage beta &nbsp;·&nbsp; [all releases](https://github.com/milind-soni/OpenMausBot/releases) 

 Powered by  boat.dev  

---

> ⚠️ **No affiliation with any cryptocurrency.** OpenMausBot has no token. Any coin using the OpenMausBot, Maus, or SupaMaus name is not created, endorsed, or affiliated with this project or its maintainer. I have received no tokens, payment, or allocation from anyone, and I will not be endorsing any token.

## Why

One assistant in one box is the wrong shape for agents. OpenMausBot is an independent, open-source project inspired by **Grok Bot** —
it keeps the idea (AI as a *messaging app*: a roster of bots you chat with, each with its own personality,
memory of its thread, model, computer, and apps) and rebuilds it open, local-first, and on the agents you
already have:

- **Bring your own agents.** Bots run on the `claude`, `codex`, and `grok` CLIs installed on your own machine
  — your existing logins and subscriptions, no new accounts, no proxy in the middle. Point any engine at a
  custom CLI binary (a versioned build or wrapper) in **Settings → Engines**.
- **Local first.** One small harness server on `127.0.0.1` owns every agent process. Transcripts, keys, and
  events live in `~/.openmausbot`, not a cloud.
- **Agents with hands.** Each bot can use a cloud Linux desktop, an isolated Local VM, or—where the platform
  safety boundary is currently certified—your own computer, plus 500+ apps through Composio. Host control is
  available on macOS and Ubuntu Xorg after explicit opt-in. Ubuntu Wayland host control remains disabled while
  issue #345 is resolved.

## The open-source alternative to Grok Bot, Muse, dots and Cue

Four closed personal-agent products shipped in seven weeks of 2
