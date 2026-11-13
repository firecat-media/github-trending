"Tailscale without Tailscale, by Tailscale"  

# Tailcat

Tailcat is a remix of Tailscale open source pieces to act like
[netcat](https://en.wikipedia.org/wiki/Netcat), but over Tailscale's data plane,
without Tailscale's control plane. Tailscale's data plane (`magicsock`,
internally) gives you point-to-point WireGuard®-encrypted tunnels between two
machines with DERP as the NAT-hole-punching communication side channel and the
ultimate relay-of-last-resort if NAT traversal fails. Instead of using the
Tailscale control plane, all `tailcat` connection metadata is exchanged out of
band, however you want.

The `tailcat` CLI (in `cmd/tailcat`) is built on the `tailcat` Go library
(importable as [`github.com/tailscale/tailcat`](https://pkg.go.dev/github.com/tailscale/tailcat)).

Whether you use `tailcat` as a CLI tool or library, one side runs a `tailcat`
server (listener) and gets back a short tailcat address. The other side passes
that tailcat address to `tailcat`'s client side to connect. All traffic between
the two is
encrypted end-to-end with WireGuard. The initial connection bootstraps through
a DERP server ([see below](#bring-your-own-derp-relay)), and then magicsock performs NAT traversal to
upgrade to a direct peer-to-peer UDP connection when possible (usually!).

You don't need a Tailscale account, root/admin access on the machine
(it doesn't alter your machine's routing tables, DNS, etc.). It's just
a userspace library and CLI tool.

And it's all open source.

You can use our free rate-limited DERP relays (the default DERP map is
https://tailcat.dev/derpmap.json) or you can [run your own](https://github.com/tailscale/tailscale/tree/main/cmd/derper#derp).

There's also an experimental in-browser web demo (tailcat compiled to
WebAssembly) at https://tailscale.github.io/tailcat/ that can send and
receive files or text, interoperating with the CLI. Browser traffic is
relayed over DERP only, with no direct connections until WebRTC
support ([#4](https://github.com/tailscale/tailcat/issues/4)).

## Install

See [INSTALL.md](./INSTALL.md) for details on each, including notes
for packagers building from source:

| Method | Linux | macOS | Windows | FreeBSD, OpenBSD | Browser (js/wasm) |
|--------|:-----:|:-----:|:-------:|:-------------------:|:--------------------:|
| [Static binaries](INSTALL.md#prebuilt-binaries) | ✅ | | ✅ | | |
| [.deb packages](INSTALL.md#prebuilt-binaries) | Debian, Ubuntu, ... | | | | |
| [.rpm packages](INSTALL.md#prebuilt-binaries) | Red Hat, Fedora, ... | | | | |
| [Homebrew](INSTALL.md#homebrew-macos) | | ✅ | | | |
| [Scoop](INSTALL.md#scoop-windows) | | | ✅ | | |
| [Snap](INSTALL.md#snap-linux) | ✅ | | | | |
| [Container image](INSTALL.md#container-image) | ✅ | | | | |
| [Nix](INSTALL.md#nix) | ✅ | ✅ | | | |
| [AUR](INSTALL.md#arch-linux-aur) | Arch | | | | |
| [conda-forge](INSTALL.md#conda-forge) | ✅ | ✅ | ✅ | | |
| [Build from source](INSTALL.md#go-toolchain) | ✅ | ✅ | ✅ | ✅ | ✅ |

## Usage

### Pipe stdin/stdout betwe
