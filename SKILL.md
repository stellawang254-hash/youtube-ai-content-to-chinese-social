---
name: youtube-ai-content-to-chinese-social
description: >
  从英文 YouTube AI 视频到中文学习笔记和社交内容，一次完成找→看→懂→用→发。
  聚焦 AI Agent / 工作流 / 大模型主题，自动筛选高价值视频，输出中文拆解笔记、
  微信公众号文章和小红书笔记。不是翻译工具，是视频转中文知识资产的 7 步流程。
aliases:
  - youtube-ai-content
  - youtube-chinese
  - youtube-视频转中文
  - youtube技能
  - 视频转中文skill
  - 油管转中文
  - 视频学习笔记
platforms: [linux, macos, windows]
metadata:
  hermes:
    related_skills: [youtube-content]
---

# YouTube AI 视频 → 中文学习沉淀 → 社交内容

> ⚡ 英文 YouTube AI 视频 → 中文学习笔记 → 公众号/小红书
> 聚焦 AI Agent / 工作流 / 大模型，不是翻译，是深度拆解。

```ascii
┌────────────┐   ┌──────────┐   ┌─────────┐   ┌──────────────┐
│ YouTube    │ → │ 字幕提取 │ → │ 中文拆解│ → │ 学习笔记     │
│ 英文AI视频 │   │ 清洗     │   │ 方法提炼│   │ 公众号稿     │
│            │   │          │   │ 可执行  │   │ 小红书笔记   │
└────────────┘   └──────────┘   └─────────┘   └──────────────┘
```

## 为什么值得装？

**问题**：你找英文 YouTube 上的 AI 教程 → 打开看 → 记笔记 → 想发中文平台
→ 每次都要 4 步，而且搜到的视频质量参差不齐。

**这个 Skill 做的**：一次把"找→看→懂→用→发"全跑完。它有自己的主题白名单（只挑 AI Agent/工作流/大模型的高价值视频），先筛再深挖，不是翻译工具。

**和直接问 Agent 有什么区别**？
- Agent 临时做 = 没有白名单、没有学习优先级、输出格式看心情
- 这个 Skill = **可复现的 7 步工作流**，每次输出格式一致

---

## 完整 7 步流程

> 以下 7 步是完整流程。日常使用不一定要全跑——可以只跑到"筛选结果"停，也可以直接跳到"处理一条已有 URL"。

### 必填（至少一项）
- 英文 YouTube 视频链接（单条或多条）
- 英文频道名称
- 英文搜索关键词
- 指定主题方向（英文）

### 可选参数
| 参数 | 说明 | 默认值 |
|---|---|---|
| `target_platform` | wechat / xiaohongshu / both / learning_only | learning_only |
| `content_goal` | learning / publishing / both | both |
| `freshness_mode` | classic / recent / hybrid | hybrid |
| `recency_window_days` | 新鲜度时间窗口（天） | 30 |
| `topic_scope` | agent / workflow / prompting / llm_advanced / tools / projects | agent |
| `word_count_range` | 字数范围 | 不限 |
| `generate_title` | 是否生成标题 | true |
| `generate_summary` | 是否生成摘要 | true |
| `generate_tags` | 是否生成标签 | true |
| `generate_cover_prompt` | 是否生成封面提示词 | false |

---

## 四、优先级顺序

你必须按以下优先级执行：

1. **先满足 freshness_mode 对应的新鲜度要求**
2. **再满足学习需求**
3. **再满足实操和落地需求**
4. **再考虑发文需求**
5. **互动验证作为辅助加分项**

如果一个视频发文价值高，但学习价值低，它不是优先处理对象。
如果一个视频学习价值高，哪怕发文价值一般，也应优先保留为中文学习笔记或方法总结。

### 新鲜度模式说明

#### classic
适合补基础、补方法、学经典结构。
优先级：学习价值 > 实操落地 > 发文适配 > 互动验证 > 时间新鲜度

#### recent
适合跟最近动态、看最新 AI Agent 变化。
优先级：时间新鲜度 > 学习价值 > 实操落地 > 发文适配 > 互动验证

#### hybrid
先返回最近时间窗口内最值得学的视频，再补充少量经典高质量内容，单独标记为"经典补充"。

---

## 五、主题白名单

> 详见 `references/topic-whitelist.md` — 一级（学习主线）/ 二级（能力增强）/ 三级（发文素材）+ 扩展场景。

### 快速参考

| 级别 | 含义 | 示例 |
|------|------|------|
| 一级 | 学习主线 | AI Agent, tool calling, agentic workflow, LangGraph |
| 二级 | 能力增强 | prompt engineering, structured output, long context |
| 三级 | 发文素材 | best AI tools, workflow automation, coding tools comparison |

---

## 六、完整 7 步流程

### Step 1: 英文搜索

使用英文搜索词，只搜索英文视频内容。
搜索策略可参考 `youtube-search-strategy` skill 中的搜索模板。

当 `freshness_mode = recent` 时，搜索词需包含 `latest`、`recent`、`this month`、`2026` 等时间限定词。

### Step 2: 视频筛选

#### 当 freshness_mode = classic
1. 主题是否匹配
2. 学习价值是否足够
3. 实操/落地价值是否足够
4. 互动验证是否足够
5. 时间新鲜度
6. 是否适合发文

#### 当 freshness_mode = recent
1. 主题是否匹配
2. 是否在最近 `recency_window_days` 天内
3. 学习价值是否足够
4. 实操/落地价值是否足够
5. 互动验证是否足够
6. 是否适合发文

#### 当 freshness_mode = hybrid
1. 先选出最近 `recency_window_days` 天内最值得学的视频
2. 再补少量经典高质量内容
3. 经典内容必须单独标记为"经典补充"

### Step 3: 字幕 / 文字稿获取

使用 `youtube-content` skill 获取字幕。

优先级：
1. 英文字幕（手动字幕优先）
2. 英文 transcript
3. 英文音频转写

#### 方法 A: 使用内置脚本（推荐）
```bash
pip3 install youtube-transcript-api
python3 /path/to/youtube-content/scripts/fetch_transcript.py "URL" --text-only --timestamps
```

#### 方法 B: 通过 Python 代码（youtube-transcript-api ≥ 1.2.x）
新版 API 不再是静态方法，需先实例化：
```python
from youtube_transcript_api import YouTubeTranscriptApi
api = YouTubeTranscriptApi()
result = api.fetch("VIDEO_ID", languages=["en"])
text = " ".join([s.text for s in result.snippets])
```

旧版兼容写法（`YouTubeTranscriptApi.get_transcript()`）在新版中已不可用，请使用实例方法。

#### 方法 C: 通过 yt-dlp 搜索（flat-playlist 模式）
```bash
python3 -m yt_dlp --flat-playlist --dump-json "ytsearch5:search query"
```
注意：flat-playlist 模式不返回 `upload_date`、`view_count`、`duration_string` 等字段。
如需完整元数据，要另外做一次完整请求：
```bash
python3 -m yt_dlp --dump-json --skip-download "https://youtube.com/watch?v=VIDEO_ID"
```

#### 搜索技巧：按时间限定
当 `freshness_mode = recent` 时，搜索词需包含年份关键词（如 `2026`），因为 YouTube 搜索的"上传日期"筛选在 API/工具层面不一定可靠，嵌入标题的年份是更稳定的信号。
#### 降级处理

如果视频没有英文字幕：

1. 尝试 `--language en` 抓取自动生成字幕
2. 尝试不带语言参数抓取任何可用字幕
3. **Whisper 本地转录**（新）—— 如果以上都不可用，用 Whisper 做音频本地转录：
   ```bash
   # 先用 yt-dlp 下载音频
   python3 -m yt_dlp -x --audio-format mp3 -o "audio.%(ext)s" "URL"
   # 用 Whisper 转录
   whisper audio.mp3 --language English --model base --output_format txt
   # 输出为 audio.txt
   ```
4. 如果仍不可用，标记该视频"无法获取英文字幕"，降级为只输出筛选结果

### Step 4: 文字稿清洗

只做清洗，不做成稿化润色：
- 删除重复片段
- 删除口头禅和停顿噪音
- 修复明显识别错词
- 统一英文术语拼写
- 按主题切段

#### 4.1 从 SRT 字幕文件清洗

yt-dlp 下载的字幕默认保存为 `.srt` 文件，且自动生成的字幕常有**每行重复 3 次**的问题。

**获取字幕命令：**
```bash
python3 -m yt_dlp --skip-download --write-auto-subs --sub-langs en --convert-subs srt -o "output_name" "https://youtube.com/watch?v=VIDEO_ID"
# 输出为 output_name.en.srt
```

**清洗命令：**
```bash
python3 SKILL_DIR/scripts/clean_subtitles.py /path/to/file.srt --output clean.txt
```

脚本会自动去掉序号行、时间轴行、空行，并做 3x 重复去重。

#### 4.2 从 youtube-transcript-api 获取文本

如果使用 `youtube-transcript-api` 库（推荐，直接从 API 获取文本，无需下载文件）：

```python
from youtube_transcript_api import YouTubeTranscriptApi
api = YouTubeTranscriptApi()
result = api.fetch("VIDEO_ID", languages=["en"])
text = " ".join([s.text for s in result.snippets])
# 直接输出到文件
with open("transcript.txt", "w") as f:
    f.write(text)
```

注意：最新版 `youtube-transcript-api`（1.2.x+）必须使用实例方法 `.fetch()`，旧版静态方法 `get_transcript()` 已不可用。

#### 4.3 常见问题

| 问题 | 原因 | 解决 |
|---|---|---|
| SSL 连接失败 | 某些频道的视频反爬严格（如 ArjanCodes） | 换用 yt-dlp 下载字幕 |
| yt-dlp 报错 SSL | 无 JS 运行时 | 添加 `--js-runtimes` 或直接用 python API |
| 字幕为空 | 视频无字幕 | 尝试无 language 参数抓取任何可用字幕 |
| 搜索结果无日期 | flat-playlist 模式 | 对每个视频单独 `--dump-json --skip-download` 获取 upload_date

### Step 5: 中文拆解

必须把英文内容先转成中文结构化理解结果：
- 中文核心主题
- 中文核心结论
- 中文主要观点（3-7 个）
- 中文关键案例
- 中文方法提炼
- 中文可执行动作

### Step 6: 中文学习沉淀

必须至少输出以下之一（推荐全部输出）：
- **中文学习笔记** — 学到了什么、哪些点值得记、视频真正值钱的地方
- **中文方法总结** — 方法、流程、结构、设计思路
- **中文可执行清单** — 今天就能试的 3 个动作、可以复现的 2 个步骤
- **中文迁移建议** — 如何用于自己的项目/skill/workflow

### Step 7: 中文平台改写

> 改写规则详见 `references/rewrite-style-rules.md`

#### 公众号版
- 中文表达自然
- 有导语、小标题、清晰正文、自然结尾
- 有信息密度
- 更像认真看完英文视频后的中文拆解

#### 小红书版
- 中文表达轻快
- 重点前置
- 节奏更短
- 更像中文学习整理/经验笔记
- 更适合收藏和转发

#### 封面提示词（可选）

当 `generate_cover_prompt = true` 时，输出可给 Midjourney/DALL-E 用的封面提示词：

```
封面提示词（Midjourney）：
A clean, modern blog cover with code snippets floating in background,
tech dashboard style, blue and purple neon on dark gradient,
text overlay area at center, no people, 16:9 --ar 16:9 --v 6
```

封面风格建议：
- AI Agent 主题 → 代码流程图 + 蓝色/紫色科技风
- 工具对比 → 左右分屏 + 暖色对比
- 教程 → 步骤图 + 绿色/白色干净风

---

## 七、去 AI 味要求

必须尽量避免：
- 机械排比、模板腔、英文翻译腔
- 空洞拔高、没有信息量的总结句
- "在当今快速发展的 AI 时代"、"值得深思"、"不容忽视" 等套话

必须优先做到：
- 结论先行、重点清楚、自然承接
- 信息优先、结构真实
- 读起来像中文作者写的

---

## 八、学习优先级分层

> 详见 `references/learning-value-criteria.md`

| 级别 | 含义 | 特征 |
|---|---|---|
| S | 强烈优先 | 有明确问题、完整步骤、框架、案例、演示、可迁移、可实操 |
| A | 优先处理 | 有方法、有结构，对学习有明显帮助 |
| B | 可补充 | 有一定启发，适合补认知和视角 |
| C | 低优先 | 有热度但学习价值一般 |
| D | 淘汰 | 学习帮助很弱，热点/盘点/观点/娱乐 |

---

## 九、输出格式要求

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

---

## 十、失败处理

如果出现以下情况，必须明确降级处理：
- 搜到的视频不在主题白名单内
- recent 模式下没有找到足够新的内容
- 学习价值过低
- 无法获取英文字幕
- 音频转写质量差
- 内容结构过散无法提炼

### 降级输出方式
- 只输出中文筛选结果
- 只输出中文学习优先级判断
- 只输出中文拆解卡
- 标记建议人工复核
- 不强行生成发文稿

---

## 十一、质量检查清单

### 学习层
- 这个视频到底学到了什么？
- 有没有明确方法？
- 有没有可执行动作？
- 有没有迁移建议？

### 新鲜度层
- 当前 freshness_mode 是什么？
- 结果是否符合时间窗口要求？
- 是否把经典补充和最近内容区分开了？

### 表达层
- 最终输出是否全中文？
- 是否还有翻译腔？
- 是否还有明显 AI 味？
- 是否平台适配明显？

### 风险层
- 是否过度贴近原视频表达？
- 是否存在未经核实信息？
- 是否把英文内容误读了？
- 是否忽略了时效性风险？

---

## 十二、典型使用示例

```bash
# 示例 1: 给一个视频链接，输出学习笔记 + 公众号 + 小红书
你：帮我处理这个视频 https://youtube.com/watch?v=xxx
    输出中文学习笔记和公众号文章

# 示例 2: 搜索最近 30 天最值得学的 AI Agent 视频
你：帮我搜一下最近 30 天 YouTube 上最值得看的 AI Agent 教程
    freshness_mode = recent, topic_scope = agent

# 示例 3: 混合模式 — 既要新的又要经典的
你：帮我找 AI workflow 相关内容
    freshness_mode = hybrid, 输出学习笔记和小红书笔记

# 示例 4: 只看学习沉淀，不发平台
你：这个视频 https://youtube.com/watch?v=yyy 帮我做中文拆解
    content_goal = learning, target_platform = learning_only
```

---

## 十四、推荐执行策略：先筛后深挖

当有多个候选视频时，推荐分两阶段执行：

### 阶段一：筛选输出
先输出中文筛选结果列表（包含标题、链接、频道、发布时间、learning_priority、平台适配判断），让用户看到全景，选择优先处理的视频。

### 阶段二：单条深度处理
用户选定一条视频后，再按以下顺序输出：
1. 中文视频内容拆解卡
2. 中文学习笔记
3. 中文方法总结
4. 中文可执行清单
5. 中文迁移建议

**不要一次性处理所有候选视频** — 筛选阶段已经完成了优先级判断，深度处理只针对最高优先级的视频。学习价值比覆盖数量更重要。

## 十五、主题白名单扩展说明

本 skill 的主题白名单默认面向 AI Agent / LLM / 工作流等主题（见第五章）。但实际使用中，以下场景也可以覆盖，归入三级优先主题（发文素材 / 开发者工具）：
- **Python 开发工具链**（包管理器、linter、测试工具） — 如果视频涉及工具实操和最佳实践
- **通用开发者效率工具**（CLI 工具、编辑器插件） — 前提是视频有清晰的方法论和步骤演示

判断标准不变：学习价值优先。如果视频只是列表盘点没有方法，则降级处理。

---

## 输出样例

下面是用一条 Agent 教程视频跑出来的学习笔记开头：

```
═══════════════════════════════════════
 中文视频拆解卡
═══════════════════════════════════════
标题：Build an AI Agent from Scratch
频道：AI Makers

【中文核心主题】
从零搭建一个能调用工具、自主决策的 AI Agent，
涵盖工具调用( tool calling)、记忆管理和任务编排三个模块。

【中文核心结论】
Agent 能力的关键不是模型本身大，而是
"工具调用 → 状态跟踪 → 失败重试"这 3 层的设计质量。

【中文方法提炼】
1. 工具注册 → 每个 tool 定义 schema + handler
2. 循环调度 → model → tool_call → execute → observe → model
3. 记忆管理 → 用短期（当前上下文）+ 长期（向量存储）

【中文可执行清单】
□ 克隆 demo 模板
□ 配置 LLM API key
□ 注册第一个自定义 tool
□ 跑通 3 轮 tool_call 循环
```

完整处理还包括公众号文章（有导语/小标题/自然结尾）和小红书笔记（重点前置/节奏短）。
