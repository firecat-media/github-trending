# AutoClip

### 一个链接，一键出片

开源，在你的电脑上剪辑与渲染。贴一个链接，选好平台，生成  视频、封面和发布文案 ， 
适配抖音、小红书、TikTok、Reels、YouTube Shorts、B 站与 YouTube。 
软件免费，云端模型按量计费；需要调整时可进入编辑器。

**[官网](https://zhouxiaoka.github.io/autoclip_intro/)** · **[下载桌面版](https://github.com/zhouxiaoka/autoclip/releases/latest)** · [案例库](https://zhouxiaoka.github.io/autoclip_intro/cases/) · [研究](docs/research/2026-10-what-drives-views/article-zh.md) · [快速开始](#快速开始) · [文档](#文档) · [问题反馈](https://github.com/zhouxiaoka/autoclip/issues/new/choose)

**简体中文** · [English](README-EN.md) · [日本語](README-JA.md) · [한국어](README-KO.md) · [Español](README-ES.md) · [Português](README-PT.md) · [Русский](README-RU.md) · [Français](README-FR.md)

**[最新正式版](https://github.com/zhouxiaoka/autoclip/releases/latest)**，桌面、CLI 与 MCP 同步更新。版本以 `autoclip --version` 和 MCP `get_version` 为准。一键出片、字幕分页、人物取景与长视频队列修复见 [更新日志](CHANGELOG.md)。旧版用户请升级。

## 真实成片

点击截图或「播放」直接观看完整成片；下方语言指成片字幕语言。这里精选 6 条，展开可看另外 10 条。

### 竖版 · 访谈式与满屏播客式

 Bill Gates  
访谈式 · 抖音 · 中文 
 ▶ 播放 1:01  ·  原片 

 AI Experts Debate  
访谈式 · Shorts · 英文 
 ▶ 播放 1:25  ·  原片 

 Tony Robbins  
满屏播客 · 抖音 · 中文 
 ▶ 播放 1:45  ·  原片 

 Andrew Garfield × Amy Poehler  
满屏播客 · Shorts · 英文 
 ▶ 播放 1:01  ·  原片 

### 横版 · 保留原画幅

 佟丽娅 × 鲁豫  
原画幅 · B 站 · 中文 
 ▶ 播放 1:41  ·  原片 

 Sam Altman  
原画幅 · B 站 · 中文 
 ▶ 播放 2:02  ·  原片 

 查看更多 10 条真实成片 

 Adam Neumann  
满屏播客 · TikTok · 英文 
 ▶ 播放 0:59  ·  原片 

 小奇 × 鲁豫  
访谈式 · 抖音 · 中文 
 ▶ 播放 0:50  ·  原片 

 郭柯宇 × 鲁豫  
访谈式 · 抖音 · 中文 
 ▶ 播放 1:11  ·  原片 

 Willem Dafoe  
满屏播客 · TikTok · 英文 
 ▶ 播放 1:07  ·  原片 

 TIM × 罗永浩  
访谈式 · 抖音 · 中文 
 ▶ 播放 1:05  ·  原片 

 Jensen Huang  
访谈式 · 小红书 · 中文 
 ▶ 播放 1:17  ·  原片 

 Andrej Karpathy  
访谈式 · 抖音 · 中文 
 ▶ 播放 0:43  ·  原片 

 A20 Pro  
访谈式 · 小红书 · 中文 
 ▶ 播放 2:00  ·  原片 

 Sylvester Stallone  
访谈式 · 抖音 · 中文 
 ▶ 播放 1:39  ·  原片 

 MrBeast  
满屏播客 · TikTok · 英文 
 ▶ 播放 1:42  ·  原片 

视频、封面与发布文案见 **[官网案例库 →](https://zhouxiaoka.github.io/autoclip_intro/cases/)**，欢迎[投稿你的成片](https://github.com/zhouxiaoka/autoclip/discussions/new?category=show-and-tell)。原片版权归原作者，仅作效果展示。

## 能做什么

### 贴链接就出片

选好平台，按平台的画幅与时长要求自动生成。每个平台按评分自动生成至多 10 条合格片段，其余列为备选，点「生成这条」再制作。每条都带封面、标题、简介、话题和 ZIP 发布包。

### 成片自己会包装

抖音 / 小红书默认访谈式，TikTok / Reels / Shorts 默认满屏播客式；竖版也可自行选择两种版式。字幕和文案语言仍按平台，B 站 / YouTube 为横版。画面跟随说话人，无人镜头保留完整画面。自动品牌片尾默认开启，可在设置中关闭；复制发布文案不附 AutoClip 署名。

### 还在你的电脑上

剪辑、取景与渲染在本机完成。分析模型自选，字幕可用作者字幕、本地 Whisper / SenseVoice 或已配置的云端转写。CLI / MCP 与桌面共用同一条一键出片链路。

## 真实素材的耗时与费用

以下是开发期间三条不同素材的实测，不是同一输入的速度对照。费用按当时 qwen-plus 的文字模型用量估算，不含云端语音识别、AI 生图或投稿服务费用；实际账单以所选服务商为准。

| 版本 | 原片 | 出片 | 文字模型费用估算（人民币） |
| --- | --- | ---: | ---: |
| **新版 · 有字幕** | Jensen · 1h43m（英 → 小红书） | **7.5 分钟 / 10 条** | **¥0.09** |
| 新版 · 无字幕 | TIM × 罗永浩 · 2h52m（中 → 抖音） | 29.5 分钟 / 10 条 | ¥0.20 |
| 旧版 | MrBeast · 2h06m（英 → TikTok） | 65 分钟 | ¥0.64 |

 测试条件与记录 

2026-10-01，同一台 Apple Silicon Mac。前两条为新链路、自动生成 10 条；旧链路生成 33 条，素材与输出数量不同。Jensen 使用作者字幕，TIM 使用本地 Whisper base。

已有作者字幕时跳过转写；没有字幕时可选本地或云端转写。追加平台和制作备选会增加处理时间与用量。完整阶段记录与估算口径见 [成本与时间](docs/COST_PER_VIDEO.md)。

## 模型与数据由你选择

剪辑和渲染在你的电脑上完成。
