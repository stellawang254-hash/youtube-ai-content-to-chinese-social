# 竞品同类扫描：youtube-ai-content-to-chinese-social

> 分析日期：2026-06-12 | 数据来源：GitHub / ClawHub / skills.sh / Tessl

---

## 关键结论

1. **全链路无直接竞品** — 没找到另一个"AI主题筛选→字幕→中文深度拆解→多平台输出"一体的 Skill
2. **每个环节都有更强的垂直竞品** — 自动化不如 youtube-to-ebook，输出设计不如 video-to-article
3. **最大差距**：零展示、零自动化、Whisper 降级缺失、封面提示词缺失

---

## 第一梯队：最直接竞品

### 1. Librarier-f/video-to-article-skill (★ 17)
- **定位**：YouTube/B站视频转精美文章，5种HTML设计风格，小红书/公众号/口播稿
- **你有它没有的**：AI主题白名单、7步流程、学习优先级分层
- **它有你没有的**：5种设计风格、双向翻译(中英)、B站支持、来源信息保留
- **README可借鉴**：用户痛点描述极佳、问题驱动式文档、设计风格展示

### 2. zarazhangrui/youtube-to-ebook (★ 465)
- **定位**：频道批量管理→字幕→EPUB电子书→邮件自动投递
- **你有它没有的**：中文拆解、多平台适配
- **它有你没有的**：批量频道追踪、EPUB输出、邮件投递、Streamlit仪表盘、launchctl定时
- **README可借鉴**：API Key教程、自动配置、Known Issues表格

### 3. yizhiyanhua-ai/youtube-ai-digest (★ 51)
- **定位**：自动追踪AI相关YouTube频道→字幕→摘要报告
- **你有它没有的**：中文深度拆解、公众号/小红书输出
- **它有你没有的**：AI频道自动追踪、缩略图自动下载、Markdown报告
- **README可借鉴**：输出示例、频道配置方式

### 4. nothinginterested/video-summarizer-skill (★ 13)
- **定位**：YouTube/B站视频总结，字幕+Whisper降级
- **你有它没有的**：学习分层、多平台改写
- **它有你没有的**：Whisper本地转录（无字幕也能处理）、B站cookie处理、时间戳、问答
- **可借鉴**：Whisper降级方案

## 第二梯队

| 项目 | ★ | 亮点 |
|------|:-:|------|
| JiamanJemma/social-creator-toolkit | 27 | 7大爆款公式、封面提示词生成 |
| zeroPointRepo/youtube-skills | 268 | 12个YouTube Skill，全框架兼容 |
| kar2phi/video-lens | 77 | 结构化HTML报告+时间戳+播放器 |
| pH-7/youtube-to-medium-blog-posts-automation | 33 | YouTube→Medium自动发布 |

---

## 生态位定位

```
                      输出形式丰富度
                     ↗
    video-to-article    social-creator-toolkit 
    (5种风格+设计展示)    (爆款公式+封面)
                     
      你的位置 → ●
      (AI垂直+中文深度拆解+全链路)
                     
    youtube-ai-digest      youtube-to-ebook
    (AI频道追踪)            (批量+定时+邮件)
                     ↘
                      自动化程度
```

生态位独特**但展示不够**。用户如果只看首屏，会以为这就是一个"YouTube转中文"工具——功能描述里没有把"AI主题白名单+学习优先级分层+7步流程"这些真正的差异化讲清楚。
