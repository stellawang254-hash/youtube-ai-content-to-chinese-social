# AGENTS.md

## Repository purpose

This repository is a learning-first workflow for turning high-value **English YouTube AI videos** into:

- Chinese learning notes
- Chinese method summaries
- Chinese actionable checklists
- Chinese WeChat articles
- Chinese Xiaohongshu notes

The workflow is **not** a translation workflow.
It is a **search → selection → transcript → deconstruction → Chinese output** workflow.

---

## Working rules for Codex

### 1. Always prioritize learning value over popularity
When processing video-related tasks, follow this order:

1. learning value
2. practical / implementation value
3. publishing fit
4. engagement signals

Do not optimize for heat or novelty first.

### 2. English in, Chinese out
Default assumptions:

- search in English
- process English YouTube videos
- prefer English subtitles / transcript / transcription
- final outputs must be Chinese unless explicitly requested otherwise

### 3. Never write directly from raw subtitles
Do not generate final Chinese articles directly from raw English subtitles.

Always go through this sequence:

1. selection
2. transcript extraction
3. transcript cleaning
4. video brief / deconstruction
5. Chinese learning outputs
6. platform rewrite

### 4. Reuse repository assets before inventing new structure
When asked to generate outputs, prioritize these files:

- `SKILL.md`
- `skills/video-selection/SKILL.md`
- `skills/transcript-extraction/SKILL.md`
- `skills/content-deconstruction/SKILL.md`
- `skills/platform-rewrite/SKILL.md`
- `references/youtube_search_strategy.md`
- `references/learning_value_criteria.md`
- `references/video_selection_criteria.md`
- `references/workflow_notes.md`
- `assets/video_brief_template.md`
- `assets/wechat_article_template.md`
- `assets/xiaohongshu_note_template.md`
- `assets/search_query_templates.md`
- `assets/rewrite_style_rules.md`
- `assets/banned_patterns.md`
- `examples/end_to_end_demo.md`
- `examples/sample_wechat_article.md`
- `examples/sample_xiaohongshu_note.md`
- `examples/personal_style_wechat_sample.md`
- `examples/personal_style_xiaohongshu_sample.md`

### 5. Respect the repository workflow
If asked to automate or extend the repository, prefer preserving the current architecture:

- root `SKILL.md` as main workflow description
- `skills/` for subskills
- `scripts/` for executable or executable-adjacent workflow layers
- `assets/` for templates
- `references/` for standards and criteria
- `examples/` for target-shape outputs

### 6. Keep outputs useful, not inflated
Prefer:

- compact structure
- direct language
- executable logic
- reusable abstractions

Avoid:

- verbose filler
- translation-like prose
- generic AI wording
- mixing WeChat and Xiaohongshu into one format

### 7. When implementing scripts, follow the markdown specs first
For any future script implementation, treat these files as source-of-truth contracts:

- `scripts/fetch_youtube_metadata.md`
- `scripts/get_subtitles.md`
- `scripts/transcribe_audio.md`
- `scripts/clean_transcript.md`
- `scripts/build_video_brief.md`
- `scripts/generate_platform_content.md`

Do not change their I/O shape casually.
If a contract change is needed, update the markdown spec first.

### 8. Prefer minimal, testable increments
When adding code:

- implement one script at a time
- preserve file names
- keep inputs/outputs explicit
- avoid large refactors unless requested

### 9. For content tasks, learning outputs come before publishing outputs
Default output priority:

1. Chinese video brief
2. Chinese learning notes
3. Chinese method summary
4. Chinese actionable checklist
5. Chinese WeChat article
6. Chinese Xiaohongshu note

If the user asks for publishing only, that override is allowed.

### 10. If unclear, ask or inspect before rewriting architecture
Do not silently flatten or replace the repository structure.
Prefer adding compatible layers.