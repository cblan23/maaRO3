# 研究资料库

这里保存能够回溯到公开来源的研究产物，不保存完整转载视频。

## 目录约定

- `catalog/sources.json`：来源、可靠性、版本和审阅状态；
- `catalog/sources.schema.json`：来源目录结构约束；
- `evidence/video/<source_id>/manifest.json`：截图与视频时间点的对应关系；
- `evidence/video/<source_id>/frames/`：仅供内部研究的必要 UI 帧；
- `evidence/still/<source_id>/manifest.json`：论坛／文章一手原图的来源、图片序号和哈希；
- `evidence/still/<source_id>/images/`：只保存支持目标状态的最少静态原图；
- `evidence/icons/catalog.json`：独立图标／状态裁图的父帧、坐标、缩放、哈希和污染记录；
- `evidence/icons/crops/`：从已校验父帧精确裁出的最小 PNG 样本；
- `notes/`：按来源整理的转述笔记，避免保存整段逐字稿；
- `raw/`、`work/`：本地临时下载与转写结果，已被 Git 忽略。

## 证据等级

- `A`：RO3 官方页面、公告或官方实机画面；
- `B`：2026 启燃测试参与者的完整录屏/截图/一手长文；
- `C`：媒体转述或多个一手来源可相互印证的总结；
- `D`：旧版本、同 IP 其他游戏、推测或单一未验证说法。

设计结论至少需要一个 A/B 级证据；坐标、按钮状态、次数、重置时间等易变信息必须在国服首测重新采样。

## 版权约定

截图仅截取理解 UI 所需的最小范围，保留来源和时间点；静态原图另记原文与原图 URL，不伪装成 `0 秒视频帧`。这些文件不作为宣传素材或再分发内容。完整视频只放本地临时目录，不能提交仓库。
