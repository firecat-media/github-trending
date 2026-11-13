# Claude Trading Skills

Claude Trading Skills started as a personal project to use AI to improve my own trading process.

Claude Trading Skills is a Claude Skills-based trading workflow toolkit for time-constrained individual investors.

It is designed for investors who use long-term investing, ETFs, and dividend stocks as their core, while using disciplined swing trading as a satellite strategy when market conditions are favorable.

The goal is not to outsource buy/sell decisions to AI. The goal is to structure market review, risk management, trade planning, journaling, and continuous improvement. It is open source because the workflows, checklists, and review habits behind better trading decisions can improve through shared practice.

This is not a signal service or a promise of profitability. It is a toolkit for traders who want to build a better decision process.

The project follows a **first for self, open for others** stance: it is built first as a practical workflow the author uses, then shared openly for others who face similar constraints.

📖 **Documentation site:**  

**Project vision:** [`PROJECT_VISION.md`](PROJECT_VISION.md)

日本語版READMEは[`README.ja.md`](README.ja.md)をご覧ください。

## Disclaimer

This repository is for educational, research, and process-improvement purposes only. It is not financial advice, investment advisory service, tax advice, legal advice, a signal service, or a broker execution platform. Trading and investing involve risk, including loss of principal. Past performance, backtests, screens, reports, and AI-generated analysis do not guarantee future results. All trading decisions, position sizing, tax/regulatory compliance, and broker usage are the user's responsibility.

The project is provided under the MIT License, **AS IS, WITHOUT WARRANTY**.

## Who This Is For

This repository is designed for:

- Time-constrained individual investors
- Long-term investors who also want disciplined swing-trading upside
- Dividend and ETF investors who want structured portfolio review
- Traders who want to manage risk before finding trade candidates
- Investors who want to journal and improve their decision process

It is not designed for fully automated trading, signal outsourcing, or short-term scalping.

## Recommended Starting Path

New users should start with one of these operational workflows. Each link points to a machine-readable manifest under [`workflows/`](workflows/) that names the exact skills, decision gates, and artifacts in order.

| Goal | Workflow | Anchor Skills | API Profile |
| --- | --- | --- | --- |
| 15-minute daily market check | [`market-regime-daily`](workflows/market-regime-daily.yaml) | market-breadth-analyzer, uptrend-analyzer, exposure-coach | No API for basic path |
| Weekly long-term portfolio review | [`core-portfolio-weekly`](workflows/core-portfolio-weekly.yaml) ([sample](examples/workflows/core-portfolio-weekly/sample-run/)) | portfolio-manager, kanchi-dividend-review-monitor, trader-memory-cor
