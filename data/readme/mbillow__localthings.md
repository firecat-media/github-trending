# LocalThings

**Control your Samsung appliances from Home Assistant over your home network, with no cloud account.**

LocalThings connects Home Assistant to Samsung washers, dryers, refrigerators, air conditioners, ovens and other appliances that work with the SmartThings app. It talks to each appliance on your local network.

- **Updates are fast.** Appliances that support push send changes as they happen. LocalThings checks the rest every 30 seconds.
- **It works without the internet.** After setup, LocalThings never contacts Samsung's servers.
- **Your data stays home.** LocalThings sends nothing to Samsung. The appliance itself still keeps its own connection to Samsung, and LocalThings doesn't change that.
- **Setup needs an IP address.** For most appliances, you enter the address and LocalThings works out the type and model, then creates matching controls and sensors.

## What it supports

| Appliance | Appliance |
|---|---|
| Air conditioner, including multi-unit systems | Microwave |
| Air dresser | Oven |
| Air monitor | Range and range hood |
| Air purifier | Refrigerator, kimchi refrigerator, wine cellar |
| Cooktop, gas, radiant electric and induction; some models read-only | Robot vacuum, early support |
| Dehumidifier | Soundbar, settings and status |
| Dishwasher | Vacuum clean station |
| Dryer | Washer and washer-dryer |
| EHS heat pump | Water purifier |

What you see depends on what each appliance reports. Typical controls and sensors include power, program or mode selection, start, pause and stop, temperatures and setpoints, time remaining and finish time, door and child-lock state, energy use, filter status and alarms.

Most Samsung appliances from about 2022 onward work, and so do some earlier washers, air conditioners and wall ovens that use an older local interface. See [Older appliances on TCP 8888](#older-appliances-on-tcp-8888). Setup detects which interface an appliance has, and tells you if it finds none.

If an appliance sets up but LocalThings doesn't recognize it, or a control is missing, Home Assistant shows a notice asking for a diagnostics download. That download is usually all the maintainers need to add support. See [Reporting a capability gap](#reporting-a-capability-gap).

## Built on open standards

LocalThings uses the standards the appliances implement:

- **OCF, the [Open Connectivity Foundation](https://openconnectivity.org/) specification.** Samsung's connected appliances are OCF devices. LocalThings discovers each appliance's resources through `/oic/res` and reads its device type, such as `oic.d.washer`, from `/oic/d`. Where an appliance offers both a standard OCF resource and a Samsung extension for the same state, LocalThings uses the standard one.
- **CoAP over DTLS.** LocalThings sends Constrained Application Protocol requests, defined in [RFC 7252](https://www.rfc-editor.org/rfc/rfc7252), over an encrypted DTLS session with an X.509 client certificate. It uses CoAP Observe, [RFC 7641](https://www
