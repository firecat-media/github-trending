# π RuView

[ ](docs/user-guide.md)

      Start here  
      Hardware  
      Models  

      AI toolkit  
      Smart home  
      Cognitum Seed  

## **See through walls with WiFi** ##

**Turn ordinary WiFi into a spatial intelligence / sensing system.** Detect people, measure breathing and heart rate, track movement, and monitor rooms — through walls, in the dark, with no cameras or wearables. Just physics.

Works natively with the four major smart-home ecosystems: **[Home Assistant](docs/integrations/home-assistant.md)** via the HA-DISCO MQTT publisher, **[Apple Home & HomePod](docs/user-guide-apple-homepod.md)** as a discoverable HAP-1.1 bridge, **[Google Home](docs/integrations/home-assistant.md)** + **[Amazon Alexa](docs/integrations/home-assistant.md)** via the same HA bridge or a [Matter](docs/adr/ADR-122-bfld-ruview-ha-matter-exposure.md) endpoint. Siri, Google Assistant, and Alexa can voice presence and vitals by room with zero custom skills.

[ ](docs/integrations/home-assistant.md) [ ](docs/adr/ADR-122-bfld-ruview-ha-matter-exposure.md) [ ](docs/user-guide-apple-homepod.md) [ ](docs/integrations/home-assistant.md) [ ](docs/integrations/home-assistant.md)

> Drop into any **Home Assistant** install with one `--mqtt` flag. Or pair into **Apple Home / Google Home / Alexa / SmartThings** as a Matter Bridge. Ships 21 entities per node (11 raw signals + 10 inferred semantic states: someone-sleeping, possible-distress, room-active, elderly-inactivity-anomaly, meeting-in-progress, bathroom-occupied, fall-risk-elevated, bed-exit, no-movement, multi-room-transition) plus 3 starter HA Blueprints. See [`docs/integrations/home-assistant.md`](docs/integrations/home-assistant.md) · [ADR-115](docs/adr/ADR-115-home-assistant-integration.md).

### π RuView is a WiFi sensing platform that turns radio signals into spatial intelligence.

Every WiFi router already fills your space with radio waves. When people move, breathe, or even sit still, they disturb those waves in measurable ways. RuView captures these disturbances using Channel State Information (CSI) from low-cost ESP32 sensors and turns them into actionable data: who's there, what they're doing, and whether they're okay.

[ ](docs/user-guide.md)

**What it senses:**
- **Presence and occupancy** — detect people through walls, count them, track entries and exits
- **Vital signs** — breathing rate and heart rate, contactless, while sleeping or sitting
- **Activity recognition** — walking, sitting, gestures, falls — from temporal CSI patterns
- **Environment mapping** — RF fingerprinting identifies rooms, detects moved furniture, spots new objects
- **Sleep quality** — overnight monitoring with sleep stage classification and apnea screening

**Also included:**

- **Camera-free pose** — estimate 17 body keypoints from WiFi CSI
- **Built-in model workflow** — record CSI, train models, load RVF files, and switch LoRA profiles
- **Local automation** — HOMECORE provides state, history, automations, sign
