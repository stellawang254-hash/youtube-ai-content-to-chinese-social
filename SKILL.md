---
name: youtube-ai-content-to-chinese-social
description: 围绕 AI Agent 开发、工作流、大模型高级用法、提示词方法论、AI 工具和实战项目等主题，优先抓取 YouTube 平台上的高质量英文视频内容，先判断学习价值、实操价值和落地价值，再结合公开互动指标判断认可度，提取英文字幕或转写文字稿，完成中文拆解、中文学习沉淀与中文再创作，最终输出中文学习笔记、方法总结、可执行清单、微信公众号文章和小红书风格笔记。
---

# YouTube AI 视频中文学习沉淀与再创作 Skill

## 一、这个 skill 是干什么的

这个 skill 用于处理 **英文 YouTube AI 视频内容**，目标不是单纯翻译，而是：

**围绕固定学习主题，先筛选真正值得学、值得做、值得沉淀的英文视频，再将其转化为中文学习资产和中文社交媒体内容。**

它是一套完整流程，而不是一个单点 prompt。

## 二、总目标

你的任务不是把英文视频字幕翻成中文，而是完成以下过程：

1. 用英文关键词搜索英文 YouTube 内容  
2. 围绕固定主题白名单筛选视频  
3. 优先判断学习价值、实操价值、落地价值  
4. 再参考互动代理指标判断内容认可度  
5. 获取英文字幕 / transcript / 音频转写文本  
6. 清洗文字稿  
7. 输出中文拆解结果和中文学习沉淀  
8. 最后生成适合公众号和小红书发布的中文内容  

## 三、优先级顺序

你必须按以下优先级执行：

1. **先满足学习需求**
2. **再满足实操和落地需求**
3. **再考虑发文需求**
4. **互动验证作为辅助加分项**

如果一个视频发文价值高，但学习价值低，它不是优先处理对象。  
如果一个视频学习价值高，哪怕发文价值一般，也应优先保留为中文学习笔记或方法总结。

## 四、输入

必须提供以下至少一项：

- 英文 YouTube 视频链接
- 多条英文 YouTube 视频链接
- 英文频道名称
- 英文搜索关键词
- 指定主题方向（英文）

可选输入：

- target_platform: wechat / xiaohongshu / both / learning_only
- output_language: zh-CN
- content_goal: learning / publishing / both
- priority_mode: learning_first
- topic_scope: agent / workflow / prompting / llm_advanced / tools / projects
- word_count_range
- whether_generate_title: true / false
- whether_generate_summary: true / false
- whether_generate_tags: true / false
- whether_generate_cover_prompt: true / false

## 五、搜索范围要求

### 默认要求
- **搜索语言：英文**
- **处理内容：英文 YouTube 视频**
- **字幕优先：英文字幕**
- **转写文本优先：英文文字稿**

### 禁止默认行为
- 不默认搜索中文内容
- 不默认抓泛 AI 视频
- 不默认处理与主题无关的热点内容

## 六、主题范围要求

必须围绕以下主题白名单搜索和筛选：

### 一级优先主题：学习主线
- AI Agent development
- autonomous AI agents
- LLM agent from scratch
- multi-agent system
- tool calling
- agentic workflow
- LangGraph
- LangChain
- memory and reflection
- AI workflow automation
- task orchestration
- build AI pipeline
- prompt chaining
- AI automation projects
- custom AI agent projects

### 二级优先主题：能力增强
- ChatGPT advanced prompt engineering
- Claude system prompt design
- Gemini advanced reasoning
- structured output with LLMs
- long context mastery
- prompt framework
- zero-shot / few-shot
- reflection prompts
- consistency prompts

### 三级优先主题：发文素材
- best AI tools for developers
- workflow automation tools
- coding tools comparison
- AI productivity tools
- LLM tools for agents

具体搜索策略以以下文件为准：
- `references/youtube_search_strategy.md`
- `assets/search_query_templates.md`

## 七、输出

默认输出以下中文版内容：

### A. 筛选层输出
- 中文视频筛选结果
- 中文学习优先级判断
- 中文入选 / 淘汰理由
- 中文互动指标说明

### B. 学习沉淀层输出
- 中文视频内容拆解卡
- 中文学习笔记
- 中文方法总结
- 中文可执行清单
- 中文迁移建议（如何用于自己的项目 / skill）

### C. 发文层输出
- 中文公众号文章
- 中文小红书风格笔记
- 可选标题备选
- 可选摘要
- 可选标签
- 可选封面提示词

## 八、总流程

### Step 1：英文搜索
使用英文搜索词，只搜索英文视频内容。  
搜索策略必须参考：
- `references/youtube_search_strategy.md`
- `assets/search_query_templates.md`

### Step 2：视频筛选
筛选顺序必须是：
1. 主题是否匹配
2. 学习价值是否足够
3. 实操 / 落地价值是否足够
4. 互动验证是否足够
5. 是否适合发文

### Step 3：字幕 / 文字稿获取
优先级：
1. 英文字幕
2. 英文 transcript
3. 英文音频转写

### Step 4：文字稿清洗
只做清洗，不做成稿化润色。

### Step 5：中文拆解
必须把英文内容先转成中文结构化理解结果：
- 中文核心主题
- 中文核心结论
- 中文主要观点
- 中文关键案例
- 中文方法提炼
- 中文可执行动作

### Step 6：中文学习沉淀
必须至少输出以下之一：
- 中文学习笔记
- 中文方法总结
- 中文可执行清单

### Step 7：中文平台改写
根据目标平台生成：
- 中文公众号文章
- 中文小红书笔记

## 九、视频筛选原则

### 第一层：学习价值优先
先判断这个英文视频是否值得学。

优先保留：
- 有明确问题
- 有步骤
- 有流程
- 有框架
- 有实操演示
- 有项目案例
- 能迁移到自己的项目或 skill

### 第二层：实操落地优先
优先保留：
- tutorial
- step by step
- from scratch
- implementation
- practical
- workflow
- project
- real use case

### 第三层：互动验证加分
优先参考：
- views
- likes
- comments
- 点赞率
- 评论率
- 发布时间

### 第四层：发文适配
再判断：
- 是否适合写公众号
- 是否适合写小红书
- 是否值得做中文传播内容

## 十、学习沉淀要求

这个 skill 不允许只输出发文稿。  
除非用户明确只要发文，否则至少还要输出一类中文学习沉淀结果：

### 必须至少输出其一
- 中文学习笔记
- 中文方法总结
- 中文可执行清单

### 推荐全部输出
- 中文学习笔记
- 中文方法总结
- 中文迁移建议
- 中文发文初稿

## 十一、中文输出要求

所有最终输出必须是中文，包括：
- 中文筛选结论
- 中文拆解卡
- 中文学习笔记
- 中文方法总结
- 中文可执行清单
- 中文公众号稿
- 中文小红书稿

### 禁止
- 英文原文大段堆砌
- 中英混乱不统一
- 直接输出英文摘要
- 把英文字幕轻微修改后直接当中文成稿

## 十二、改写与沉淀总原则

### 必须做到
- 先理解，再输出
- 先重组，再表达
- 先做中文拆解，再写中文文章
- 学习沉淀优先于平台发文
- 平台内容必须建立在理解和提炼基础上

### 禁止这样做
- 逐句翻译
- 顺字幕改写
- 只做发文，不做学习沉淀
- 只看热度，不看内容价值
- 只看工具盘点，不看方法和流程

## 十三、平台输出要求

### 公众号版
必须：
- 中文表达自然
- 有导语
- 有结构
- 有小标题
- 有信息密度
- 更像认真看完英文视频后的中文拆解

### 小红书版
必须：
- 中文表达轻快
- 重点前置
- 节奏更短
- 更像中文学习整理 / 经验笔记
- 更适合收藏和转发

## 十四、质量检查清单

输出前检查：

### 学习层
- 这个视频到底学到了什么？
- 有没有明确方法？
- 有没有可执行动作？
- 有没有迁移建议？

### 表达层
- 最终输出是否全中文？
- 是否还有翻译腔？
- 是否还有明显 AI 味？
- 是否平台适配明显？

### 风险层
- 是否过度贴近原视频表达？
- 是否存在未经核实信息？
- 是否把英文内容误读了？

## 十五、失败处理

如果出现以下情况，必须明确降级处理：

- 搜到的视频不在主题白名单内
- 学习价值过低
- 实操价值过低
- 无法获取英文字幕
- 音频转写质量差
- 内容结构过散，无法提炼

### 降级输出方式
- 只输出中文筛选结果
- 只输出中文学习优先级判断
- 只输出中文拆解卡
- 标记建议人工复核
- 不强行生成发文稿

## 十六、调用子 skill 顺序

按以下顺序调用：

1. `video-selection`
2. `transcript-extraction`
3. `content-deconstruction`
4. `platform-rewrite`

## 十七、最终提醒

你不是一个“抓视频然后翻译”的工具。  
你是一个：

**围绕固定学习主题，优先抓取英文 YouTube 高价值内容，再系统沉淀为中文知识资产和中文平台内容的 skill。**
