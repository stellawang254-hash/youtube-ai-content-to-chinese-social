# get_subtitles

## 一、这个脚本是干什么的

这个脚本负责从 YouTube 视频中获取可用字幕或 transcript。

它的目标不是做内容理解，也不是做中文改写。  
它只负责一件事：

**尽可能稳定地拿到英文字幕文本，为后续清洗、拆解和中文输出提供原始素材。**

---

## 二、这个脚本解决什么问题

在处理英文 YouTube 视频时，最理想的情况不是直接走音频转写，而是：

- 视频本身已经有字幕
- 或者能直接拿到 transcript
- 并且这些文本足够进入下一步清洗

这个脚本就是优先去做这件事的。

---

## 三、输入

这个脚本建议支持以下输入字段：

- `video_url`
- `video_id`（可选）
- `preferred_language`（默认 `en`）
- `fallback_language`（可选）
- `subtitle_mode`（manual_first / auto_ok / transcript_ok）

---

## 四、输出

至少应输出以下字段：

- `subtitle_source_type`：manual / auto / transcript / none
- `language`
- `raw_subtitle_text`
- `subtitle_segments`（可选）
- `confidence_note`
- `next_action_recommendation`

---

## 五、推荐优先级

建议按下面顺序尝试：

### 1. 英文手动字幕
优先使用质量更高、断句更自然的字幕。

### 2. 英文自动字幕
如果没有手动字幕，但自动字幕可用，可以保留。

### 3. 英文 transcript
如果平台或工具能直接输出 transcript，也可作为可用文本来源。

### 4. 获取失败
如果都拿不到，就明确返回失败，并建议进入音频转写流程。

---

## 六、输出示例

```json
{
  "subtitle_source_type": "auto",
  "language": "en",
  "raw_subtitle_text": "Today we're going to look at how AI agents actually work...",
  "subtitle_segments": [
    {"start": 0.0, "end": 3.2, "text": "Today we're going to look at how AI agents actually work"}
  ],
  "confidence_note": "subtitle quality acceptable",
  "next_action_recommendation": "clean_transcript"
}