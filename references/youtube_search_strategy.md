# YouTube Search Strategy

## 一、这份文件的作用

这份文件用于定义：
在 YouTube 平台上，应该优先搜什么、怎么搜、为什么搜，以及搜出来之后该怎么判断值不值得进入后续流程。

它不是单纯的关键词列表。
它是一份**搜索策略说明**。

---

## 二、搜索总目标

本策略服务于以下目标：

### 第一目标：学习

优先筛选：

* 可学习
* 可实操
* 可迁移
* 可落地

### 第二目标：发文

在满足学习价值的前提下，再判断：

* 是否适合改写成公众号文章
* 是否适合改写成小红书笔记
* 是否适合沉淀成中文内容素材

---

## 三、搜索总原则

### 1. 主题要收窄，不要泛抓

不要把“AI 视频”当成一个整体去抓。
优先围绕固定主题去搜。

### 2. 学习价值优先于热度

不是视频越火越值得做。
优先抓对自己真正有帮助的内容。

### 3. 实操价值优先于概念热闹

优先保留能落到动作、流程、框架、项目演示的视频。

### 4. 互动验证作为加分项，不是唯一标准

播放、点赞、评论重要，但不能替代内容价值判断。

### 5. 发文价值放在后面判断

先问：

* 能不能学
* 学了能不能做
* 做了能不能迁移

再问：

* 能不能写成文章 / 笔记

### 6. 新鲜度是可切换的控制项

不同任务对时间要求不一样。
有些任务适合补经典内容，有些任务必须优先看最近 30 天。

所以搜索时必须支持按模式切换，而不是一套规则打天下。

---

## 四、新鲜度模式

## 1. classic

适合：

* 补基础
* 补方法
* 补框架
* 学经典工作流

特征：

* 不强制限制发布时间
* 允许抓到 2024、2025 或更早但仍然高价值的内容
* 排序时更看学习价值和实操价值

## 2. recent

适合：

* 跟最近 30 天动态
* 看 AI Agent 最近一个月的新趋势
* 关注工具、框架和最佳实践的新变化

特征：

* 优先搜索最近 `recency_window_days` 天内发布的视频
* 超过时间窗口内容默认降权
* 超过 90 天内容默认不进入主结果

## 3. hybrid

适合：

* 既想看最近内容
* 又不想错过经典高质量内容

特征：

* 先输出最近时间窗口内最值得学的视频
* 再单独补 1-2 条经典内容作为“经典补充”
* 不能把老视频混在主结果最前面

---

## 五、主题白名单

### 一级优先主题：学习主线

这些主题优先抓取。

#### 1. AI Agent 开发

* AI Agent development tutorial
* Building autonomous AI agents
* LLM agent from scratch
* Multi-agent system design
* AI agent tool calling tutorial
* Agentic workflow development
* LangGraph agent tutorial
* LangChain agent step by step
* AI agent with memory & reflection
* How to build a GPT-4o agent

#### 2. AI 工作流 / 自动化

* AI workflow automation tutorial
* LLM workflow design best practices
* Agentic workflow for business
* AI task orchestration
* Build AI pipeline for automation
* Prompt chaining for complex tasks
* AI workflow for content creation

#### 3. 实战项目

* Build AI agent to automate work
* AI workflow for content repurposing
* AI assistant for YouTube summarization
* Create custom AI agent with LangChain
* Automate tasks with AI agents

### 二级优先主题：能力增强

这些内容适合作为补充学习。

#### 4. ChatGPT / Claude / Gemini 高级用法

* ChatGPT advanced prompt engineering
* Claude 3 Opus system prompt design
* Gemini advanced reasoning techniques
* GPT-4o best practices for developers
* Claude long context window mastery
* Structured output with LLMs
* LLM prompt framework for consistency
* How to use ChatGPT for complex workflows

#### 5. 提示词方法论

* Prompt engineering for AI agents
* Advanced prompting techniques 2026
* Zero-shot / few-shot prompting mastery
* Chain of thought prompting guide
* Self-consistency & reflection prompts
* Professional system prompt templates

### 三级优先主题：内容素材

这些内容更适合做发文素材和趋势补充。

#### 6. AI 工具 / 效率工具

* Best AI tools for developers 2026
* Top AI workflow automation tools
* AI coding tools better than GitHub Copilot
* Must-have AI tools for productivity
* AI tools for research & summarization
* Best LLM tools for building agents

---

## 六、推荐搜索顺序

### 当 freshness_mode = classic

第一轮优先：

* AI Agent
* Workflow
* Automation
* LangGraph
* LangChain
* Tool calling
* Memory / reflection
* Task orchestration
* Build / tutorial / step by step / from scratch

第二轮补：

* Prompt engineering
* Structured output
* Long context
* Consistency framework
* System prompt design

第三轮补：

* AI tools
* Productivity tools
* Best AI tools
* Coding tools

### 当 freshness_mode = recent

第一轮优先：

* 主题词 + latest
* 主题词 + recent
* 主题词 + this month
* 主题词 + 2026
* 主题词 + current best practices

第二轮再补：

* tutorial
* step by step
* implementation
* practical
* workflow

第三轮再补：

* advanced tips
* tool updates
* new releases
* best practices

### 当 freshness_mode = hybrid

先按 `recent` 模式搜一轮，
再按 `classic` 模式补一轮，
最后把结果分成：

* 最近时间窗口内最值得学的内容
* 经典补充内容

---

## 七、搜索词使用逻辑

### A. 想优先学习“怎么做”

优先搜索：

* tutorial
* step by step
* from scratch
* build
* implementation
* system design

### B. 想优先学习“怎么落地”

优先搜索：

* workflow
* automation
* orchestration
* business
* pipeline
* practical
* real use case

### C. 想优先补“方法论”

优先搜索：

* best practices
* framework
* prompting
* consistency
* reasoning
* reflection

### D. 想优先补“发文素材”

优先搜索：

* advanced tips
* best tools
* 2026
* comparison
* roundup

### E. 想优先抓最近一个月内容

优先搜索：

* latest
* recent
* this month
* current
* 2026
* new update
* current best practices

---

## 八、近 30 天优先的推荐搜索词

以下搜索词特别适合 `freshness_mode = recent`：

* AI agent latest
* AI agent recent tutorial
* AI agent this month
* AI workflow 2026
* agentic workflow latest
* LangGraph recent tutorial
* LangGraph 2026
* structured output latest best practices
* Claude latest prompt engineering
* Gemini recent reasoning techniques
* current AI agent best practices
* latest AI automation workflow

---

## 九、搜索结果筛选顺序

每次搜完，不要直接处理全部结果。
按以下顺序筛选：

### 当 freshness_mode = classic

1. 主题是否匹配
2. 学习价值是否够高
3. 实操价值是否足够
4. 互动验证是否足够
5. 是否适合发文
6. 时间新鲜度作为补充参考

### 当 freshness_mode = recent

1. 主题是否匹配
2. 是否在最近 `recency_window_days` 天内
3. 学习价值是否够高
4. 实操价值是否足够
5. 互动验证是否足够
6. 是否适合发文

### 当 freshness_mode = hybrid

1. 先筛出最近 `recency_window_days` 天内内容
2. 在这些内容里按学习价值和实操价值排序
3. 再从时间窗口外补 1-2 条经典内容
4. 经典内容必须单列，不可混排在主结果前面

---

## 十、推荐组合搜法

### classic 模式

* AI agent + workflow + tutorial
* Build AI agent + LangGraph + step by step
* LLM + prompt engineering + best practices

### recent 模式

* AI agent + latest
* AI workflow + 2026
* LangGraph + recent tutorial
* structured output + current best practices
* agentic workflow + this month

### hybrid 模式

* recent 结果 + classic 补充
* latest + tutorial
* recent + best practices
* 2026 + implementation
* current + framework

---

## 十一、降权处理的内容

以下内容可以搜索到，但优先级应降低：

* 泛 AI 新闻
* 纯热点评论
* 情绪型观点视频
* 没有实操的工具盘点
* 纯概念讲解
* 只展示结果，不讲过程的视频
* 标题很强但内容空的视频

在 `recent` 模式下，还应额外降权：

* 发布时间明显超出时间窗口的内容
* 标题里没有任何当前性信号的旧内容
* 明显讲旧版本工具或旧版本框架的视频

---

## 十二、推荐输出格式

### 当 freshness_mode = classic

输出：

* 推荐优先学习的视频
* 推荐优先改写的视频
* 备选内容

### 当 freshness_mode = recent

输出：

#### 最近 `recency_window_days` 天最值得学的内容

* 标题
* 日期
* 为什么值得学

#### 经典补充（可选）

* 标题
* 日期
* 为什么虽然旧但仍值得补

### 当 freshness_mode = hybrid

输出：

#### A. 最近时间窗口内最值得学的内容

#### B. 经典补充内容

---

## 十三、最终提醒

这套搜索策略的重点，不是“抓更多视频”，而是：

* 抓得更准
* 抓得更值
* 抓到真正能学的内容
* 在 recent 模式下，优先抓到最近时间窗口内真正值得学的内容
* 再从里面挑适合发出来的内容
