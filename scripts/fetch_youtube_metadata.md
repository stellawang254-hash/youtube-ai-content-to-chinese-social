# fetch_youtube_metadata

## 一、这个脚本是干什么的

这个脚本负责从 YouTube 视频中获取基础元数据和公开可见的互动代理指标。

它不是内容分析脚本，也不是字幕提取脚本。  
它的任务只有一个：

**为后续的视频筛选层提供足够稳定、可比较的输入数据。**

---

## 二、这个脚本解决什么问题

在正式处理视频之前，需要先知道：

- 这条视频标题是什么
- 来自哪个频道
- 发布时间是什么时候
- 时长多长
- 播放、点赞、评论大概是什么水平
- 有没有字幕 / transcript 的可能性
- 这条内容是不是值得进入下一步

这个脚本就是负责拿这些信息的。

---

## 三、输入

这个脚本建议支持以下输入方式：

### 1. 单条视频链接
- `youtube_url`

### 2. 多条视频链接
- `youtube_url_list`

### 3. 频道 URL
- `channel_url`

### 4. 搜索结果列表
- `video_url_list_from_search`

---

## 四、输出

至少应输出以下字段：

- `video_title`
- `video_url`
- `channel_name`
- `published_at`
- `duration`
- `view_count`
- `like_count`
- `comment_count`
- `description`
- `tags`（如果可获取）
- `thumbnail_url`（可选）
- `subtitle_available`
- `transcript_available`
- `language_hint`

---

## 五、推荐衍生字段

为了方便后续筛选，建议额外计算：

- `like_rate = like_count / view_count`
- `comment_rate = comment_count / view_count`
- `freshness_days`
- `rough_engagement_score`

这些不是必须字段，但很适合给筛选层使用。

---

## 六、输出示例

```json
{
  "video_title": "How AI Agents Actually Work",
  "video_url": "https://youtube.com/xxx",
  "channel_name": "Example Creator",
  "published_at": "2026-04-10",
  "duration": "18:25",
  "view_count": 182000,
  "like_count": 9200,
  "comment_count": 640,
  "description": "This video explains how AI agents work...",
  "tags": ["AI agent", "workflow", "automation"],
  "subtitle_available": true,
  "transcript_available": true,
  "language_hint": "en",
  "like_rate": 0.0505,
  "comment_rate": 0.0035,
  "freshness_days": 7,
  "rough_engagement_score": 0.71
}