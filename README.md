# hermes-youtube-skills

从英文 YouTube AI 视频到中文学习笔记和社交内容，一次完成找→看→懂→用→发。

聚焦 AI Agent / 工作流 / 大模型主题，自动筛选高价值视频，输出中文拆解笔记、微信公众号文章和小红书笔记。不是翻译工具，是视频转中文知识资产的 7 步流程。

```ascii
┌────────────┐   ┌──────────┐   ┌─────────┐   ┌──────────────┐
│ YouTube    │ → │ 字幕提取 │ → │ 中文拆解│ → │ 学习笔记     │
│ 英文AI视频 │   │ 清洗     │   │ 方法提炼│   │ 公众号稿     │
│            │   │          │   │ 可执行  │   │ 小红书笔记   │
└────────────┘   └──────────┘   └─────────┘   └──────────────┘
```

## 安装

```bash
# 复制到 Hermes skills 目录
cp -r SKILL.md references/ scripts/ ~/.hermes/skills/creative/youtube-ai-content-to-chinese-social/
```

或者直接配置 Hermes 从 GitHub 加载（取决于你的 Hermes 版本）。

## 使用

```bash
hermes -s youtube-ai-content-to-chinese-social
```

进入会话后：

```
帮我处理这个视频 https://youtube.com/watch?v=xxx
输出中文学习笔记和公众号文章
```

更多示例见 SKILL.md。

## 依赖

- Python 3.8+
- youtube-transcript-api（字幕获取）
- yt-dlp（备用字幕/音频下载）
- openai-whisper（可选，无字幕时音频转录降级）

## 文件结构

```
hermes-youtube-skills/
├── SKILL.md                    # 主流程（7步 + 测试用例引用）
├── README.md
├── LICENSE
├── references/
│   ├── competitive-landscape.md    # 竞品分析
│   ├── learning-value-criteria.md  # 学习优先级分层
│   ├── rewrite-style-rules.md      # 公众号/小红书改写规则
│   ├── test-cases.md               # 6组测试用例
│   ├── topic-whitelist.md          # 主题白名单
│   └── youtube-search-strategy.md  # 搜索策略模板
└── scripts/
    └── clean_subtitles.py          # 字幕清洗脚本
```

## License

MIT
