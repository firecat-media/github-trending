The full full-stack framework for Rust 

[![Crates.io][crates-badge]][crates-url]
[![Docs.rs][docs-badge]][docs-url]
[![MIT licensed][mit-badge]][mit-url]
[![Build Status][actions-badge]][actions-url]
[![Discord chat][discord-badge]][discord-url]

[crates-badge]: https://img.shields.io/crates/v/topcoat.svg?style=flat-square
[crates-url]: https://crates.io/crates/topcoat
[docs-badge]: https://img.shields.io/docsrs/topcoat?style=flat-square
[docs-url]: https://docs.rs/topcoat/latest/topcoat
[mit-badge]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
[mit-url]: https://github.com/tokio-rs/topcoat/blob/main/LICENSE
[actions-badge]: https://img.shields.io/github/actions/workflow/status/tokio-rs/topcoat/ci.yml?branch=main&style=flat-square
[actions-url]: https://github.com/tokio-rs/topcoat/actions?query=workflow%3ACI+branch%3Amain
[discord-badge]: https://img.shields.io/discord/500028886025895936.svg?logo=discord&style=flat-square
[discord-url]: https://discord.gg/tokio

Topcoat is a modular, batteries-included Rust framework for building full-stack apps. It prioritizes simplicity and productivity. See [Learn Topcoat](#learn-topcoat) to get started, or the [Roadmap](#roadmap) for what's coming next.

**Early-stage and experimental. Expect breaking changes.**

```rust,ignore
use topcoat::{
    Result,
    context::Cx,
    router::{module_router, page},
    view::{View, component, view},
};

#[tokio::main]
async fn main() {
    topcoat::start(module_router!().build()).await.unwrap();
}

#[page]
async fn home(cx: &Cx) -> Result  {
    Ok(view! {

                hello(name: "World")

    })
}

#[component]
async fn hello(cx: &Cx, name: &str) -> Result  {
    Ok(view! {  "Hello, " (name) "!"  })
}
```

## What makes Topcoat different

### Client reactivity without the boilerplate

Topcoat renders all markup on the server: components can be async and query the database directly, eliminating all the traditional boilerplate needed for a separate API layer. Interactivity does not have to cost a round-trip, though. A `$(...)` expression is ordinary type-checked Rust that Topcoat evaluates on the server for the initial render and also translates to JavaScript, so it re-runs instantly in the browser. No wasm bundle, no client build step:

```rust,ignore
#[component]
async fn faq(cx: &Cx) -> Result  {
    let open = signal(cx, || false);

    Ok(view! {
        // Runs entirely in the browser; no server round-trip.
         "What is Topcoat?" 
         "A full-stack Rust framework." 
    })
}
```

When an update does need the server, like fresh search results, mark the component as a `#[shard]`. Topcoat re-renders it on the server whenever one of its `$(...)` arguments changes and swaps the new HTML in place:

```rust,ignore
#[component]
async fn search(cx: &Cx) -> Result  {
    let query = signal(cx, String::new);

    Ok(view! {

        // Updates as the user types.
        search_results(query: $(query.get()))
    })
}

#[shard]
async fn s
