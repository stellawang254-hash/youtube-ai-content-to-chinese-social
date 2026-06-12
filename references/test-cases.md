# YouTube AI 内容 Skill — 测试用例

> 测试 prompt + 预期输出。每次修改流程、白名单或输出模板后，至少运行这组测试确认不回归。
> 这些测试设计为「新用户安装后 3 分钟内能跑通一条完整流程」。

---

## 测试 1：核心流程 — 给一条 URL 输出学习笔记

### 测试 prompt

```
帮我处理这个视频 https://www.youtube.com/watch?v=UC5W00zIgIM
content_goal = learning, target_platform = learning_only
只输出中文学习笔记，不需要公众号和小红书稿
```

假设该视频标题为 "Build an AI Agent from Scratch in 30 Minutes" / 频道名 "AI Makers"

### 预期输出结构（不是逐字精确，但必须包含以下所有 section）

```
═══════════════════════════════════════
 中文视频拆解卡
═══════════════════════════════════════
标题：Build an AI Agent from Scratch in 30 Minutes
频道：AI Makers
链接：https://youtube.com/watch?v=UC5W0...

【中文核心主题】
[2-3 句说明视频讲了什么]

【中文核心结论】
[1-2 句视频最核心的判断]

【中文主要观点】(3-7个)
1. ...
2. ...

【中文关键案例】
[视频中演示的具体例子]

【中文方法提炼】
[视频的方法/流程/框架提炼]

【中文可执行清单】
□ [步骤1]
□ [步骤2]
□ [步骤3]

【中文迁移建议】
[如何用到自己的项目/skill/workflow]
```

### 验证点

- [ ] 输出了完整的 8 个 section
- [ ] 全文是中文（技术术语可保留英文）
- [ ] 没有翻译腔
- [ ] 可执行清单至少 3 项

---

## 测试 2：搜索筛选 + freshness_mode 验证

### 测试 prompt

```
帮我搜一下最近 7 天 YouTube 上最值得看的 AI Agent 教程
freshness_mode = recent, recency_window_days = 7, topic_scope = agent
```

### 预期输出结构

```
═══════════════════════════════════════
 中文筛选结果
═══════════════════════════════════════
freshness_mode: recent (7天窗口)

  ✅ [S] 视频标题 | 频道名 | 发布时间
      学习价值：有明确方法+完整框架+可实操
      平台适配：适合公众号

  ✅ [A] 视频标题 | 频道名 | 发布时间
      学习价值：有方法有结构
      ...

  ⚠️ 共搜索到 12 个匹配视频，其中 5 个在时间窗口内。
  推荐优先处理：视频A（强烈优先）
```

### 验证点

- [ ] 只返回 recency_window_days 内的视频
- [ ] 有 S/A/B/C/D 优先级标注
- [ ] 超过窗口的视频被过滤或单独标记为"经典补充"
- [ ] 搜索词包含时间限定词

---

## 测试 3：无字幕降级处理

### 测试 prompt

```
帮我处理这个视频 https://www.youtube.com/watch?v=NO_SUBTITLES_123
假设这个视频没有任何可用字幕（英文字幕和自动生成字幕均不可用）
```

### 预期输出

```
⚠️ 降级处理：无法获取英文字幕
尝试了：手动字幕 → 无 / 自动生成字幕 → 无 / 无语言参数 → 无
该视频标记为"无法获取英文字幕"，已降级为只输出筛选结果。

视频标题：[title]
链接：[URL]
频道：[channel]
建议：人工核查是否有字幕，或换用其他来源。
```

### 验证点

- [ ] 先尝试手动字幕 → 自动字幕 → 无语言参数（3 级降级）
- [ ] 降级时有明确标记
- [ ] 不强行生成发文稿

---

## 测试 4：Hybrid 模式验证

### 测试 prompt

```
帮我找 AI workflow 相关内容
freshness_mode = hybrid, recency_window_days = 30
```

### 预期输出

```
freshness_mode: hybrid

─── 近期推荐（最近 30 天）───
✅ [S] 视频A | 发布日: 2026-06-08
✅ [A] 视频B | 发布日: 2026-06-01

─── 经典补充（超出时间窗口，但学习价值高）───
📌 [S] 视频C | 发布日: 2026-04-15 | ⭐ 经典补充
📌 [A] 视频D | 发布日: 2026-03-20 | ⭐ 经典补充
```

### 验证点

- [ ] 近期推荐和经典补充分开标记
- [ ] 经典内容标记了 ⭐ 或 "经典补充"
- [ ] 时间窗口计算正确

---

## 测试 5：去 AI 味检查

### 测试 prompt

```
帮我处理这个视频 https://www.youtube.com/watch?v=TEST_AI_FLAVOR
处理完后检查输出中是否包含以下禁用短语：
"在当今快速发展的 AI 时代"、"值得深思"、"不容忽视"、"随着人工智能的不断发展"
```

### 预期输出

```
✅ 去 AI 味检查通过
禁用短语命中：0个
翻译腔检测：无
结论先行：是
信息密度：高
```

### 验证点

- [ ] 无禁用套话
- [ ] 结论先行
- [ ] 读起来像中文作者写的，不是翻译的

---

## 测试 6：质量检查清单自动跑

### 测试 prompt（处理完一条视频后）

```
对这个视频的处理结果跑一遍质量检查清单（第十一节）并给出报告
```

### 预期输出

```
学习层
✅ 学到了明确的方法
✅ 有可执行动作
✅ 有迁移建议

新鲜度层
✅ freshness_mode = recent, 结果在 7 天窗口内
✅ 近期推荐和经典补充已区分

表达层
✅ 全中文输出
✅ 无翻译腔
✅ 无 AI 味

风险层
✅ 未过度贴近原视频
✅ 所有信息经核实
✅ 时效性风险已标注
```

---

## 工具链验证

### 字幕获取

```python
from youtube_transcript_api import YouTubeTranscriptApi
api = YouTubeTranscriptApi()
result = api.fetch("UC5W0...", languages=["en"])
assert len(result.snippets) > 0
```

### 字幕清洗

```bash
python3 scripts/clean_subtitles.py test_data/test_subtitles.srt --output /tmp/clean.txt
cat /tmp/clean.txt | head -5
# 预期：无序号行、无时间轴行、无3x重复
```
