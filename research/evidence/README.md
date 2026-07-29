# 视觉证据

每组视频帧或静态原图必须和同目录 `manifest.json` 一起提交。Manifest 至少包含：

- 来源 ID 与原始 URL；
- 来源发布时间、测试版本和采集日期；
- 视频的精确时间点，或静态来源中的图片序号；
- 画面展示的事实；
- 是否含解说字幕、水印或后期标注；
- 国服首测是否需要重新验证。

截图只能支持“该测试版本在该画面如此显示”，不能直接证明国服首测仍有相同入口、坐标、次数或规则。

公开视频原帧可能含 UID、玩家名、聊天和水印。仓库当前将其视为内部研究证据；若未来公开仓库、发布数据集或制作宣传材料，必须先重新审查版权、测试条款和个人信息，并制作与原始证据分离的脱敏副本。

视频证据位于 [`video/`](video/) 下，论坛／文章原图位于 [`still/`](still/) 下；
两类目录都包含独立 Manifest 和最少必要画面。静态原图使用独立 Schema，不能伪装
成 `0 秒视频帧`。生活职业与采矿证据见
[`life-mining-bv18h756kehz/manifest.json`](video/life-mining-bv18h756kehz/manifest.json)，
同一原始视频的配方解锁与材料不足精抽见
[`life-crafting-bv1d67v6pemq/manifest.json`](video/life-crafting-bv1d67v6pemq/manifest.json)。

独立图标与 UI 状态裁图见 [`icons/`](icons/README.md)。裁图不能脱离父帧：
目录必须记录来源、视频时间戳或静态图片序号、父图 SHA-256、裁切坐标、缩放算法、污染说明与自身
SHA-256，并由总校验器逐像素复算。

提交前运行 `py -3 tools/validate_research.py`，它会校验来源引用、文件存在性、
SHA-256、国服复验标记，以及裁图与父帧、坐标和缩放声明的逐像素一致性。
