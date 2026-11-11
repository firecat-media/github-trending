#   Modern Web Guidance (Source)

This repo is the source repository for [GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance) and includes the code and documentation for authoring, calibrating, and evaluating its contents.

[**Modern Web Guidance**](https://developer.chrome.com/docs/modern-web-guidance) is a set of skills that embed web platform expertise, best practices, and browser compatibility data directly into your coding agents. It helps to steer your coding agents away from legacy patterns, and instead toward solutions that harness the power and capabilities of the modern web platform.

See [CONTRIBUTING.md](./CONTRIBUTING.md) and [GOVERNANCE.md](./GOVERNANCE.md) for how we work on the project and orientation of the codebase.

---

*Stewarded by the Google Chrome, Microsoft Edge, Mozilla Firefox, and MDN teams, alongside the web development community.*

[Documentation](https://developer.chrome.com/docs/modern-web-guidance) · [Eval Dashboard](https://googlechrome.github.io/modern-web-guidance-src/) · [Source Code](https://github.com/GoogleChrome/modern-web-guidance-src) · [Report an Issue](https://github.com/GoogleChrome/modern-web-guidance-src/issues)

##   Quickstart

```shell
npx modern-web-guidance@latest install
```

This command runs an interactive wizard to install Modern Web Guidance. See [Alternative Installation Methods](#-alternative-installation-methods) below.

#### Try it out (without installing)

```shell
# Search for relevant guides
npx modern-web-guidance@latest search "animate a dialog modal backdrop"

# Retrieve a guide by ID
npx modern-web-guidance@latest retrieve "animate-to-from-top-layer"

# Scan a codebase for legacy patterns to modernize
npx modern-web-guidance@latest legacy-scan .
```

##   Why?

Coding agents often default to older patterns because LLM training data contains vast amounts of legacy code. This often leads them to generate bloated JavaScript for tasks that now have native, high-performance web platform solutions.

Even if a model knows an API exists, it often lacks the density of real-world, modern implementation patterns required for production-ready code.

**Modern Web Guidance bridges this gap.** Our skill's CLI returns targeted, expert-curated guidelines directly into your agent's context window, focusing on:
* **Modern Browser APIs**: Helping models correctly structure APIs they frequently misuse.
* **Performance & Accessibility**: Preferring platform-level APIs that can be optimized by the browser and include built-in accessibility affordances.
* **Responsible Fallbacks**: Guiding models to use sensible, lightweight fallbacks instead of heavy polyfills or legacy libraries.

##   What's Included?

We cover the past several years of the web platform's new features, all the way up to the cutting edge. The guides are **designed to be token-efficient**; we run evals enabling us to prune lowest-common-denominator content that models already know.

### Core Discipli
