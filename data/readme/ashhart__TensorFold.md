# TensorFold

TensorFold serves language models from a Zig binary on Apple Silicon and NVIDIA GPUs.
The engine reads checkpoints, tokenizes requests and runs Metal or CUDA kernels directly.
Serving needs no Python or MLX installation.

Building with a coding agent? Have it load the [contributor skill](docs/recipes/SKILL.md) before it writes any code.

## Contributing with agents

Please use [Agent Traffic Control](https://github.com/ashhart/ATC) before editing TensorFold so contributors and agents can avoid duplicate work and conflicting changes.
Check the [live agent radar](https://tensorfold.dev/atc) before choosing an issue and follow [CONTRIBUTING.md](CONTRIBUTING.md) and the [ATC contributor instructions](docs/atc/SKILL.md).

Install or upgrade ATC to 0.9.4 or later, then run from an updated TensorFold clone:

```sh
npm install -g github:ashhart/ATC
atc check ISSUE --json
atc claim ISSUE --json
```

Replace `ISSUE` with the issue number and claim only after a complete check says the work is free.
TensorFold enables automatic public check-ins: a successful new claim starts an anonymous session on the radar and returns its `session` number.
Keep that number instead of starting a duplicate session.
For work already yours, start a session with `atc start ISSUE --json`.
Add `--github-name` to `claim` or `start` only if you want your verified GitHub name shown; `--local` keeps a new session on your machine.
The board shows the issue, activity state and last check-in; GitHub still associates the verification comment with its author.
Check that `publication` is `public`; `unavailable` means the public update failed even if the local claim or session succeeded.

Pulse only while the agent is working, before its five-minute check-in expires:

```sh
atc pulse ISSUE SESSION working --json
atc who path/to/file --json
atc overlap --json
atc land ISSUE SESSION --json
atc release ISSUE --json
```

Use `reviewing` or `blocked` when appropriate, land the session when it stops, and resolve overlaps before opening a pull request.
Before opening a pull request, have the agent run the [pull request skill](docs/pr/SKILL.md); agents that support skills can install it as `tensorfold-pull-request`.

## Quick start

Start with Qwen3.5-2B, the small 4-bit checkpoint checked on Metal and a GB10. The commands below download its
pinned revision, then serve it as `local-model`. Model weights have their own licenses.
Reviewing or benchmarking TensorFold? [Evaluating TensorFold](docs/evaluating.md) covers pinning, signature checks,
a container and the tests that need no GPU.

### Mac with Apple Silicon

Install with Homebrew, then start the server:

```sh
brew install ashhart/tensorfold/tensorfold
tensorfold pull mlx-community/Qwen3.5-2B-MLX-4bit@93760be4f1f69842a46bc13dbdc0f19e291392a3
tensorfold serve mlx-community/Qwen3.5-2B-MLX-4bit --name local-model --context 8192 --no-thinking
```

### Linux with an NVIDIA GPU

Use the release archive for your CPU: `linux-aarch64` on 
