[ ](https://github.com/solidjs/solid/actions/workflows/main-ci.yml)
[ ](https://coveralls.io/github/solidjs/solid?branch=main)

[ ](https://www.npmjs.com/package/solid-js)
[ ](https://www.npmjs.com/package/solid-js)
[ ](https://discord.com/invite/solidjs)
[ ](https://www.reddit.com/r/solidjs/)

**[Website](https://www.solidjs.com/) • [Docs](https://docs.solidjs.com/) • [Tutorial](https://docs.solidjs.com/tutorial) • [Playground](https://playground.solidjs.com/) • [Discord](https://discord.com/invite/solidjs)**

Solid is a declarative JavaScript library for building user interfaces. Instead of a Virtual DOM, it compiles templates to real DOM nodes and updates them with fine-grained reactivity. Declare your state and use it throughout your app — when a piece of state changes, only the code that depends on it re-runs.

## At a glance

```tsx
import { createSignal } from "solid-js";
import { render } from "@solidjs/web";

function Counter() {
  const [count, setCount] = createSignal(0);
  const doubled = () => count() * 2;

  // The component body runs once. Only `{doubled()}` updates when count changes.
  return   setCount(c => c + 1)}>{doubled()} ;
}

render(() =>  , document.getElementById("app")!);
```

Try it in our [Playground](https://playground.solidjs.com/).

 Explain this! 

Solid compiles your JSX to real DOM operations at build time. The component function runs once on mount; reactivity is per-expression, not per-render. The `{doubled()}` expression compiles to a tracked update that only touches that one DOM position when `count()` changes.

```js
import { template, delegateEvents, insert } from "@solidjs/web";
import { createSignal } from "solid-js";

const _tmpl$ = /*#__PURE__*/ template(` `);

function Counter() {
  const [count, setCount] = createSignal(0);
  const doubled = () => count() * 2;

  return (() => {
    const _el$ = _tmpl$();
    _el$._$$click = () => setCount(c => c + 1);
    insert(_el$, doubled);
    return _el$;
  })();
}
delegateEvents(["click"]);
```

Reads update on the next microtask (or call `flush()` for synchronous interop). Effects are split into a tracking `compute` phase and a side-effecting `apply` phase — see the [docs](https://docs.solidjs.com) for the full model.

## Key features

- Fine-grained updates to the real DOM — no virtual DOM diff.
- Declarative reactive primitives (`createSignal`, `createMemo`, `createStore`).
- Render-once components — your component function is plain JavaScript that runs once.
- Automatic dependency tracking — reading reactive state subscribes to it.
- Microtask-batched updates with `flush()` for synchronous interop.
- First-class async: any computation can return a `Promise`/`AsyncIterable`; ` ` is the boundary.
- Optimistic UI primitives (`createOptimistic`, `createOptimisticStore`) and structured `action(...)` mutations.
- Streaming SSR and progressive hydration.
- TypeScript-first, JSX-first, web-component friendly.
- Universal: write custom renderers via [`@solidjs/univ
