# improve

An agent skill that audits any codebase and writes implementation plans for other agents to execute.

The idea: use your most capable model for the part where intelligence compounds — understanding the codebase, judging what's worth doing, writing the spec — and hand execution to cheaper models. The skill never implements anything itself. The plan is the product.

```
you          →  /improve                    (expensive model, advises)
plans/       →  001-fix-n-plus-one.md       (self-contained specs)
other agent  →  implements, tests, ships    (cheap model, executes)
```

## Install

```bash
npx skills add shadcn/improve
```

Works in any agent that supports [Agent Skills](https://agentskills.io) format. The plans it writes are plain markdown, so any agent (or human) can pick them up.

## Usage

```
/improve                        full audit → prioritized findings → plans
/improve quick                  cheap pass: hotspots, top findings only
/improve deep                   exhaustive: every package, every category
/improve security               focused audit (also: perf, tests, bugs, ...)
/improve branch                 audit only what the current branch changes
/improve next                   feature suggestions — where to take the project
/improve plan       skip the audit, spec one thing
/improve review-plan       critique and tighten an existing plan
/improve execute           dispatch a cheaper executor, review its work
/improve reconcile              refresh the backlog: verify, unblock, retire
/improve ... --issues           also publish plans as GitHub issues
```

## How to use

A typical first run, start to finish:

1. Open your agent in the repo and run `/improve` (or `/improve quick` to keep it cheap).
2. It maps the repo, audits it, and comes back with a findings table. Reply with the ones you want planned — "plan 1, 3 and 5".
3. Plans land in `plans/` — one file each, plus an index with the recommended order. Read them; they're meant to be reviewed.
4. Hand a plan to any agent ("implement plans/001-*.md"), or let the skill run it: `/improve execute 001`. It dispatches a cheaper model in an isolated worktree, reviews the diff against the plan, and reports back with a verdict. Merging stays up to you.
5. Next session, run `/improve reconcile` to clean up the backlog: verify what landed, refresh what drifted, unblock what got stuck.

Before a PR, `/improve branch` does the same thing scoped to just what your branch changes.

## Example

A run against [shadcn/ui](https://github.com/shadcn-ui/ui) came back with findings like:

```
| # | Finding                                        | Category  | Effort | Confidence |
|---|------------------------------------------------|-----------|--------|------------|
| 1 | shadow-config duplicated in search.ts/view.ts, | tech-debt | M      | HIGH       |
|   | copies already drifted (TODO at search.ts:31)  |           |        |            |
| 2 | O(n²) icon migration (migrate-icons.t
