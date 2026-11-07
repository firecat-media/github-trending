# Astryx

An open source design system that's fully customizable and built for how we build now:   by people and the agents working alongside them.

**Currently in Beta** · Built on [React 19+](https://react.dev) and [StyleX](https://stylexjs.com)

[ ](https://www.npmjs.com/package/@astryxdesign/core)
[ ](LICENSE)
[ ](https://github.com/meta/astryx/wiki/Contributing)

[ ](https://astryx.atmeta.com)
[ ](https://astryx.atmeta.com/storybook/)
[ ](https://astryx.atmeta.com/sandbox/)

**[Docs](https://astryx.atmeta.com)** · **[Storybook](https://astryx.atmeta.com/storybook/)** · **[Sandbox](https://astryx.atmeta.com/sandbox/)** · **[Contributing](https://github.com/meta/astryx/wiki/Contributing)** · **[Discord](https://discord.com/invite/XnsUcFykEP)**

## Overview

Astryx is an open source design system that grew inside Meta over the last eight years, where it became the most-used and largest design system in the company — powering 13,000+ apps and shaped by the engineers, designers, and product teams who depend on it every day.

It ships 150+ accessible components, brand-level theming, dark mode, ready-to-ship templates, and a CLI as one cohesive system. You import pre-built CSS and use typed React components — no build plugin, no styling library to adopt — and both people and AI assistants build with the same tooling.

**What makes Astryx different:**

- **Open internals.** Components are built to be composed at any level, not locked behind a closed top-level API. The building blocks you'd reach for are exported directly, and when you need to go deeper, swizzle ejects a component's full source into your project to own.
- **No styling lock-in.** Astryx authors its styles with StyleX, but that's invisible to consumers. Override with `className` using Tailwind, CSS modules, or plain CSS — whatever your project already uses.
- **Customize without wrapping.** A theme is a set of CSS custom property overrides, so a designer can make Astryx unmistakably theirs without forking or wrapping component source.
- **Built for people and agents.** The API, docs, and CLI are designed together so a person and an AI assistant build the same way, from the same reference.

## Getting Started

Astryx requires **React 19** or later (`react` and `react-dom` are peer dependencies of `@astryxdesign/core`).

Install Astryx, a theme, and its peer dependencies:

```bash
# npm
npm install @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex
npm install -D @astryxdesign/cli

# pnpm
pnpm add @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex
pnpm add -D @astryxdesign/cli

# yarn
yarn add @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex
yarn add -D @astryxdesign/cli
```

You can also install the CLI once for your computer, so `astryx` works in any folder and every coding agent knows Astryx; in a project, it still runs that project's own version:

```bash
npm i -g @astryxdesign/cli
```

Project install, global install, or both? `astryx docs gl
