# YouTube AI Content to Chinese Social

一个面向 **英文 YouTube AI 视频内容** 的学习驱动型内容处理 skill。

它的核心目标不是泛抓 AI 视频，更不是机械翻译字幕，而是：

**围绕 AI Agent、工作流、大模型高级用法、提示词方法论、AI 工具和实战项目等固定主题，优先筛选具备学习价值、实操价值和落地价值的英文视频内容，再沉淀成中文学习笔记、方法总结、公众号文章和小红书笔记。**

---

## 这个仓库适合谁

适合以下几类人：

- 想系统学习海外 AI 干货内容的人
- 想围绕 Agent、Workflow、Prompt、LLM 高级用法持续补课的人
- 想把 YouTube 高质量英文视频沉淀成中文内容资产的人
- 想给 Codex、Trae、Hermes、OpenClaw 等 agent 修炼内容处理能力的人
- 想建立“学习 + 发文”一体化内容流水线的人

---

## 这个仓库不做什么

这套 skill 不做以下事情：

- 不泛抓所有 AI 视频
- 不优先处理中文视频
- 不以“热点最大”为唯一标准
- 不把字幕直接翻译成文章
- 不追求粗糙洗稿
- 不把公众号和小红书写成一个版本

---

## 核心定位

这是一个：

**英文 YouTube AI 视频筛选 → 学习沉淀 → 中文平台再创作** 的 skill 系统。

它的优先级顺序非常明确：

1. 先满足学习需求
2. 再满足实操和落地需求
3. 最后满足发文需求

---

## 核心原则

### 1. 抓取英文内容
默认搜索、筛选和处理对象为：
- 英文 YouTube 视频
- 英文标题
- 英文字幕 / transcript / 音频转写文本

### 2. 输出中文内容
所有最终输出必须是中文版，包括：
- 中文学习笔记
- 中文方法总结
- 中文可执行清单
- 中文公众号文章
- 中文小红书笔记

### 3. 学习价值优先
先看：
- 能不能学到方法
- 能不能学到流程
- 能不能学到结构
- 能不能迁移到自己的项目和 skill 里

### 4. 实操落地优先
优先抓：
- tutorial
- step by step
- from scratch
- workflow
- implementation
- best practices
- build
- project
- real use case

### 5. 互动验证加分
结合公开代理指标：
- views
- likes
- comments
- 点赞率
- 评论率
- 发布时间

### 6. 发文适配放在后面
满足学习和实操价值后，再判断：
- 是否适合公众号
- 是否适合小红书
- 是否值得做内容再创作

---

## 核心主题范围

### 一级优先：学习主线
- AI Agent 开发
- Agentic workflow
- AI 工作流 / 自动化
- Tool calling
- Multi-agent system
- LangGraph
- LangChain
- Task orchestration
- Memory / reflection
- 实战项目搭建

### 二级优先：能力增强
- ChatGPT / Claude / Gemini 高级用法
- Structured output
- System prompt design
- Prompt engineering
- Long context
- Consistency / reflection

### 三级优先：发文素材
- AI 工具盘点
- AI 效率工具
- AI coding tools
- 趋势型工具推荐内容

---

## 工作流总览

### Step 1：英文搜索
基于：
- `references/youtube_search_strategy.md`
- `assets/search_query_templates.md`

优先使用英文关键词搜索英文内容。

### Step 2：视频筛选
基于：
- `references/learning_value_criteria.md`
- `references/video_selection_criteria.md`

按以下顺序判断：
1. 主题是否匹配
2. 学习价值是否够高
3. 实操价值是否足够
4. 是否有互动验证
5. 是否适合发文

### Step 3：字幕 / 转写获取
优先顺序：
1. 英文字幕
2. 英文 transcript
3. 英文音频转写

### Step 4：清洗文字稿
- 删除重复
- 删除口头禅
- 修复错词
- 统一术语
- 按主题切段

### Step 5：内容拆解
生成：
- 中文视频拆解卡
- 中文学习笔记
- 中文方法总结
- 中文可执行清单

### Step 6：平台改写
输出：
- 中文公众号文章
- 中文小红书笔记

---

## 这套 skill 的最终输出

默认输出包括：

### A. 学习沉淀层
- 中文视频筛选结果
- 中文学习优先级判断
- 中文视频内容拆解卡
- 中文方法总结
- 中文可执行清单

### B. 发文层
- 中文公众号文章
- 中文小红书风格笔记
- 可选标题 / 摘要 / 标签 / 封面提示词

---

## 仓库结构

- `README.md`：项目总说明
- `SKILL.md`：主 skill 文件

### `assets/`
- 写作规则
- 搜索模板
- 平台模板
- 禁用表达

### `references/`
- 英文搜索策略
- 学习价值判断标准
- 视频筛选标准
- 工作流说明

### `scripts/`
- 脚本说明文件
- 定义每个执行环节的输入输出和边界

### `skills/`
- 视频筛选
- 字幕提取
- 内容拆解
- 平台改写

### `examples/`
- 端到端样例
- 公众号样例
- 小红书样例

---

## 最终提醒

这套 skill 的目标，不是“抓视频然后写文章”。

它真正的目标是：

**围绕固定学习主题，抓到真正值得学、值得做、值得沉淀的英文 YouTube 内容，再系统地转化为中文知识资产和中文平台内容。**
