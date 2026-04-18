# generate_platform_content

## 一、这个脚本是干什么的

这个脚本负责基于已经完成的中文视频拆解卡、中文学习笔记和中文方法总结，生成：

* 中文公众号文章
* 中文小红书风格笔记

它不是翻译脚本，也不是字幕处理脚本。
它的作用是：

**把已经完成理解和沉淀的内容，进一步转化为可发布的中文平台内容。**

---

## 二、这个脚本解决什么问题

如果没有这个脚本，后续生成平台内容时很容易出现几个问题：

* 直接顺着英文字幕写，翻译味重
* 只整理信息，没有平台感
* 公众号和小红书写成一个版本
* 没有基于“学习沉淀”来生成内容

这个脚本就是为了把“中文理解结果”转成“中文可发内容”。

---

## 三、输入

这个脚本建议支持以下输入字段：

* `video_brief`
* `learning_notes`
* `method_summary`
* `actionable_checklist`（可选）
* `target_platform`：wechat / xiaohongshu / both
* `style_rules`
* `banned_patterns`
* `word_count_range`（可选）
* `content_goal`（learning_share / publishing / both）

---

## 四、输出

### 当 target_platform = wechat

输出：

* `title`
* `intro`
* `body`
* `ending`
* `optional_summary`
* `optional_share_copy`

### 当 target_platform = xiaohongshu

输出：

* `title`
* `body`
* `optional_tags`
* `optional_cover_prompt`

### 当 target_platform = both

依次输出：

1. `wechat_version`
2. `xiaohongshu_version`

---

## 五、推荐生成原则

### 1. 必须基于中文理解结果

不要直接根据英文字幕生成。
输入应该优先来自：

* 中文视频拆解卡
* 中文学习笔记
* 中文方法总结

### 2. 学习优先后的再创作

平台稿是学习成果的外化，不是英文视频的直接翻版。

### 3. 必须区分平台

公众号和小红书不能共用一版内容。

### 4. 优先去 AI 味

输出前必须参考：

* `assets/rewrite_style_rules.md`
* `assets/banned_patterns.md`

---

## 六、推荐输出示例

### 公众号版（简化）

```json
{
  "title": "很多人都在讲 AI Agent，但真正决定它能不能落地的，不是模型有多聪明",
  "intro": "最近关于 AI Agent 的内容很多，但真正把这件事讲清楚的并不算多...",
  "body": "正文内容...",
  "ending": "如果把整条视频压成一句话，我会这样概括...",
  "optional_summary": "120字简介",
  "optional_share_copy": "朋友圈转发语"
}
```

### 小红书版（简化）

```json
{
  "title": "这条 AI Agent 视频，我看完只记住了 4 句话",
  "body": "正文内容...",
  "optional_tags": ["AI Agent", "Workflow", "AI学习"],
  "optional_cover_prompt": "封面提示词"
}
```

---

## 七、这个脚本不负责什么

这个脚本不负责：

* 直接抓字幕
* 音频转写
* 清洗英文文字稿
* 判断视频学习价值
* 生成中文拆解卡

它只负责：

**从中文中间层 → 生成中文平台内容。**

---

## 八、失败处理

如果出现以下情况，应明确降级：

* `video_brief` 太弱
* 学习笔记提炼不出重点
* 方法总结不清楚
* 不适合生成平台稿
* 更适合只做学习沉淀

### 推荐返回

* 只输出中文学习笔记
* 只输出中文方法总结
* 只输出发文建议
* 不强行生成公众号 / 小红书成稿

---

## 九、与后续流程的关系

这个脚本的输出，对应：

* `skills/platform-rewrite/SKILL.md`
* `assets/wechat_article_template.md`
* `assets/xiaohongshu_note_template.md`

它是整条链路最靠后的生成层。

---

## 十、执行提醒

这个脚本最重要的，不是“生成得多快”，而是：

* 真正建立在理解基础上
* 真正区分平台
* 真正像中文内容
* 真正能发

平台稿不是字幕翻译稿，而是学习成果的再表达。
