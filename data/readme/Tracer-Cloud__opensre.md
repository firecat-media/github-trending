OpenSRE: The open-source agent for CI/CD reliability 

 Your CI tells you it broke, but not why or how to fix it. OpenSRE is a CLI agent that reads the failed run, traces the cause and pushes a fix for you to review. Self-hosted, with your own models. 

     Quickstart  ·
     Docs  ·
     FAQ  ·
     Security 

---

> 🚧 Public Alpha: Core workflows are usable for early exploration, though not yet fully stable. The project is in active development, and APIs and integrations may evolve.

---

## Before you begin

Make sure you have:

- A terminal open in a code project
- A Git repository (recommended for the full workflow demonstration)

## Step 1: Install and start opensre

macOS or Linux:

```bash
curl -fsSL https://install.opensre.com | bash -s -- -gh
```

Windows (PowerShell):

```powershell
& ([scriptblock]::Create((irm https://install.opensre.com/install.ps1))) -gh
```

Then start OpenSRE:

```bash
opensre
```

Windows details: [Windows](docs/install/windows-local.mdx).

The installer fetches the latest build from `main` without requiring sudo. If `opensre` is not found, follow the PATH instructions printed by the installer or open a new terminal.

For supported platforms and troubleshooting, see [Install locally](https://www.opensre.com/docs/install/install-local).

---

## Table of Contents

- [Before you begin](#before-you-begin)
- [Install and start opensre](#step-1-install-and-start-opensre)
- [Why OpenSRE?](#why-opensre)
- [Quick Start](#quick-start)
- [Deployment](#deployment)
- [How OpenSRE Works](#how-opensre-works)
- [Integrations](#integrations)
- [Security](#security)
- [Telemetry](#telemetry)
- [License](#license)
- [Citations](#citations)

---

## Why OpenSRE?

AI writes more of the code every month. Someone still has to fix the build.

When CI goes red, it tells you _that_ something failed, not _why_ or how to fix it. Under deadline pressure, teams hit re-run and move on, flaky checks pile up, `main` stays red, and the real investigation waits for whichever senior engineer has time. OpenSRE is an open-source CI/CD reliability agent that does that investigation for you, built to run on your own infrastructure with your own models:

- **Recover from red builds faster:** it investigates the moment a run fails, reading logs, testing hypotheses and pushing a fix for you to review
- **Fix the cause, not just the rerun:** it separates CI-caused failures from code-caused ones, so you fix the right thing
- **Know what CI is costing you:** failure rate, developer hours lost to unreliable CI, and how long `main` stays red
- **Senior-level context for everyone:** every engineer gets the same depth of analysis

SWE-bench 1  showed that agents improve fastest with realistic tasks and clear feedback. Pipeline failures are slower, noisier and harder to reproduce than local code tasks, so we hold OpenSRE to the same standard by:

- running real-world end-to-end tests across cloud-backed scenarios [(tests/e2e)](tests/e2e)
- keeping semantic tes
