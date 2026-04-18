---
name: video-selection
description: 在 YouTube 平台上围绕固定英文关键词和固定主题白名单，筛选值得进入学习沉淀与中文改写流程的英文 AI 视频，优先判断学习价值和实操落地价值，再结合互动代理指标和发文适配度做最终决策。
---

# Video Selection Skill

## 一、你的任务

你的任务不是找“最火的视频”，而是找：

**最值得学习、最值得实操、最值得沉淀成中文知识资产的英文 AI 视频。**

只有在满足学习价值和实操价值之后，才进一步判断它是否适合做中文发文内容。

## 二、输入

输入可以是：

- 英文 YouTube 视频链接
- 英文 YouTube 视频列表
- 英文频道名称
- 英文主题关键词
- 指定主题范围（agent / workflow / prompting / llm_advanced / tools / projects）

## 三、搜索与筛选边界

### 搜索要求
- 默认只面向英文 YouTube 内容
- 默认使用英文搜索词
- 默认围绕主题白名单搜索

### 参考文件
- `references/youtube_search_strategy.md`
- `references/learning_value_criteria.md`
- `references/video_selection_criteria.md`
- `assets/search_query_templates.md`

## 四、筛选顺序

你必须按以下顺序判断：

### 1. 主题是否匹配
这个视频是否属于以下主题之一：
- AI Agent
- Workflow / Automation
- Tool calling
- Multi-agent
- LangGraph / LangChain
- Prompt engineering
- Structured output
- LLM advanced usage
- AI 实战项目
- AI 工具（仅作补充）

### 2. 学习价值是否够高
这个视频是否：
- 有明确问题
- 有步骤或流程
- 有框架
- 有演示
- 可迁移到项目或 skill

### 3. 实操落地价值是否足够
这个视频是否：
- 可跟着做
- 有 build / tutorial / implementation / project / workflow 属性
- 能变成自己的练手方向

### 4. 互动验证是否足够
参考：
- views
- likes
- comments
- 点赞率
- 评论率
- 发布时间

### 5. 发文适配度
最后再判断：
- 是否适合写公众号
- 是否适合写小红书
- 是否适合只做学习笔记

## 五、入选原则

### 优先入选
- 英文内容
- 主题命中一级或二级优先范围
- 学习价值高
- 实操性强
- 有结构和方法
- 有案例或项目
- 有互动验证
- 可转成中文学习笔记和中文内容

### 次优先入选
- 学习价值较高，但发文价值一般
- 可保留为学习素材，不强求改写

### 可作为素材补充
- 工具盘点
- 趋势盘点
- 进阶技巧总结
- 更适合发文，但学习价值一般

## 六、直接淘汰条件

满足以下任一项，可以直接淘汰：

- 不是英文内容
- 不在主题白名单里
- 学习价值弱
- 纯热点评论
- 纯工具盘点且无方法
- 纯概念介绍且无步骤
- 严重依赖娱乐表达
- 无法形成中文学习沉淀或中文发文价值

## 七、推荐输出字段

你必须输出以下中文版信息：

- 视频标题
- 视频链接
- 频道名称
- 发布时间
- 视频时长
- views
- likes
- comments
- 主题判断
- learning_priority：S / A / B / C / D
- learning_reason
- practical_takeaways
- reusable_method
- publishing_fit：wechat / xiaohongshu / both / learning_only / reject
- 结论：入选 / 备选 / 淘汰
- 理由

## 八、平台判断规则

### 更适合公众号
- 结构完整
- 信息较多
- 逻辑清晰
- 适合解释和展开

### 更适合小红书
- 重点集中
- 观点明确
- 记忆点强
- 适合短节奏整理

### 更适合学习笔记
- 学习价值高
- 发文价值一般
- 更适合自己消化和迁移

## 九、执行提醒

你筛选的不是“热视频”，也不是“泛 AI 视频”。

你筛选的是：

**围绕固定英文学习主题，值得先学、值得再做、最后才值得转成中文内容的视频。**
