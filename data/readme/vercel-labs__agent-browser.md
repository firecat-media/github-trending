# agent-browser

Browser automation for AI agents: open pages, read them as an accessibility tree, and act on elements from the shell.

agent-browser is a native Rust CLI that gives an AI agent a browser it can drive one command at a time. `snapshot` returns the page as compact text with a ref such as `@e1` for each element. The agent acts on a ref, reads the page again to check the result, and repeats. The browser stays open between commands, so each step is one short shell call.

## Install

```bash
npm install -g agent-browser
agent-browser install           # download Chrome for Testing (first time only)
```

- **Homebrew:** `brew install agent-browser`, then `agent-browser install`.
- **Linux:** `agent-browser install --with-deps` also installs the browser's system libraries.
- **No install:** `npx agent-browser open example.com`.

Project installs, building from source, `upgrade`, and `doctor` are covered in [Installation](https://agent-browser.dev/installation).

## Quick start

```bash
agent-browser open example.com
agent-browser snapshot -i       # interactive elements, each with a ref
agent-browser click @e1         # act on a ref from that snapshot
agent-browser get url           # check the result
agent-browser close
```

The snapshot for `example.com`:

```
- link "Learn more" [ref=e1]
```

- Refs describe the page at the time of the snapshot. After navigation or a DOM change, take a new snapshot before using refs again.
- CSS selectors, text, XPath, and semantic locators also work, for example `agent-browser find role button click --name "Submit"`. See [Selectors](https://agent-browser.dev/selectors).
- A click fails, instead of reporting success, when the target is hidden, disabled, outside the viewport, or covered by another element such as a consent banner. Dismiss the covering element, take a new snapshot, and retry.

The full walkthrough is in the [quick start](https://agent-browser.dev/quick-start).

## How it works

The CLI sends each command to a background daemon that starts on the first command and controls the browser over the Chrome DevTools Protocol. Each `--session` gets its own daemon and browser. By default, the daemon closes a headless browser and exits after one hour without commands, saving state first when [session persistence](https://agent-browser.dev/sessions) is configured.

Chrome for Testing is the default browser. You can also attach to a running Chrome with `--cdp` or `--auto-connect` ([CDP mode](https://agent-browser.dev/cdp-mode)), select the [Lightpanda](https://agent-browser.dev/engines/lightpanda) or [Obscura](https://agent-browser.dev/engines/obscura) engine with `--engine`, drive Mobile Safari in the [iOS Simulator](https://agent-browser.dev/ios), or use a cloud browser provider such as [Browserbase](https://agent-browser.dev/providers/browserbase), [Browserless](https://agent-browser.dev/providers/browserless), [Browser Use](https://agent-browser.dev/providers/browser-use), [Kernel](https://agent-
