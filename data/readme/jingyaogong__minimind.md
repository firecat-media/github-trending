[ ](https://github.com/jingyaogong/minimind/stargazers)
[ ](LICENSE)
[ ](https://github.com/jingyaogong/minimind/commits/master)
[ ](https://github.com/jingyaogong/minimind/pulls)
[ ](https://huggingface.co/collections/jingyaogong/minimind-66caf8d999f5c7fa64f399e5)

   "大道至简" 

中文 | [English](./README_en.md)

* 此开源项目旨在完全从 0 开始，仅用 3 块钱成本与 2 小时训练时间，即可训练出规模约为 64M 的超小语言模型 MiniMind。
* MiniMind 系列极其轻量，主线最小版本体积约为 GPT-3 的 $\frac{1}{2700}$，力求让普通个人 GPU 也能快速完成训练与复现。
* 项目同时开源了大模型的极简结构与完整训练链路，覆盖 MoE、数据清洗、预训练（Pretrain）、监督微调（SFT）、LoRA、RLHF（DPO）、RLAIF（PPO / GRPO / CISPO）、Tool Use、Agentic RL、自适应思考与模型蒸馏等全过程代码。
* MiniMind 同时拓展了视觉模态模型 [MiniMind-V](https://github.com/jingyaogong/minimind-v)、多模态 Omni 模型 [MiniMind-O](https://github.com/jingyaogong/minimind-o)、扩散语言模型（MiniMind-dLM）、线性模型（MiniMind-Linear），详见 [Discussion](https://github.com/jingyaogong/minimind/discussions)。
* 项目所有核心算法代码均从 0 使用 PyTorch 原生实现，不依赖第三方库提供的高层抽象接口。
* 这不仅是一个大语言模型全阶段开源复现项目，也是一套面向 LLM 入门与实践的教程。
* 希望此项目能为更多人提供一个可复现、可理解、可扩展的起点，一起感受创造的乐趣，并推动更广泛 AI 社区的进步。

> 注：本项目基于 Apache 2.0 协议开源，完全免费。“2 小时” 指 SFT 阶段在单张 NVIDIA 3090 上跑完 `1 epoch` 的实测耗时，“3 块钱” 指对应时段的 GPU 租用成本。

---

[🔗 在线体验](https://www.modelscope.cn/studios/gongjy/MiniMind) | [🔗 视频介绍](https://www.bilibili.com/video/BV12dHPeqE72)

---

# 📌 项目介绍

大语言模型（Large Language Model, LLM）的出现，引发了全球范围内对 AI 的空前关注。无论是 ChatGPT、DeepSeek 还是 Qwen，都以惊艳的效果让人真切感受到这场技术浪潮的冲击力。然而，动辄数百亿参数的模型规模，使得它们对个人设备而言不仅难以训练，甚至连部署都显得遥不可及。打开大模型的“黑盒子”，真正去理解其内部运作机制，本应是一件令人心潮澎湃的事。遗憾的是，绝大多数探索最终都止步于使用 LoRA 等技术对现有大模型做少量微调，学习一些新指令或特定任务。这更像是在教牛顿如何使用 21 世纪的智能手机——虽然有趣，却偏离了理解物理本质的初衷。

与此同时，第三方的大模型框架与工具库，如 `transformers` / `trl` / `peft` 等，往往只暴露出高度抽象的接口。只需短短十几行代码，就可以完成“加载模型 + 加载数据集 + 推理 + 强化学习”的全流程训练。这种高效封装固然便利，却也在一定程度上把开发者与底层实现隔离开来，削弱了深入理解 LLM 核心代码的机会。我认为 “用乐高自己拼出一架飞机，远比坐在头等舱里飞行更让人兴奋”，然而更现实的问题是，互联网上充斥着大量付费课程和营销内容，用漏洞百出、一知半解的讲解包装所谓的 AI 教程。正因如此，本项目的初衷就是尽可能降低 LLM 的学习门槛，让每个人都能从理解每一行代码开始，从 0 开始亲手训练一个极小的语言模型。是的，从**零开始训练**，而不是仅仅停留在**推理**层面。最低只需不到 3 块钱的服务器成本，就能亲身体验从 0 到 1 构建一个语言模型的全过程。

😊 一起感受创造的乐趣吧！

---

#### 🎉 本项目包含以下内容

- 提供完整的 MiniMind-LLM 结构代码（Dense + MoE），当前主线结构对齐 `Qwen3 / Qwen3-MoE` 生态。
- 提供 Tokenizer 与分词器训练代码，支持 ` `、` `、` ` 等模板标记。
- 覆盖 Pretrain、SFT、LoRA、RLHF-DPO、RLAIF（PPO / GRPO / CISPO）、Tool Use、Agentic RL、自适应思考与模型蒸馏等完整训练流程。
- 提供全阶段开源数据，覆盖收集、蒸馏、清洗与去重后的高质量数据集。
- 关键训练算法与核心模块均从 0 实现，不依赖第三方框架封装。
- 兼容 `transformers`、`trl`、`peft` 等主流框架，以及 `llama.cpp`、`vllm`、`ollama` 等常用推理引擎与 `Llama-Factory` 等训练框架。
- 支持单机单卡与单机多卡（DDP、DeepSpeed）训练，支持 wandb / swanlab 可视化与动态启停训练。
- 支持在 C-Eval、C-MMLU、OpenBookQA 等第三方测评集上进行评测，并支持通过 YaRN 实现 RoPE 长文本外推。
- 提供兼容 OpenAI API 协议的极简服务端，便于接入 FastGPT、Open-WebUI 等第三方 Chat UI，并支持 `reasoning_content`、`tool_calls`、`open_thinking`。
- 提供基于 Streamlit 的极简聊天 WebUI，支持思考展示、工具选择与多轮 Tool Call。
- 包含实验性拓展：离散扩散语言模型（[dLM](https://github.com/jingyaogong/minimind/discussions/618)）与线性注意力模型（[Linear Attention](https://github.com/jingyaogong/minimind/discussions/704)），均可基于主线 AR 模型进行续训。

#### 🎉 已发布模型列表

| 模型 | 参数量 | Release |
|------|--------|---------|
| minimind-3 | 64M | 2026.04.01 |
| minimind-3-moe | 198M-A64M |
