---
name: youtube-ai-content-to-chinese-social
description: Search English YouTube AI videos around agents, workflows, advanced LLM usage, prompting, tools, and practical builds; prioritize learning value and practical value first; then generate Chinese learning notes, method summaries, actionable checklists, WeChat articles, and Xiaohongshu notes.
---

# YouTube AI Content to Chinese Social Skill

## What this skill does

This skill processes **English YouTube AI videos** into **Chinese learning outputs and Chinese publishable content**.

It is designed for tasks such as:

- finding high-value English AI videos
- selecting videos by learning value
- extracting subtitles or transcript
- cleaning transcript text
- building a structured video brief
- generating Chinese learning notes
- generating Chinese WeChat articles
- generating Chinese Xiaohongshu notes

This is **not** a direct translation skill.

---

## Default workflow

Always follow this order unless the user explicitly asks to skip steps:

1. search English YouTube content
2. select by learning value
3. extract English subtitles / transcript
4. clean transcript
5. build structured brief
6. generate Chinese learning outputs
7. generate Chinese platform outputs

---

## Default priorities

When tradeoffs appear, use this priority order:

1. learning value
2. practical / implementation value
3. reusable method value
4. publishing fit
5. engagement signals

Do not prioritize hype first.

---

## Scope

This skill is optimized for topics such as:

- AI agents
- agentic workflows
- LLM workflows
- tool calling
- multi-agent systems
- LangGraph
- LangChain
- structured output
- system prompt design
- advanced prompting
- automation workflows
- practical AI builds
- AI coding / productivity tools

---

## Inputs

Typical inputs include:

- one English YouTube URL
- a list of English YouTube URLs
- an English search topic
- a channel name
- a content goal:
  - learning
  - publishing
  - both

Optional input hints:

- target_platform: wechat / xiaohongshu / both / learning_only
- topic_scope
- learning_first = true
- output_language = zh-CN

---

## Expected outputs

### Learning outputs
- Chinese selection result
- Chinese video brief
- Chinese learning notes
- Chinese method summary
- Chinese actionable checklist
- Chinese migration suggestions

### Publishing outputs
- Chinese WeChat article
- Chinese Xiaohongshu note
- optional title candidates
- optional short summary
- optional share copy
- optional cover prompt

---

## Read these files first

When this skill is invoked, prioritize these repository files:

### Core workflow
- `SKILL.md`
- `AGENTS.md`

### Selection
- `skills/video-selection/SKILL.md`
- `references/youtube_search_strategy.md`
- `references/learning_value_criteria.md`
- `references/video_selection_criteria.md`

### Transcript layer
- `skills/transcript-extraction/SKILL.md`
- `scripts/get_subtitles.md`
- `scripts/transcribe_audio.md`
- `scripts/clean_transcript.md`

### Deconstruction layer
- `skills/content-deconstruction/SKILL.md`
- `assets/video_brief_template.md`
- `scripts/build_video_brief.md`
- `references/workflow_notes.md`

### Rewrite layer
- `skills/platform-rewrite/SKILL.md`
- `assets/wechat_article_template.md`
- `assets/xiaohongshu_note_template.md`
- `assets/rewrite_style_rules.md`
- `assets/banned_patterns.md`
- `scripts/generate_platform_content.md`

### Examples
- `examples/end_to_end_demo.md`
- `examples/sample_wechat_article.md`
- `examples/sample_xiaohongshu_note.md`
- `examples/personal_style_wechat_sample.md`
- `examples/personal_style_xiaohongshu_sample.md`

---

## Operating rules

### 1. English source, Chinese output
Assume:
- search in English
- process English input
- output in Chinese

### 2. Never write from raw subtitles directly
Always transform raw transcript into a structured brief first.

### 3. Learning notes are mandatory by default
If the user does not explicitly request publishing-only output, generate at least:
- Chinese learning notes
- Chinese method summary
- Chinese actionable checklist

### 4. Distinguish platforms
WeChat and Xiaohongshu must not share the same writing structure.

### 5. Keep style natural
Avoid:
- translation tone
- generic AI phrasing
- inflated summaries
- repetitive framework clichés

### 6. Prefer reusable abstractions
When extracting value, prioritize:
- workflow
- method
- design pattern
- reusable skill candidate
- actionable sequence

---

## Failure handling

If any earlier stage is weak, downgrade gracefully.

Examples:
- weak selection → output recommendation only
- weak transcript → request manual review
- weak brief → stop before publishable content
- low publishing fit → produce learning outputs only

Do not force publishable Chinese content from poor inputs.

---

## Good invocation examples

- Find 3 English YouTube videos on AI agents and rank them by learning value.
- Use this skill to process one English workflow video into Chinese learning notes and a WeChat draft.
- Build a Chinese video brief from this English transcript before writing anything publishable.
- Generate only Chinese learning outputs, not publishable content.
- Turn this English AI video into a Xiaohongshu-style Chinese note after a full deconstruction step.

---

## Final reminder

This skill is not for "subtitle translation".

It is for:

**learning-first transformation of English YouTube AI content into reusable Chinese knowledge assets and Chinese platform-ready outputs.**