# 📈 股票智能分析系统

[ ](https://github.com/ZhuLinsen/daily_stock_analysis/stargazers)
[ ](https://arxiv.org/abs/2608.26990)
[ ](https://github.com/ZhuLinsen/daily_stock_analysis/actions/workflows/ci.yml)
[ ](https://opensource.org/licenses/MIT)
[ ](https://www.python.org/downloads/)
[ ](https://github.com/features/actions)
[ ](https://hub.docker.com/r/zhulinsen/daily_stock_analysis)

   &nbsp;   

> 🤖 基于 AI 大模型的 A股/港股/美股/日股/韩股/台股自选股智能分析系统，每日自动分析并推送「决策仪表盘」到企业微信/飞书/Telegram/Discord/Slack/邮箱

[**产品预览**](#-产品预览) · [**功能特性**](#-功能特性) · [**快速开始**](#-快速开始) · [**推送效果**](#-推送效果) · [**文档中心**](docs/INDEX.md) · [**完整指南**](docs/full-guide.md)

简体中文 | [English](docs/README_EN.md) | [繁體中文](docs/README_CHT.md)

  💖 赞助商 (Sponsors)  

       感谢  Modelflare  赞助本项目！由美国 Havenbyte LLC 运营，满血稳定不掺水，低成本接入 GPT、Claude、Gemini、Grok 及 40+ 图片/视频模型。指定 OpenAI 分组提供  65% / 75% / 85% 每日缓存命中率保障 ；单笔充值  US$20 解锁 GPT 0.015x ， US$50 解锁 Claude 0.03x 。 专属链接注册  

## 🖥️ 产品预览

## ✨ 功能特性

| 能力 | 覆盖内容 |
|------|------|
| AI 决策报告 | 核心结论、评分、趋势、买卖点位、风险警报、催化因素、操作检查清单 |
| 多市场数据聚合 | 覆盖 A股、港股、美股、日股、韩股、台股和 ETF，支持行情、K 线、技术指标、新闻、公告、基本面与报告辅助数据；不同市场的数据源和能力边界见 [市场支持边界](docs/market-support.md) |
| Web / 桌面工作台 | 手动分析、任务进度、历史报告、完整 Markdown、回测、持仓、配置管理、浅色 / 深色主题 |
| Agent 策略问股 | 多轮追问，支持均线、缠论、波浪、趋势、热点、事件、成长、预期等 15 种内置策略，覆盖 Web/Bot/API |
| 智能导入与补全 | 图片、CSV/Excel、剪贴板导入；股票代码/名称/拼音/别名补全 |
| 自动化与推送 | GitHub Actions、Docker、本地定时任务、FastAPI 服务和企业微信/飞书/Telegram/Discord/Slack/邮件推送 |

> 功能细节、字段契约、基本面 P0 超时语义、交易纪律、数据源优先级、Web/API 行为请看 [完整配置与部署指南](docs/full-guide.md)。

### 技术栈与数据来源

| 类型 | 支持 |
|------|------|
| AI 模型 | [Modelflare](https://modelflare.dev/sign-up?utm_source=github&utm_campaign=daily_stock_analysis)、[AIHubMix](https://inferera.com/?aff=CfMq)、Gemini、OpenAI 兼容、DeepSeek、通义千问、Claude、Ollama 本地模型等 |
| 行情数据 | AkShare、Tushare、Pytdx、Baostock、YFinance、Longbridge |
| 新闻搜索 | [Anspire](https://open.anspire.cn/dsa?share_code=QFBC0FYC)、[SerpAPI](https://serpapi.com/github-daily-stock-analysis)、[Tavily](https://tavily.com/)、[Bocha](https://open.bocha.cn/)、[Brave](https://brave.com/search/api/)、[MiniMax](https://platform.minimaxi.com/)、SearXNG |
| 社交舆情 | [Stock Sentiment API](https://api.adanos.org/docs)（Reddit / X / Polymarket，仅美股，可选） |

> 项目默认内置 AkShare、Baostock、YFinance 等免费行情源，可零配置运行；免费源受上游限流、接口变动和网络波动影响，稳定性不保证。长期定时、批量分析或更稳定行情建议配置 Tushare、Longbridge 等 token 型数据源，适用市场、Actions 映射和 fallback 规则见 [数据源配置](docs/full-guide.md#数据源配置)。

## 🚀 快速开始

### 方式一：[GitHub Actions（推荐）](https://www.bilibili.com/video/BV11FEb66EXG/)

> 5 分钟完成部署，零成本，无需服务器。

#### 1. Fork 本仓库

点击右上角 `Fork` 按钮（顺便点个 Star⭐ 支持一下）

#### 2. 配置 Secrets

`Settings` → `Secrets and variables` → `Actions` → `New repository secret`

**AI 模型配置（至少配置一个）**

默认先选一个模型服务商并填写 API Key；需要多模型、图片识别、本地模型或高级路由时，再参考 [LLM 配置指南](docs/LLM_CONFIG_GUIDE.md)。

| Secret 名称 | 说明 | 必填 |
|------------|------|:----:|
| `MODELFLARE_KEY` | [Modelflare](https://modelflare.dev/sign-up?utm_source=github&utm_campaign=daily_stock_analysis) API Key，低成本接入全球热门大模型 | **推荐** |
| `AIHUBMIX_KEY` | [AIHubMix](https://inferera
