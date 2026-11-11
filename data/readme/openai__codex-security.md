# Codex Security

Codex Security helps you find, investigate, and fix vulnerabilities in your code.
Use its security workflows in Codex, or automate them with the
`@openai/codex-security` CLI and TypeScript SDK.

- **In Codex:** [choose a security workflow](docs/agent-workflows.md).
- **In a terminal:** [install the CLI and scan your repository](#quick-start).
- **In automation:** use the [TypeScript SDK](#typescript-sdk) or
  [GitHub Action](#github-actions).

## Features

- Scan repositories, selected paths, or Git changes. Deep scans repeat Standard scans and return their deduplicated findings.
- Validate candidate findings, generate patches, and verify existing fixes.
- Draft `SECURITY.md` policies and save threat models for later review.
- Browse saved scans and findings, identify duplicates, assess severity against
  your own rubric, and suggest owners from source and Git history.
- Preview third-party scanner findings, save them locally, or publish supported reports to Codex Security Cloud. [Scanner import guides](docs/scanner-imports/README.md).
- Track findings in Linear, Jira, or GitHub, publish completed scans, or export SARIF, JSON, and CSV. [Integration workflows](docs/plugin-connectors.md).
- Automate scans across repositories or project components, including in CI and
  containers.

## Use in Codex

Open your repository in a Codex session with the Codex Security plugin enabled,
then ask:

> Run a Codex Security scan on this repository, focusing on authentication and
> authorization. Return the saved report, source evidence, and coverage limits.

A completed scan saves a report and findings. Read the report for source
evidence and exclusions, then request a patch or ask Codex to verify an
existing fix. See the [agent workflow guide](docs/agent-workflows.md) for setup,
task selection, and recovery.

## Quick start

Requires Node.js 22.13.0+ within 22.x, or Node.js 24.x or 26.x, and Python 3.10+.
Python 3.10 also requires `tomli`.

Install the CLI globally and sign in:

```bash
npm install --global @openai/codex-security
cs login
```

Run your first scan from the repository directory:

```bash
cs scan .
```

When the scan completes, open the Markdown file at the **REPORT** path in the
terminal. Run `cs scans show` from the same repository to find its latest
completed scan again. See [scan scope and follow-up work](sdk/typescript/docs/cli.md#understand-scan-scope-and-follow-up-work)
for how to interpret exclusions in the report.

`cs` and `codex-security` run the same CLI. If the short name conflicts with
another command, use `codex-security`. To skip the global install, or if npm
reports an `EEXIST` conflict, use `npx @openai/codex-security` in place of
`cs` for both login and scanning.

For CI, set `OPENAI_API_KEY` or `CODEX_API_KEY` in the scan process's environment.
For a headless machine, see [device or SSH login](sdk/typescript/docs/cli.md#authentication).

### Scan options

Choose a scope and scan mode:

```bash
# Scan selected 
