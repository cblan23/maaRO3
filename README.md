# maaRO3

《RO 仙境传说 3》的 MaaFramework 前期研究与离线采样仓库。

当前阶段不是可用的游戏脚本。仓库用于在 2026 年 8 月国服“重逢测试”前积累可追溯资料、离线关键帧、架构契约和采样方案；在拿到客户端、复核专项协议并取得覆盖具体行为的书面许可之前，不实现或运行真实客户端输入。

## 当前已经具备

- 241 条机器可读来源，覆盖国服官方、全球官方、Bilibili、YouTube、Twitch、巴哈、4Gamers、PChome、PTT 等；23 条 Twitch 分类内有效 VOD 与 3 条分类外／混合 RO3 长直播已完成故事板、聊天定位和重点秒级回抽，另有 9 条 Twitch 非 RO3 误命中完成 1,800 张全程稀疏帧排除；Twitch 全时段目录的 30 条 Clip（8 条 TEST-B＋22 条旧构建）均已全片复核，巴哈 RO3 板 74 个主题已完成目录盘点与 TEST-B 时段定向扫描，多批 YouTube 长直播因公开访问验证仍待审帧；
- 26 条官方／准官方来源的逐条事实和待复核项；
- 31 份视频 Manifest／138 张视频关键帧和 1 份静态 Manifest／1 张一手原图，覆盖日常、挂机、生活、宠物、精炼、公会、精灵之塔、异常、连接与复活反例，带 URL、BVID／VOD／Clip、时间戳、限制和 SHA-256；
- 52 个机器可读图标／状态键、99 张可逐像素回溯的独立 PNG 裁图，逐项记录父帧、坐标、哈希、污染、构建隔离与国服复验要求；
- 游戏类型、操作方式、日常、挂机、MVP、五人本、十人本、生活、公会、交易和异常状态的事实矩阵；
- 2026-08-25／27 协议复核与实机采样手册；
- 参考 MaaKES 后形成的 Win32、不可变 RunSpec、分层 Router、动作事务、SQLite WAL 和 replay 设计；
- MaaFramework Project Interface v2 的 Win32 骨架、官方 Schema 快照和 CI；
- 强制 `OFFLINE_RESEARCH` 的策略文件与回归检查。

## 关键入口

- [预研总档案：长期设计依据](docs/research/00-master-dossier.md)
- [玩法与操作事实库](docs/research/01-game-facts.md)
- [候选能力矩阵](docs/research/02-opportunity-matrix.md)
- [UI 证据索引](docs/research/03-ui-evidence-index.md)
- [8 月国服采样手册](docs/research/04-august-capture-plan.md)
- [未决问题与冲突](docs/research/05-open-questions.md)
- [视频审阅队列](docs/research/06-video-review-queue.md)
- [日常系统百科与首期边界](docs/research/07-daily-system-encyclopedia.md)
- [流程级直接证据缺口](docs/research/08-direct-evidence-gap-log.md)
- [图标与状态视觉证据目录](docs/research/09-icon-evidence-catalog.md)
- [详细研究报告](docs/research/10-detailed-research-report.md)
- [官方来源台账](docs/research/official_sources.md)
- [详细架构设计](docs/design/architecture.md)
- [阶段路线图](docs/design/roadmap.md)
- [合规门](docs/design/compliance_gate.md)

## 工程骨架

```text
assets/interface.json        MaaFramework PI v2；只含 Win32 占位控制器
assets/resource/pipeline/    唯一节点是 DirectHit + DoNothing
config/research_policy.json  当前能力门；真实输入为 false
deps/tools/                  固定提交的官方 MaaFramework Schema
research/catalog/            来源目录
research/evidence/           最小关键帧、图标裁图、Manifest、坐标与哈希
tools/research/              公开视频检索、临时下载、抽帧和联络表工具
tests/                       策略、Interface、来源和证据回归检查
```

`assets/interface.json` 的窗口标题与类名是故意不可能匹配的占位值。没有国服实机标定时不得改成 `.*`，也不得照搬 MaaKES 的 ADB／MuMu 配置。

## 本地校验

```powershell
py -3 tools/validate_research.py

py -3 -m unittest discover -s tests -p "test_*.py" -v

py -3 tools/validate_schema.py `
  --schema-dir deps/tools `
  --resource-dirs assets/resource `
  --interface-files assets/interface.json
```

可选的 Maa checker：

```powershell
npm ci
npm run maa:check
```

## 研究工具

公开视频只下载到系统临时目录，不提交完整视频：

```powershell
powershell -File tools/research/fetch_bilibili_sample.ps1 -Bvid BV1YqTK6oEkk

uv run --python 3.12 --with av --with pillow python tools/research/extract_frames.py `
  --input "$env:TEMP/maaRO3-research/BV1YqTK6oEkk/video.m4s" `
  --output "research/work/BV1YqTK6oEkk" `
  --times 333 388 448 456 466
```

关键帧必须人工审阅，并与 Manifest 一起提交。字幕、水印和解说者说法要与客户端画面事实分开。

## 合规边界

Bilibili 游戏中心现行协议把可影响游戏操作、包括模拟用户操作的独立程序纳入外挂范围，并明确举例自动升级、自动练级、自动吃药和自动完成任务。RO3 全球条款也禁止 auto／macro，但明确排除中国，不能代替国服专项条款。

因此当前只允许公开资料整理、离线录像分析、合成／离线识别和架构测试。正式客户端截图、OCR、键鼠输入、自动任务、挂机维持、交易、PVP／GVG、多账号、反检测、注入、抓包和私有协议均不默认获准。完整门禁见 [合规门](docs/design/compliance_gate.md)。

如果 8 月没有获得专项书面许可，项目仍可继续做日常状态看板、离线识别、人工提醒和版本差异分析，但不会转成正式服自动化。
