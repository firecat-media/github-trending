# SkillEvaluator

[ ](LICENSE)
[ ](https://www.python.org/)
[ ](https://pypi.org/project/skillevaluator/)
[ ](https://docs.nvidia.com/skills/skillevaluator/)
[ ](https://arxiv.org/abs/2608.20614)
[ ](https://developer.nvidia.com/blog/evaluating-ai-agent-skill-performance-with-nvidia-skillevaluator/)

> 📺 **Livestream:** [Ask the Experts: Evaluating Agent Skills](https://www.youtube.com/watch?v=4rI0zATFxYI)

SkillEvaluator checks AI agent skills and measures their effect on task results:
start with quality checks, then compare runs with and without a skill.

Agent skills are folders of instructions and supporting files defined by the
[Agent Skills specification](https://agentskills.io/). SkillEvaluator is part of
the [NVIDIA Verified Skills pipeline](https://github.com/NVIDIA/skills).

## Get started

Three ways in, one CLI, same results.

 1. Run the CLI directly 
 2. Add it to your repo via CI 
 3. Wire it to your agent 

Install with pip:

```bash
pip install skillevaluator
```

  Or install with uv 

```bash
uv tool install \
  skillevaluator
```

Then check your skill, no API key:

```bash
skillevaluator validate \
  ./my-skill --tiers 1
```

Other tiers: [installation guide](https://docs.nvidia.com/skills/skillevaluator/installation).

Run this in your GitHub repository. It opens a setup PR:

```bash
skillevaluator ci init
```

GitLab and details: [repository guide](https://docs.nvidia.com/skills/skillevaluator/repository-integration).

Add the skill to Claude Code, Codex or another agent:

```bash
npx skills add \
  NVIDIA/SkillEvaluator
```

Then ask: *"Is my skill any good?"* It runs the CLI from step 1.
See the [agent guide](https://docs.nvidia.com/skills/skillevaluator/agent-skill).

## Quickstart

Both paths use bundled `text-analyzer`.

| Start here | Requires | First result |
| --- | --- | --- |
| [Run without an LLM](#run-without-an-llm) | Git and uv | A deterministic quality score and findings |
| [Use NVIDIA Build](#use-nvidia-build) | Git, uv, and a Build API key | Model-backed rubric scores and feedback |

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and Git,
then get the example:

```bash
git clone --depth 1 https://github.com/NVIDIA/SkillEvaluator.git
cd SkillEvaluator
```

uv provisions Python 3.13 and dependencies. For standalone installation, see
[Installation](https://docs.nvidia.com/skills/skillevaluator/installation).

### Run without an LLM

```bash
uv run --python 3.13 skillevaluator quality-check \
  src/skillevaluator/tier3/reference_skills/text-analyzer \
  -r cli -r json -o reports/first-quality
```

No API key, scanner, GPU or Docker is needed. The example scores **88.8/100 (B)**,
exits `0` and saves `reports/first-quality/skillevaluator-quality.json`. The
passing threshold defaults to 70.

This checks static quality; publication evidence stays `INCOMPLETE`. Security
needs scanners; agent impact needs live evaluation. Replace the example path
with your skill directory. See the
[keyless wal
