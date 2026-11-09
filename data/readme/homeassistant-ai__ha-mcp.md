> **Breaking change (v7.3.0):** `ha_config_set_yaml` has been moved to [beta](docs/beta.md).

  # HA-MCP — Manage Home Assistant with AI

     Configure and automate Home Assistant with Claude, ChatGPT, and other AI assistants. 

---

---

## 🚀 Get Started

The recommended way to run ha-mcp is the **HA-MCP integration**. It installs into Home Assistant through HACS (the built-in Marketplace on Home Assistant 2026.11+), runs the full server **in-process**, and works on **every** Home Assistant installation type — Home Assistant OS, Supervised, Container, and Core — with full feature parity. It is the easiest setup in every case: setup asks for an administrator access token and how clients may connect.

**Add it to Home Assistant via HACS or, on Home Assistant 2026.11+, the Marketplace (the preferred install):**

[ ](https://my.home-assistant.io/redirect/hacs_repository/?owner=homeassistant-ai&repository=ha-mcp&category=integration)

**Quick start:**

> The setup below is for version 9.0.0 (October 28, 2026) and later; earlier versions show a shorter setup form without the administrator account step.

1. Install the **HA-MCP integration** (requires **Home Assistant 2026.8.0 or newer**; see [compatibility details](docs/in-process-server.md#requirements)). On **Home Assistant 2026.8–2026.10**, open HACS, search for **HA-MCP**, then **Download**.
   On **Home Assistant 2026.11 or newer**, open **Settings → Marketplace**, accept its first-run warning, and search for **HA-MCP**, then **Install**. HA-MCP is in the default catalog, so installing it and receiving its updates do not require connecting GitHub or adding a custom repository. The badge above also opens its catalog page.
   Already installed from the earlier `homeassistant-ai/ha-mcp-integration` repository? It keeps receiving the same releases. On the Marketplace, keep GitHub connected for its background checks on that custom repository.
   Older installed releases may still appear as **HA-MCP Custom Component**; searching for **HA-MCP** matches both names.
2. **Restart Home Assistant.**
3. Decide which administrator account the server acts as. Either create a long-lived access token on your own account (your profile → **Security** → **Long-lived access tokens** → **Create token**; it works from anywhere if it leaks, and the server's changes show under your name), or, safer, create an account just for HA-MCP under **Settings → People → Add person** with **Allow login**, **Local access only** and **Administrator** on. Never use your own login for the second option.
4. Go to **Settings → Devices & Services → Add Integration**, search for **HA-MCP** and choose **HA-MCP Server**. Paste your token, or enter the user name and password of the account you made for HA-MCP (HA-MCP creates its token), pick how clients may connect — **Remote access through Home Assistant** (start with **Secret URL**, the simplest; **Home Assistant sign-in** adds a login) and/or **Network access: Local network** — then click
