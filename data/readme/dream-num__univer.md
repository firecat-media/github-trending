Build your own AI office with Univer Office SDK. 

 Start with open-source Sheets and Docs, then connect your own application or agent. 

  🚀 Quick start  ·  📚 Documentation  ·  ⚖️ Feature comparison  ·  🌐 Website  ·  🎮 Showcase  ·  🔧 API Reference  ·  📝 Blog  

  English  ·  Français  ·  Deutsch  ·  Español  ·  简体中文  ·  繁體中文  ·  日本語  ·  한국어  

 Table of contents 

- [💡 What is Univer?](#what-is-univer)
  - [Open-source capabilities](#open-source-capabilities)
- [🚀 Build on the open-source foundation](#what-you-can-build)
  - [Quick start: an open-source spreadsheet editor](#quick-start)
  - [Connect your application to editable content](#connect-your-application-to-editable-content)
- [🏗️ Explore the open-source architecture](#open-source-architecture)
  - [Give custom features clear boundaries](#give-custom-features-clear-boundaries)
  - [Compose cross-feature edits and undo/redo](#compose-cross-feature-edits-and-undoredo)
  - [Connect applications and agents through Facade APIs and events](#connect-applications-and-agents-through-facade-apis-and-events)
- [🧩 Extend your application with Univer Office SDK](#open-source-and-commercial-extensions)
  - [Scope and licensing](#scope-and-licensing)
- [🌐 Application patterns and ecosystem](#application-patterns-and-ecosystem)
  - [Univer Workspace: an Office SDK reference application](#univer-workspace-an-office-sdk-reference-application)
  - [CLI, agent integrations, and developer skills](#cli-agent-integrations-and-developer-skills)
- [📚 Documentation and contributing](#documentation-and-contributing)
  - [Runtime compatibility](#runtime-compatibility)
- [💬 Community](#community)
- [🔒 Security](#security)
- [❤️ Sponsors](#sponsors)
- [📄 License](#license)

## 💡 What is Univer?

**Univer** is an Office SDK for building Office applications inside your own product. It provides Office editing, calculation, collaboration, and file processing for people and existing agents, using your data and permissions. The product family covers spreadsheets, documents, presentations, relational tables, canvases, and PDFs.

Univer Office SDK has three parts:

- **Web SDK** is the foundation: content models, editing, rendering, formula calculation, and Facade APIs (application-facing APIs). Compose its plugins into an embedded editor or your own Office application, and reuse the content models, commands, and calculation for Headless processing without an interactive editor.
- **Server SDK** adds backend services for real-time collaboration, edit history, and Office file import and export.
- **AI SDK** connects Office capabilities to existing agents and workflows, with content tools, execution, and review integrations.

**This repository provides the Web SDK's core architecture and engine implementations under Apache-2.0**: content models and snapshot formats, plugin and dependency management, the command system, formula and rendering engines, Facade APIs, UI foundation, and Sheets and Docs editing capabilities. Commerci
