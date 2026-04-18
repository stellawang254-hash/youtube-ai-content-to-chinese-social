# clean_transcript

## 一、这个脚本是干什么的

这个脚本负责把“粗糙的英文字幕 / transcript / 音频转写稿”，清洗成一份更适合后续分析和拆解的英文文字稿。

它不是翻译脚本，也不是成稿脚本。  
它的任务只有一个：

**把原始英文文本整理成可用于中文理解、中文拆解和中文沉淀的工作底稿。**

---

## 二、这个脚本解决什么问题

从 YouTube 或音频转写得到的原始文本，通常会存在这些问题：

- 断句很碎
- 重复很多
- 口头禅太多
- 模型名 / 产品名识别错误
- 英文术语不统一
- 文字虽然有了，但不适合直接拿去分析

这个脚本就是为了解决这些问题。

---

## 三、输入

这个脚本建议支持以下输入字段：

- `raw_subtitle_text`
- `transcription_text`
- `subtitle_segments`（可选）
- `language`
- `domain_hint`（默认 `AI / tech`）
- `preserve_timestamps`（true / false）

---

## 四、输出

至少应输出以下字段：

- `cleaned_transcript`
- `normalized_terms`
- `removed_noise_summary`
- `structure_note`
- `transcript_status`

---

## 五、推荐输出示例

```json
{
  "cleaned_transcript": "Today we're going to look at how AI agents actually work. The key idea is that an agent is not just a chatbot...",
  "normalized_terms": [
    {"raw": "lang graph", "fixed": "LangGraph"},
    {"raw": "gpt four o", "fixed": "GPT-4o"}
  ],
  "removed_noise_summary": [
    "removed filler words",
    "merged repeated subtitle lines"
  ],
  "structure_note": "split into 5 thematic paragraphs",
  "transcript_status": "ready_for_brief"
}