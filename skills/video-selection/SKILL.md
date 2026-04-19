---

name: video-selection
description: 在 YouTube 平台上围绕固定英文关键词和固定主题白名单，筛选值得进入学习沉淀与中文改写流程的英文 AI 视频，支持 classic、recent、hybrid 三种新鲜度模式，优先判断时间要求、学习价值和实操落地价值，再结合互动代理指标和发文适配度做最终决策。
--------------------------------------------------------------------------------------------------------------------------------------------------

# Video Selection Skill

## 一、你的任务

你的任务不是找“最火的视频”，而是找：

**最值得学习、最值得实操、最值得沉淀成中文知识资产的英文 AI 视频。**

同时，这个 skill 必须支持三种不同的新鲜度模式：

* `classic`
* `recent`
* `hybrid`

也就是说，你不能永远用同一套排序逻辑。

---

## 二、输入

输入可以是：

* 英文 YouTube 视频链接
* 英文 YouTube 视频列表
* 英文频道名称
* 英文主题关键词
* 指定主题范围（agent / workflow / prompting / llm_advanced / tools / projects）

可选输入还包括：

* `freshness_mode`: classic / recent / hybrid
* `recency_window_days`: 30

默认行为：

* `freshness_mode = hybrid`
* `recency_window_days = 30`

---

## 三、搜索与筛选边界

### 搜索要求

* 默认只面向英文 YouTube 内容
* 默认使用英文搜索词
* 默认围绕主题白名单搜索

### 参考文件

* `references/youtube_search_strategy.md`
* `references/learning_value_criteria.md`
* `references/video_selection_criteria.md`
* `assets/search_query_templates.md`

---

## 四、新鲜度模式说明

## 1. classic

适合：

* 补基础
* 补方法
* 学经典结构
* 学稳定 workflow

在这个模式下：

* 不强制限制发布时间
* 优先看学习价值和实操价值
* 老视频只要仍然有价值，就可以排到前面

## 2. recent

适合：

* 跟最近 30 天动态
* 看 AI Agent 最近变化
* 关注最近一个月的工具、框架和最佳实践

在这个模式下：

* 优先最近 `recency_window_days` 天内发布的视频
* 超过时间窗口的视频默认降权
* 超过 90 天的视频默认不应进入主结果前列

## 3. hybrid

适合：

* 既想看最近内容
* 又不想错过经典高质量内容

在这个模式下：

* 先输出最近时间窗口内最值得学的内容
* 再补少量经典内容
* 经典内容必须单独标记为“经典补充”
* 不能和 recent 主结果混排

---

## 五、筛选顺序

你必须按 `freshness_mode` 切换筛选顺序。

### 当 freshness_mode = classic

筛选顺序：

1. 主题是否匹配
2. 学习价值是否够高
3. 实操落地价值是否足够
4. 可迁移性是否够强
5. 互动验证是否足够
6. 发文适配度
7. 时间新鲜度作为补充参考

### 当 freshness_mode = recent

筛选顺序：

1. 主题是否匹配
2. 是否在最近 `recency_window_days` 天内
3. 学习价值是否够高
4. 实操落地价值是否足够
5. 可迁移性是否够强
6. 互动验证是否足够
7. 发文适配度

### 当 freshness_mode = hybrid

筛选顺序：

#### 第一阶段

先筛出最近 `recency_window_days` 天内的候选视频

#### 第二阶段

在 recent 候选里按：

* 学习价值
* 实操价值
* 可迁移性
* 互动
  排序

#### 第三阶段

再从时间窗口外补少量经典高质量视频

#### 第四阶段

把结果分成两组：

* 最近时间窗口内最值得学的内容
* 经典补充内容

---

## 六、主题判断规则

这个视频是否属于以下主题之一：

* AI Agent
* Workflow / Automation
* Tool calling
* Multi-agent
* LangGraph / LangChain
* Prompt engineering
* Structured output
* LLM advanced usage
* AI 实战项目
* AI 工具（仅作补充）

如果主题不匹配，默认不进入高优先级结果。

---

## 七、学习价值判断规则

这个视频是否：

* 有明确问题
* 有步骤或流程
* 有框架
* 有演示
* 可迁移到项目或 skill

优先保留：

* 能学到方法
* 能学到结构
* 能学到流程
* 能迁移到自己的项目中

---

## 八、实操和落地判断规则

这个视频是否：

* 可跟着做
* 有 build / tutorial / implementation / project / workflow 属性
* 能变成自己的练手方向
* 能沉淀成 skill / workflow / 模板

---

## 九、互动验证规则

参考：

* views
* likes
* comments
* 点赞率
* 评论率
* 发布时间

互动验证是加分项，不是唯一标准。
不能因为热视频就跳过学习价值判断。

---

## 十、新鲜度判断规则

这是这个 skill 必须新增的判断层。

### 当 freshness_mode = classic

* 记录发布时间
* 识别内容是否可能过时
* 不把新鲜度作为硬门槛

### 当 freshness_mode = recent

必须重点判断：

* 是否在最近 `recency_window_days` 天内
* 是否明显属于当前一轮的更新内容
* 是否讲的是较新的模型 / 框架 / 版本 / best practices

### 当 freshness_mode = hybrid

必须显式标记：

* `within_recency_window = true / false`
* `is_classic_supplement = true / false`

recent 主结果里，不要混入过老视频。

---

## 十一、入选原则

### 优先入选

* 英文内容
* 主题命中一级或二级优先范围
* 学习价值高
* 实操性强
* 有结构和方法
* 有案例或项目
* 有互动验证
* 在 recent / hybrid 模式下满足时间窗口要求
* 可转成中文学习笔记和中文内容

### 次优先入选

* 学习价值较高，但发文价值一般
* 可保留为学习素材，不强求改写

### 经典补充内容

只在 `hybrid` 模式下使用：

* 超出时间窗口
* 但学习价值很高
* 结构和方法仍不过时
* 值得作为背景补充或经典参考

---

## 十二、直接淘汰条件

满足以下任一项，可以直接淘汰：

* 不是英文内容
* 不在主题白名单里
* 学习价值弱
* 纯热点评论
* 纯工具盘点且无方法
* 纯概念介绍且无步骤
* 严重依赖娱乐表达
* 无法形成中文学习沉淀或中文发文价值

在 `recent` 模式下，以下也应直接淘汰或明显降权：

* 明显超过时间窗口且无强补充价值
* 明显讲旧版本工具 / 旧版本框架 / 旧方法
* 旧内容却没有“仍然可用”的理由

---

## 十三、推荐输出字段

你必须输出以下中文版信息：

* 视频标题
* 视频链接
* 频道名称
* 发布时间
* 视频时长
* views
* likes
* comments
* 主题判断
* `learning_priority`：S / A / B / C / D
* `learning_reason`
* `practical_takeaways`
* `reusable_method`
* `publishing_fit`：wechat / xiaohongshu / both / learning_only / reject
* `freshness_mode`
* `recency_window_days`
* `within_recency_window`
* `is_classic_supplement`
* `freshness_note`
* 结论：入选 / 备选 / 淘汰
* 理由

---

## 十四、平台判断规则

### 更适合公众号

* 结构完整
* 信息较多
* 逻辑清晰
* 适合解释和展开

### 更适合小红书

* 重点集中
* 观点明确
* 记忆点强
* 适合短节奏整理

### 更适合学习笔记

* 学习价值高
* 发文价值一般
* 更适合自己消化和迁移

---

## 十五、推荐输出格式

### 当 freshness_mode = classic

输出：

* 入选视频
* 备选视频
* 淘汰视频
* 理由

### 当 freshness_mode = recent

输出：

#### 最近 `recency_window_days` 天最值得学的内容

* 视频信息
* learning_priority
* 为什么值得学
* 为什么适合 / 不适合发文

#### 经典补充（可选）

* 标题
* 日期
* 为什么虽然旧但仍有参考价值

### 当 freshness_mode = hybrid

输出：

#### A. 最近时间窗口内最值得学的内容

#### B. 经典补充内容

---

## 十六、执行提醒

你筛选的不是“热视频”，也不是“泛 AI 视频”。

你筛选的是：

**围绕固定英文学习主题，按照 classic / recent / hybrid 不同模式，找到真正值得先学、值得再做、最后才值得转成中文内容的视频。**
