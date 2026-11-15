#   AG-UI: The Agent-User Interaction Protocol

AG-UI is an open, lightweight, event-based protocol that standardizes how AI agents connect to user-facing applications.
Built for simplicity and flexibility, it enables seamless integration between AI agents, real time user context, and user interfaces.

---

[ ](https://www.npmjs.com/package/@ag-ui/core)

  Join our Discord →   &nbsp;&nbsp;&nbsp;   Read the Docs →   &nbsp;&nbsp;&nbsp;   Go to the AG-UI Dojo →   &nbsp;&nbsp;&nbsp;   Follow us →  

## 🚀 Getting Started
Create a new AG-UI application in seconds:
```bash
npx create-ag-ui-app my-agent-app
```

  Useful Links: 

- [The AG-UI Dojo](https://dojo.ag-ui.com/)
- [Build AG-UI-powered applications(Quickstart)](https://docs.ag-ui.com/quickstart/applications)
- [Build new AG-UI framework integrations (Quickstart)](https://go.copilotkit.ai/agui-contribute)
- [Book a call to discuss an AG-UI integration with a new framework](https://calendly.com/markus-copilotkit/ag-ui)
- [Join the Discord Community](https://discord.gg/Jd3FzfdJa8)

## What is AG-UI?

AG-UI is an open, lightweight, event-based protocol for agent-human interaction, designed for simplicity & flexibility:

- During agent executions, agent backends **emit events _compatible_ with one of AG-UI's ~16 standard event types**
- Agent backends can **accept one of a few simple AG-UI compatible inputs** as arguments

**AG-UI includes a flexible middleware layer** that ensures compatibility across diverse environments:

- Works with **any event transport** (SSE, WebSockets, webhooks, etc.)
- Allows for **loose event format matching**, enabling broad agent and app interoperability

It also ships with a **reference HTTP implementation** and **default connector** to help teams get started fast.

[Learn more about the specs →](https://go.copilotkit.ai/ag-ui-introduction)

## Why AG-UI?

AG-UI was developed based on real-world requirements and practical experience building in-app agent interactions.

## Where does AGUI fit in the agentic protocol stack?
AG-UI is complementary to the other 2 top agentic protocols
- MCP gives agents tools
- A2A allows agents to communicate with other agents
- AG-UI brings agents into user-facing applications

## 🚀 Features

- 💬 Real-time agentic chat with streaming
- 🔄 Bi-directional state synchronization
- 🧩 Generative UI and structured messages
- 🧠 Real-time context enrichment
- 🛠️ Frontend tool integration
- 🧑‍💻 Human-in-the-loop collaboration

## 🛠 Supported Integrations

AG-UI was born from CopilotKit's initial **partnership** with LangChain and CrewAI - and brings the incredibly popular agent-user-interactivity infrastructure to the wider agentic ecosystem.

**1st party** = the platforms that have AG‑UI built in and provide documentation for guidance.

## Frameworks

| Framework                                                          | Status                   | AG-UI Resources                                                                 |
| ----------------
