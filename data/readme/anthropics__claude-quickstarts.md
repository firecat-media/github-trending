# Claude Quickstarts

Claude Quickstarts is a collection of projects designed to help developers quickly get started with building  applications using the Claude API. Each quickstart provides a foundation that you can easily build upon and customize for your specific needs.

## Getting Started

To use these quickstarts, you'll need an Claude API key. If you don't have one yet, you can sign up for free at [console.anthropic.com](https://console.anthropic.com).

## Available Quickstarts

### Customer Support Agent

A customer support agent powered by Claude. This project demonstrates how to leverage Claude's natural language understanding and generation capabilities to create an AI-assisted customer support system with access to a knowledge base.

[Go to Customer Support Agent Quickstart](./customer-support-agent)

### Financial Data Analyst

A financial data analyst powered by Claude. This project demonstrates how to leverage Claude's capabilities with interactive data visualization to analyze financial data via chat.

[Go to Financial Data Analyst Quickstart](./financial-data-analyst)

### Computer Use Demo

An environment and tools that Claude can use to control a desktop computer. This project demonstrates how to leverage the computer use capabilities of Claude, including support for the latest `computer_toolset_20260801` toolset shape, where each computer action is a member tool the model calls by name.

[Go to Computer Use Demo Quickstart](./computer-use-demo)

### Computer Use Best Practices

A pedagogical, native-macOS reference implementation of a computer-use agent. Unlike the containerized Computer Use Demo, this project runs directly against the macOS desktop (run it in a VM!) and demonstrates common patterns for building more reliable and cost-effective computer-use agents: explicit tool definitions, correct image sizing and pruning, prompt caching, server-side compaction, batched tool calls, a sandboxed shell, and trajectory recording. It pairs with Anthropic's [computer-use best-practices guide](https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude).

[Go to Computer Use Best Practices Quickstart](./computer-use-best-practices)

### Browser Use Demo

A complete reference implementation for browser automation powered by Claude. This project demonstrates how to give Claude the ability to navigate websites, inspect and interact with DOM elements, extract content, and fill forms using a custom Playwright-backed browser tool.

[Go to Browser Use Demo Quickstart](./browser-use-demo)

### Browser Toolset Quickstart

The minimal CDP example of Claude's browser toolset (`browser_toolset_20260801`), in Python and TypeScript. It has a small driver for one Chromium tab over the Chrome DevTools Protocol, a script that runs the driver with the tool runner, and a script that exercises it without a model. It shows the interface and is not production code.

[Go to Browser Toolset Quickstart](./browser-toolset)

### Computer 
