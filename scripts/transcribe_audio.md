# transcribe_audio

## 一、这个脚本是干什么的

这个脚本负责在没有可用英文字幕或 transcript 时，把视频音频转成英文文字稿。

它是字幕获取链路里的兜底方案，不是首选方案。  
也就是说：

**优先拿现成字幕，拿不到时，再走音频转写。**

---

## 二、这个脚本解决什么问题

不是每条英文 YouTube 视频都带有：

- 手动字幕
- 自动字幕
- transcript

当这些都拿不到，或者拿到的字幕质量太差时，就需要从音频本身出发，重新生成英文文字稿。

这个脚本就是为这种情况准备的。

---

## 三、输入

这个脚本建议支持以下输入字段：

- `video_url` 或 `audio_file_path`
- `language_hint`（默认 `en`）
- `output_mode`（plain_text / segmented）
- `domain_hint`（AI / tech / mixed）
- `speaker_count`（可选）
- `timestamp_required`（true / false）

---

## 四、输出

至少应输出以下字段：

- `transcription_text`
- `segmented_transcription`（可选）
- `detected_language`
- `quality_note`
- `terminology_risk_note`
- `next_action_recommendation`

---

## 五、推荐输出示例

```json
{
  "transcription_text": "Today we're going to look at how AI agents actually work...",
  "segmented_transcription": [
    {"start": 0.0, "end": 4.2, "text": "Today we're going to look at how AI agents actually work"}
  ],
  "detected_language": "en",
  "quality_note": "medium",
  "terminology_risk_note": "AI terms may need correction",
  "next_action_recommendation": "clean_transcript"
}