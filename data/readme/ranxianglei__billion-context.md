# billion-context

  English  |  中文  

  Context-compression plugin  —  billion-context is all you need.  

  small context windows (100K is enough) ·  5× fewer tokens  · month-long single sessions (billions of tokens) · high compression quality  

 npm install -g billion-context --prefix=~/.local 

   &nbsp;
      &nbsp;
      &nbsp;
      &nbsp;
   &nbsp;
      &nbsp;
   &nbsp;
      &nbsp;
   &nbsp;
   &nbsp;
   &nbsp;
   &nbsp;
   &nbsp;
   &nbsp;
   &nbsp;
   &nbsp;
   &nbsp;
   &nbsp;
      &nbsp;
   &nbsp;
   &nbsp;
   &nbsp;

---

> **Cache health at a glance:** a healthy session keeps a **95–97%** prefix-cache hit rate — compression itself costs ≤2%. Sustained lower? Check attribution with `/acp` or `/acp-cache` (see [FAQ](#faq)); usual causes, in order: upstream cache TTL expiry · model switch · a bili bug (please report) · other/unknown.

## Community

QQ Group:
1056132097 (full)
1108730198 (full)
1129868472 (open)

---

## 📄 Paper / Preprint

- **[Model-Driven Incremental Hierarchical Compression: Training-Free Multi-Generational Context Management for Long-Lived Coding Agents](./paper/model-driven-incremental-hierarchical-compression-training-free-multi-generational-context-management-for-long-lived-coding-agents.md)** (English, v0.2)

> 📝 **The paper itself is open-sourced under the MIT License as part of the codebase (`paper/`). It is a living document — anyone may edit it; improvements are welcome via pull request.**

A production-scale longitudinal study: 4.5 months, three hosts, 174,327 model calls, 18.76B cumulative input tokens (~24.7B across all hosts), zero window violations on 204,800-token models, marathon sessions of 8,584–12,049 calls.

### 📊 Independent Third-Party Benchmarks

- **[1,500-Item Cross-Benchmark Evaluation (`LongMemEval-S` · `ContextBench` · `MemoryAgentBench`)](./benchmarks/third-party-1500/README.md)** ([中文版](./benchmarks/third-party-1500/README.zh-CN.md)) — head-to-head comparison of `billion-context` (`v0.1.202`) against `full` context and 3 RAG arms (`bm25`, `embedding`, `embedding-rerank`) with `DeepSeek V4.1 Flash`, `Qwen3-Embedding-8B`, `Qwen3-Reranker-4B`, and `Pi Agent`: **#1 on ContextBench** (`0.3097` Utilized F1, `-58.3%` cost vs `full`), **+16.6% over best RAG on LongMemEval-S** (`79.20%` vs `62.60%`, `-71.1%` independent-session cost vs `full`), and **100% survival on 1.48M-token MemoryAgentBench TTL** (`30×` steady-state compression where `full` fails `199/199`).

---

`billion-context` sits between **any** agent and its model API, rewriting Anthropic/OpenAI streams with [acp-kernel](https://github.com/ranxianglei/acp-kernel) compression. The model decides **when** and **what** to compress into high-fidelity summaries — not a hard truncation limit.

## Why

Long coding sessions blow up context. Each provider charges per token, and once you pass the context window the session degrades or dies. `billion-context` compresses consumed conversation into layered summaries so you can run a single se
