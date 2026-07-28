# UI 视觉证据索引

> 证据帧只证明“对应视频所记录的测试构建在该时刻如此显示”。它们不证明国服入口、坐标、等级、次数或快捷键相同。完整来源元数据和 SHA-256 位于 [Manifest](../../research/evidence/video/day1-guide-bv1yqtk6oekk/manifest.json)。

需要按图标种类和状态变体查找原帧时，见[图标与状态视觉证据目录](09-icon-evidence-catalog.md)。

## 1. 已入库关键帧

### 国服官方首曝：只作身份、日期与宣传 UI 基准

来源：[国服官方 Bilibili 首曝片](https://www.bilibili.com/video/BV1fmKH63EPT/)，完整元数据见 [Manifest](../../research/evidence/video/official-cn-pv-bv1fmkh63ept/manifest.json)。它是 `CN-A` 发行／宣传来源，但片中实机为未标 build 的剪辑素材，不能自动升级为国服客户端规则证据。

| 时间 | 画面 | 支持的状态 | 设计边界 |
|---:|---|---|---|
| 00:16 | [国服宣传片开放世界 HUD](../../research/evidence/video/official-cn-pv-bv1fmkh63ept/frames/0016-cn-promotional-openworld-hud.png) | 简体中文素材同时展示 Base／Job、目标、掉落、小地图和技能栏，可作为 8 月 UI 差异基线 | 未标 build、经过剪辑；不证明自动战斗规则、坐标或最终国服布局 |
| 02:31 | [重逢首测日期片尾](../../research/evidence/video/official-cn-pv-bv1fmkh63ept/frames/0151-cn-reunion-test-date.png) | 国服官方视频明确写出 8 月 27 日重逢首测 | 平台、删档、资格和预下载等仍引用招募公告，并继续监测延期 |

以下各组玩法细节来自 `TEST-B` 启燃测试，只作同项目旧构建旁证：

来源：阿翊《RO仙境传说3 开服第 1 天》，原始 [YouTube](https://www.youtube.com/watch?v=SNpXR5F2UXc)，抽帧使用 [Bilibili 转载源](https://www.bilibili.com/video/BV1YqTK6oEkk/)。测试上下文为 2026-06-25 台港澳启燃技术测试首日。

| 时间 | 画面 | 支持的设计事实 | 不支持的推断 |
|---:|---|---|---|
| 00:48 | [操作模式选择](../../research/evidence/video/day1-guide-bv1yqtk6oekk/frames/0048-control-mode-selection.png) | 曾有经典／现代／行动三种模式；画面示意点地和 WASD | 国服名称、默认模式、完整键位 |
| 05:33 | [自动战斗 HUD](../../research/evidence/video/day1-guide-bv1yqtk6oekk/frames/0333-auto-battle-hud.png) | 游戏内建自动战斗存在；战斗 HUD 多区域并存 | 自动战斗完整启动／停止条件 |
| 06:04 | [生活职业选择](../../research/evidence/video/day1-guide-bv1yqtk6oekk/frames/0364-life-profession-selection.png) | 生活职业页面和两个槽位 | 可选职业、重选规则、国服等级 |
| 06:32 | [每日必做面板](../../research/evidence/video/day1-guide-bv1yqtk6oekk/frames/0392-daily-panel.png) | 委托、公会商队、生活、精灵塔、活跃箱和限时活动 | 固定任务表、阈值、重置时间 |
| 06:49 | [五人副本入口](../../research/evidence/video/day1-guide-bv1yqtk6oekk/frames/0409-five-player-dungeon.png) | 卡片显示五人副本、奖励和次数 | 匹配、战斗、结算流程 |
| 07:10 | [个人摊位上架](../../research/evidence/video/day1-guide-bv1yqtk6oekk/frames/0430-stall-listing.png) | 摊位槽位、背包、税率、价格／货币 UI | 自动交易许可或安全性 |
| 07:28 | [野外挂机选择](../../research/evidence/video/day1-guide-bv1yqtk6oekk/frames/0448-farming-panel.png) | 等级区间、目标魔物、加倍分钟和开始入口 | 国服时长、目标列表、异常恢复 |
| 07:36 | [加倍挂机规则](../../research/evidence/video/day1-guide-bv1yqtk6oekk/frames/0456-farming-rules.png) | 存在可展开的规则说明；内容涉及队伍、累计和击杀 | 低清小字的逐条精确规则 |
| 07:46 | [扩展每日面板](../../research/evidence/video/day1-guide-bv1yqtk6oekk/frames/0466-daily-panel-expanded.png) | 升级后面板加入 MVP、野外挂机并有完成态 | 国服 MVP 次数和挂机进度 |

### 每日奖励与公会商队连续状态

活跃奖励来源：[Twitch VOD 2807782689](https://www.twitch.tv/videos/2807782689)，完整元数据见 [Manifest](../../research/evidence/video/twitch-vod-2807782689/manifest.json)。

| 时间 | 画面 | 支持的状态 | 设计边界 |
|---:|---|---|---|
| 13:35.2 | [20 档金色可领](../../research/evidence/video/twitch-vod-2807782689/frames/0815.20-activity-reward-claimable.jpg) | 活跃度 20；20 档发光，后续档位仍闭合 | 只覆盖一个阈值和一个动画相位 |
| 13:35.6 | [领取后过渡](../../research/evidence/video/twitch-vod-2807782689/frames/0815.60-activity-reward-claimed.jpg) | 输入后短暂仍保持金色，证明“点击完成”不是成功判据 | 文件名沿用早期定位；状态以 Manifest 为准 |
| 13:37.0 | [绿色已领取与反馈](../../research/evidence/video/twitch-vod-2807782689/frames/0817.00-activity-reward-received.jpg) | 绿色勾选是持久终态，且页面未自动关闭 | 奖励经验与同时发生的升级数值不能完全拆分 |

公会商队来源：[Twitch VOD 2805645541](https://www.twitch.tv/videos/2805645541)，完整元数据见 [Manifest](../../research/evidence/video/twitch-vod-2805645541/manifest.json)。

| 时间 | 画面 | 支持的状态 | 设计边界 |
|---:|---|---|---|
| 22:14.4 | [材料满足、载货 7/8](../../research/evidence/video/twitch-vod-2805645541/frames/1334.40-guild-material-ready-load.jpg) | 选中煤矿石，需求／库存 `6/6`，装载按钮可用 | 一键购买／求助不可自动触发 |
| 22:14.6 | [已提交、载货 8/8](../../research/evidence/video/twitch-vod-2805645541/frames/1334.60-guild-material-submitted-full.jpg) | 0.2 秒后出现“物品已提交”，当前批次满载 | 没有背包数量前后帧，不证明精确扣物 |
| 22:15.6 | [提交奖励提示](../../research/evidence/video/twitch-vod-2805645541/frames/1335.60-guild-submit-rewards.jpg) | 公会贡献 200、钱币 5000 提示与后续红点 | 其他背景掉落通知不能归入商队奖励 |
| 22:16.4 | [满载奖励覆盖层](../../research/evidence/video/twitch-vod-2805645541/frames/1336.40-guild-caravan-reward-overlay.jpg) | 奖励层出现，背景已刷新为 2/4 | 奖励物品名不可读 |
| 22:16.8 | [下一批 2/4](../../research/evidence/video/twitch-vod-2805645541/frames/1336.80-guild-caravan-next-batch.jpg) | 新需求同时含满足与不足项目 | 只覆盖 1/4 → 2/4，不证明四批终局 |

### 生活职业、配方与采矿

来源：[启燃测试完整实机](https://www.bilibili.com/video/BV18H756KEhz/)，原始 [YouTube](https://www.youtube.com/watch?v=1S8-6dr2lN4)，完整元数据见 [Manifest](../../research/evidence/video/life-mining-bv18h756kehz/manifest.json)。

| 时间 | 画面 | 支持的状态 | 设计边界 |
|---:|---|---|---|
| 15:50 | [生活职业总览](../../research/evidence/video/life-mining-bv18h756kehz/frames/0950-life-profession-overview.png) | 厨师／矿工两个已选职业槽、等级进度、活力 `700/5000` | 不能推出职业总数、第二槽解锁或重选规则 |
| 16:00 | [绿色药水配方](../../research/evidence/video/life-mining-bv18h756kehz/frames/0960-green-potion-recipe.png) | 材料、数量、制作、职业等级锁和活力消耗 `20` | 没有实际制作、批量、满包或材料不足结果 |
| 16:40 | [采矿进度](../../research/evidence/video/life-mining-bv18h756kehz/frames/1000-mining-progress-45s.png) | `1 级矿脉`、镐子交互、进度 `3.7/4.5s` | 不证明自动导航／连采和中断行为 |
| 16:42 | [第一次结果](../../research/evidence/video/life-mining-bv18h756kehz/frames/1002-mining-yield-1-of-5.png) | 活力 `680`、矿工经验 `220` | 不能单帧推出每日完成 |
| 16:50–17:01 | [第二次](../../research/evidence/video/life-mining-bv18h756kehz/frames/1010-mining-yield-2-of-5.png)、[第三次](../../research/evidence/video/life-mining-bv18h756kehz/frames/1015-mining-yield-3-of-5.png)、[第四次](../../research/evidence/video/life-mining-bv18h756kehz/frames/1021-mining-yield-4-of-5.png) | 严格等差的 `-20／+220` 累计序列 | 不能证明自动选取下一节点 |
| 17:08 | [第五次累计结果](../../research/evidence/video/life-mining-bv18h756kehz/frames/1028-mining-yield-cumulative.png) | 活力 `600/5000`、矿工经验 `1100/5000`，闭合五次事务 | 节点刷新、活力恢复和背包满仍未知 |
| 19:10 | [生活玩法 100/100 已完成](../../research/evidence/video/life-mining-bv18h756kehz/frames/1150-daily-life-100-completed.png) | 同一实机稍后显示每日稳定完成态 | 没拍到即时 `80/100 → 100/100`；活跃 60 还含其他任务 |

补充来源：[测试版本批评与系统分析](https://www.bilibili.com/video/BV1QyT964EHc/)，完整元数据见 [Manifest](../../research/evidence/video/life-professions-bv1qyt964ehc/manifest.json)。

| 时间 | 画面 | 支持的状态 | 设计边界 |
|---:|---|---|---|
| 05:47 | [生活职业全览标签](../../research/evidence/video/life-professions-bv1qyt964ehc/frames/0347-life-profession-overview.png) | 客户端直接显示矿工、厨师、园艺师；矿工／厨师已有等级，园艺师未选用 | 论坛“采药／制药／挖矿”更像功能概括；国服名称、换职与第二槽规则仍待验证 |

### 内建自动战斗、宠物助战与公会日历

来源：[启燃测试结束小结](https://www.bilibili.com/video/BV1YbNy6fEzE/)，完整元数据见 [Manifest](../../research/evidence/video/test-closeout-bv1ybny6feze/manifest.json)。

| 时间 | 画面 | 支持的状态 | 设计边界 |
|---:|---|---|---|
| 01:02 | [宠物助战五槽](../../research/evidence/video/test-closeout-bv1ybny6feze/frames/0062-pet-support-five-slots.png) | 助战 1–5 号位、稀有度、星级和名称是独立可见字段 | 画面不证明作者口述的属性继承比例、解锁或替换规则 |
| 01:32 | [公会活动日历](../../research/evidence/video/test-closeout-bv1ybny6feze/frames/0092-guild-activity-calendar.png) | 五类公会活动以不同卡片和时段展示 | 只用于识别并排除定时／竞争场景，不设计自动参与 |
| 01:47 | [自动战斗设置](../../research/evidence/video/test-closeout-bv1ybny6feze/frames/0107-auto-battle-settings.png) | 设置窗按类别列技能和等级，并与开放世界 HUD、任务和挂机统计同屏 | 单帧不证明启用项、优先级、索敌、用药或当前 AutoOn 状态 |

### 高倍挂机、背包容量与快捷用药

| 来源／时间 | 画面 | 支持的状态 | 设计边界 |
|---|---|---|---|
| `2805739995` 01:38:15 | [高倍可开启 `60分/180分`](../../research/evidence/video/twitch-vod-2805739995/frames/5895.00-farming-boost-available-clean.jpg) | 有额度、金色开启按钮 | 不证明点击后启动；数值不可固化 |
| `2804892798` 03:05:30 → 03:05:40 | [运行起点](../../research/evidence/video/twitch-vod-2804892798/frames/11130.00-farming-boost-active-countdown-start.jpg)、[十秒后](../../research/evidence/video/twitch-vod-2804892798/frames/11140.00-farming-boost-active-countdown-later.jpg) | `59:50 → 59:40`，关闭按钮持续可见 | 未跨到零；与其他两态不是同账号 |
| `2804807809` 06:46:51 → 06:47:15 | [耗尽](../../research/evidence/video/twitch-vod-2804807809/frames/24411.00-farming-boost-exhausted.jpg)、[耗尽时奖励通知变化](../../research/evidence/video/twitch-vod-2804807809/frames/24420.00-farming-boost-exhausted-reward-feed.jpg)、[稳定耗尽](../../research/evidence/video/twitch-vod-2804807809/frames/24435.00-farming-boost-exhausted-stable.jpg) | `0秒/180分`、次日 5:00 补充；页面保持耗尽时齿轮、经验和物品通知仍变化，背景有伤害 | 排除“归零即停战／必然零收益”；仍无低倍／疲劳标签与掉率 |
| `2804892798` 00:07:25 | [空背包 `0/300`](../../research/evidence/video/twitch-vod-2804892798/frames/0445.00-inventory-capacity-empty-0-of-300.jpg) | 空容量与 HUD 背包入口 | 不证明国服／扩容后上限 |
| `2804807809` 05:01:32 | [正常背包 `36/300`](../../research/evidence/video/twitch-vod-2804807809/frames/18092.00-inventory-capacity-normal-36-of-300.jpg) | 远未满的正常容量基准 | 仍不是真正满包 |
| `2805739995` 01:41:50.5 | [自动用药启用、数量 36](../../research/evidence/video/twitch-vod-2805739995/frames/6110.50-quick-potion-auto-use-before.jpg) | 勾选“HP 低于 70% 时自动使用” | 70% 是账号配置，不是推荐常量 |
| `2805739995` 01:41:51.0 | [数量变 35](../../research/evidence/video/twitch-vod-2805739995/frames/6111.00-quick-potion-auto-use-consumed.jpg) | 同窗 `36 → 35` 与战斗持续 | 无键盘输入可视化，仍需受控复测 |
| `2805739995` 01:41:54.5 | [缺少道具反馈](../../research/evidence/video/twitch-vod-2805739995/frames/6114.50-quick-potion-missing-item-toast.jpg) | “背包中没有该道具，无法添加” | 配置缺药不等于战斗中 `1 → 0` |

### 商城与衣橱的通用状态反例

商城来源：[18 秒卡册实机 Manifest](../../research/evidence/video/shop-card-pack-bv15ytg6jenn/manifest.json)；衣橱来源：[巴哈一手原图 Manifest](../../research/evidence/still/bahamut-system-overview-187/manifest.json)。这些样本用于证明“选中、已售罄、已装备、锁定必须按父页面分别建模”，不能当作跨页面通用模板。

| 画面 | 已保存状态 | 边界 |
|---|---|---|
| [卡册选中／可购买](../../research/evidence/video/shop-card-pack-bv15ytg6jenn/frames/0004-shop-card-pack-selected.png) → [购买后已售罄](../../research/evidence/video/shop-card-pack-bv15ytg6jenn/frames/0007-shop-card-pack-sold-out.png) | 同一商品金色选中、变暗售罄 | 涉及货币，永不据此授权购买 |
| [衣橱原图](../../research/evidence/still/bahamut-system-overview-187/images/wardrobe-lock-selected-states.jpg) | 分类普通／金色选中，脸饰已装备／白色挂锁 | 静态图不证明点击、解锁或换装流程 |

### 宠物孵化、主战与支援阵容

来源：[RO3 的宠物系统是什么](https://www.bilibili.com/video/BV14gTK6LELc/)，完整元数据见 [Manifest](../../research/evidence/video/pet-system-bv14gtk6lelc/manifest.json)。

| 时间 | 画面 | 支持的状态 | 设计边界 |
|---:|---|---|---|
| 03:30 | [孵化房等级与品质概率](../../research/evidence/video/pet-system-bv14gtk6lelc/frames/0210-pet-incubation-level-probability.png) | 孵化房 `6 → 7` 升级预览、总熟练度进度和多个品质概率变化是独立 UI 字段 | 不证明熟练度来源、孵化耗时、升级触发方式；等级和概率只属 TEST-B |
| 08:30 | [主战位与三支援槽](../../research/evidence/video/pet-system-bv14gtk6lelc/frames/0510-pet-main-support-slots.png) | 一个主战位、支援 1／2／3；支援 3 显示 Base 50 解锁门槛 | 不证明主战／支援技能效果、替换消耗或解说者所称的属性继承比例 |

### 自动挂机卡位候选序列

来源：[近战职业自动挂机被地形卡住](https://www.bilibili.com/video/BV1rg376UE6k/)，完整元数据见 [Manifest](../../research/evidence/video/auto-blocked-terrain-bv1rg376ue6k/manifest.json)。作者标题的原因判断与画面事实必须分开。

| 时间 | 画面 | 支持的状态 | 设计边界 |
|---:|---|---|---|
| 00:00.5 | [序列起点](../../research/evidence/video/auto-blocked-terrain-bv1rg376ue6k/frames/0000-auto-blocked-start.png) | 角色位于狭窄走廊边缘，附近有魔物；建立位置／朝向基线 | 单帧不证明 AutoOn 或卡位 |
| 00:06.5 | [序列中段](../../research/evidence/video/auto-blocked-terrain-bv1rg376ue6k/frames/0006-auto-blocked-middle.png) | 位置近似不变，但动作轨迹和伤害数字变化，排除静态冻结 | 无法区分攻击、受击或寻路转向，也看不清稳定 AutoOn 标志 |
| 00:13.5 | [序列末端](../../research/evidence/video/auto-blocked-terrain-bv1rg376ue6k/frames/0013-auto-blocked-end.png) | 约 13 秒仍无有效位移进展，支持 `AutoOnBlockedCandidate` 时间窗样本 | 样本太短，不能把 14 秒硬编码成报警阈值；国服和其他职业需复验 |

### 精炼槽与材料来源

来源：[RO3 真的很烂吗](https://www.bilibili.com/video/BV19HTn6PEo2/)，完整元数据见 [Manifest](../../research/evidence/video/refine-ui-bv19htn6peo2/manifest.json)。

| 时间 | 画面 | 支持的状态 | 设计边界 |
|---:|---|---|---|
| 03:02 | [槽位精炼预览](../../research/evidence/video/refine-ui-bv19htn6peo2/frames/0182-refine-slot-level.png) | 左侧按装备部位列等级；右侧显示下一等级、成功率、属性、材料和按钮 | 换装继承仍需连续实机；成功率和消耗只属 TEST-B |
| 03:32 | [精炼材料来源](../../research/evidence/video/refine-ui-bv19htn6peo2/frames/0212-refine-material-sources.png) | 材料可展开获得途径，并与目标槽、预期属性和预算同屏 | 来源可能通向商店或多人玩法；只做缺口报告，不自动前往、购买或精炼 |

### 困难五人本异常状态

来源：[困难蛮荒五人本开荒](https://www.bilibili.com/video/BV1WzTn6QEkE/)，完整元数据见 [Manifest](../../research/evidence/video/hard-five-player-bv1wztn6qeke/manifest.json)。

| 时间 | 画面 | 支持的状态 | 设计边界 |
|---:|---|---|---|
| 02:29.6 | [团灭重整](../../research/evidence/video/hard-five-player-bv1wztn6qeke/frames/0149-party-wipe-retry.png) | `PartyWipe`，全队状态、倒计时、两个决策按钮 | 不能和个人死亡共用处理 |
| 02:40.0 | [再战后 Boss 重置](../../research/evidence/video/hard-five-player-bv1wztn6qeke/frames/0160-boss-reset-after-retry.png) | `BossReset`，全队回场、Boss 100% | 中间投票／加载需单独采样 |
| 12:18.5 | [个人死亡等待](../../research/evidence/video/hard-five-player-bv1wztn6qeke/frames/0738-dead-wait.png) | `DungeonDeadWait`，队友仍在战斗 | 没有自行复活证据 |
| 12:34.5 | [队友复活邀请](../../research/evidence/video/hard-five-player-bv1wztn6qeke/frames/0754-revive-invite.png) | `ReviveInvite`，拒绝／同意 | 自动接受影响团队资源，默认人工 |
| 12:40.5 | [复活后战斗](../../research/evidence/video/hard-five-player-bv1wztn6qeke/frames/0760-revived-fighting.png) | `FightingAfterRevive`，技能栏恢复 | 无敌时间／资源扣减仍未知 |
| 26:22.5 | [胜利奖励](../../research/evidence/video/hard-five-player-bv1wztn6qeke/frames/1582-victory-reward.png) | `VictoryReward`，奖励与倒计时 | 胜利不等于已经退出副本 |

### 十人本机制与队内拍卖

正常战斗、机制与结算来源：[十人副本完整录像](https://www.bilibili.com/video/BV1CNKD6YE4s/)，完整元数据见 [Manifest](../../research/evidence/video/ten-player-raid-bv1cnkd6ye4s/manifest.json)。个人死亡等待另由一条 TEST-B [Twitch Clip](https://www.twitch.tv/fans1021/clip/AggressiveAmusedCodChocolateRain-G93cCHbtRSzole42)交叉验证，见[死亡等待 Manifest](../../research/evidence/video/twitch-clip-test-b-raid-dead-wait-g93cchbtrszole42/manifest.json)。

| 时间 | 画面 | 支持的状态 | 设计边界 |
|---:|---|---|---|
| 01:00 | [十人战斗 HUD](../../research/evidence/video/ten-player-raid-bv1cnkd6ye4s/frames/0060-ten-player-combat-hud.png) | 分组队员、Boss、任务、伤害统计和技能栏并存 | 动态遮挡多，不能套野外 HUD 模板 |
| Clip 00:00 | [十人本个人死亡等待](../../research/evidence/video/twitch-clip-test-b-raid-dead-wait-g93cchbtrszole42/frames/0000.00-ten-player-dead-wait.png) | `DungeonDeadWait`：画面变暗、技能栏消失、底部等待复活；队友战斗继续 | Clip 从死亡后开始且复活前结束；不能补足触发、邀请或野外复活 |
| 05:00 | [密集圆形 AOE](../../research/evidence/video/ten-player-raid-bv1cnkd6ye4s/frames/0300-dense-circle-aoe.png) | 大量位置预警与机制物体 | 不设计自动走位 |
| 15:00 | [等待队长开战](../../research/evidence/video/ten-player-raid-bv1cnkd6ye4s/frames/0900-waiting-for-leader.png) | `WaitingForLeader`，Boss 可见但未开战 | Boss 可见不等于 Fighting |
| 25:00 | [交叉网格 AOE](../../research/evidence/video/ten-player-raid-bv1cnkd6ye4s/frames/1500-grid-aoe.png) | 另一类全场机制视觉 | 只作人工接管提示 |
| 28:40 | [团队拍卖面板](../../research/evidence/video/ten-player-raid-bv1cnkd6ye4s/frames/1720-team-auction-panel.png) | `TeamAuction`，物品和倒计时 | 经济行为默认排除 |
| 29:00 | [拍卖二次确认](../../research/evidence/video/ten-player-raid-bv1cnkd6ye4s/frames/1740-auction-confirmation.png) | 带货币价格的确认弹窗 | 不可当作普通奖励确认 |

### 连接恢复、标题返回与角色选择

TEST-B 直接来源：[GVG 骑士完整录像](https://www.bilibili.com/video/BV1h2Kf6qEFz/)，完整元数据和九帧连续链见 [Manifest](../../research/evidence/video/gvg-knight-bv1h2kf6qefz/manifest.json)。竞争场景本身仍排除自动参与，但连接层可作为同构建状态证据。

| 时间 | 画面／状态 | 支持的状态 | 设计边界 |
|---:|---|---|---|
| 12:34.5 → 12:35.0 | [正常战斗](../../research/evidence/video/gvg-knight-bv1h2kf6qefz/frames/0754.5-before-disconnect.png) → [重新连接中](../../research/evidence/video/gvg-knight-bv1h2kf6qefz/frames/0755.0-reconnecting.png) | 自然出现的正常态到连接恢复进行态 | 不知道断线根因或底层重试次数 |
| 12:54.8 → 12:55.3 | [双按钮重试](../../research/evidence/video/gvg-knight-bv1h2kf6qefz/frames/0774.8-retry-dialog.png) → [再次重连中](../../research/evidence/video/gvg-knight-bv1h2kf6qefz/frames/0775.3-reconnecting-after-dialog.png) | “返回登入／重新连接”与等待态可区分 | 输入不可见，不能声称由客户端自动选择 |
| 13:05.7 → 13:07.0 | [要求重新登入](../../research/evidence/video/gvg-knight-bv1h2kf6qefz/frames/0785.7-relogin-required.png) → [标题页](../../research/evidence/video/gvg-knight-bv1h2kf6qefz/frames/0787.0-title-screen.png) | 可重试失败态会转为单按钮重新登录终态 | 没有账号验证、服务器或角色选择画面 |
| 13:12.0 → 13:15.0 | [公告载入](../../research/evidence/video/gvg-knight-bv1h2kf6qefz/frames/0792.0-notice-loading.png) → [场景加载](../../research/evidence/video/gvg-knight-bv1h2kf6qefz/frames/0794.0-scene-loading.png) → [回到 GVG](../../research/evidence/video/gvg-knight-bv1h2kf6qefz/frames/0795.0-returned-to-gvg.png) | 本次最终恢复到世界而非停在登录页 | 不能证明全程无人干预、原坐标、AutoOn 或任务状态保留 |

PIONEER-A 只作跨构建语义对照，不进入 TEST-B／国服模板：

- [英文开放世界连接失败链](../../research/evidence/video/twitch-vod-2540550896/manifest.json)：`OpenWorld → UnableToConnect 双按钮 → TitleScreen`；
- [角色进入链](../../research/evidence/video/twitch-vod-2541630934/manifest.json)：`CharacterSelection → ControlModeSelection → OpenWorld`，证明旧构建存在角色选择，但 TEST-B 与国服仍缺该页直接样本；
- [模拟对抗赛自动复活链](../../research/evidence/video/pioneer-simulation-revive-bv1qwtm6besg/manifest.json)：`AliveCombat → DeadCountdown → RevivePointWait → CountdownZero → RevivedHud`，只证明旧竞技模式状态机。

### PIONEER-A 竞技死亡／自动复活对照

来源：[模拟对抗赛第二场](https://www.bilibili.com/video/BV1QwTM6bESg/)，完整元数据和七帧连续链见 [Manifest](../../research/evidence/video/pioneer-simulation-revive-bv1qwtm6besg/manifest.json)。全片按 2 秒复核；首轮按 0.25 秒精抽，触发与恢复边界再按 0.02–0.05 秒请求相邻解码帧。请求秒数不是原视频帧 PTS，以下只写可复核的观测边界。

| 时间 | 画面／状态 | 支持的状态 | 设计边界 |
|---:|---|---|---|
| 01:20.58 | [正常战斗 HUD](../../research/evidence/video/pioneer-simulation-revive-bv1qwtm6besg/frames/0080.58-alive-combat-hud.png) | 最后一张明确保留底部技能栏的正常态观测帧 | 特效密集，不能判断致死技能 |
| 01:20.85 | [死亡＋9 秒](../../research/evidence/video/pioneer-simulation-revive-bv1qwtm6besg/frames/0080.85-dead-countdown-9.png) | 死亡横幅、自动复活提示和技能栏消失已经出现 | 只能约束到相邻视频帧，不能声称服务端毫秒时间 |
| 01:22.00 | [战场观察＋8 秒](../../research/evidence/video/pioneer-simulation-revive-bv1qwtm6besg/frames/0082.00-dead-countdown-8.png) | 数值递减且背景战斗继续，排除一次性静态提示 | 顶部目标更新会遮挡，不能整屏硬匹配 |
| 01:25.25 | [复活台＋5 秒](../../research/evidence/video/pioneer-simulation-revive-bv1qwtm6besg/frames/0085.25-revive-point-countdown-5.png) | 倒计时未结束时视角已切到复活点等待阶段 | 不知道切换由秒数还是战场规则触发 |
| 01:28.00 | [复活台＋2 秒](../../research/evidence/video/pioneer-simulation-revive-bv1qwtm6besg/frames/0088.00-revive-point-countdown-2.png) | 临近复活的稳定等待态 | 仍不可操作，不可把小数值当成功 |
| 01:30.00 | [复活台＋0 秒](../../research/evidence/video/pioneer-simulation-revive-bv1qwtm6besg/frames/0090.00-revive-point-countdown-0.png) | 归零后技能栏仍未恢复，存在短同步／动画间隔 | 不能硬编码固定 0.70 秒等待 |
| 01:30.70 | [HUD 恢复](../../research/evidence/video/pioneer-simulation-revive-bv1qwtm6besg/frames/0090.70-auto-revived-hud.png) | 生命条、目标框和技能栏重新出现，闭合自动复活链 | 不证明 AutoOn 恢复或角色会自动离开复活点 |

约 `03:49–03:58` 还出现第二轮同类死亡／复活循环，说明首轮不是孤立剪辑帧。另一条 12:34 的[先锋公会战](https://www.bilibili.com/video/BV1WGbhz2EMB/)已全程按 2 秒复核；红／绿区域切换属于战场传送或控制点变化，没有找到可靠玩家死亡终态。两条都属于 PIONEER-A 竞争内容，既不能关闭 TEST-B 开放世界死亡缺口，也不能提高开放世界无人值守评分。

## 2. 已审阅但未入库的录像

为控制版权和仓库体积，下面只保留 URL、时间轴和结论，不提交完整视频或整张 storyboard。

| 来源 | 时长 | 审阅状态 | 主要用途 |
|---|---:|---|---|
| [一周体验](https://www.bilibili.com/video/BV1oKNi6kEzy/) | 17:49 | 音轨已完整转写并人工复核 | 日常负担、挂机／图鉴、生活、宠物、经济评价 |
| [启燃测试完整实机](https://www.bilibili.com/video/BV18H756KEhz/) | 22:28 | 时间轴复核 + 9 帧入库 | 生活职业、配方、4.5 秒采矿、五次资源序列和 `100/100 已完成` |
| [Day2：二转、精炼、裂隙、疲劳](https://www.bilibili.com/video/BV1GqTK6oE4n/) | 05:36 | 已建立分钟级时间轴 | 地图、嘉奖宝库、加倍／疲劳、图鉴目标 |
| [Day4：三转与灵魂残响](https://www.bilibili.com/video/BV1YqTK6oE7g/) | 06:03 | 已建立分钟级时间轴 | 主线后日常、五人本、残响来源／配置 |
| [十人副本完整录像](https://www.bilibili.com/video/BV1CNKD6YE4s/) | 29:27 | 三张 storyboard 已审阅 | 团队列表、Boss 阶段、AOE、机制和结算 |
| [伊尔莫普通攻略](https://www.bilibili.com/video/BV1teNM6SEeM/) | 02:57 | storyboard 与画面文字已审阅 | 音符颜色、人数占位、弹人、换色冷却 |
| [困难五人本开荒](https://www.bilibili.com/video/BV1WzTn6QEkE/) | 27:00 | 异常时间轴复核 + 6 帧入库 | 团灭、Boss 重置、个人死亡、复活邀请、复活后战斗与胜利 |
| [恶魔波利 MVP](https://www.bilibili.com/video/BV1hG7G6eEoE/) | 00:50 | storyboard 已审阅 | 野外多人 Boss 与奖励结算 |
| [黄金虫 MVP](https://www.bilibili.com/video/BV1yp7Y67Eko/) | 07:11 | 已快速审阅 | Boss 战、多人参与、长战斗状态 |
| [敏骑挂机螳螂](https://www.bilibili.com/video/BV1HgTi6oEra/) | 02:45 | 连续时间轴已审阅 | 自动战斗、目标切换、掉落、地图 HUD；无死亡或低倍／疲劳边界 |
| [骑士金 2 挂机](https://www.bilibili.com/video/BV1C1T36oEWs/) | 01:37 | 已快速审阅 | 同一循环的不同地图／怪物样本 |
| [骑士挂机直升机哥布灵](https://www.bilibili.com/video/BV1adTz6XECf/) | 04:58 | 已快速审阅 | 长挂机、技能与目标变化 |
| [6 分钟挂出 2 张卡](https://www.bilibili.com/video/BV1FkKd6CEYL/) | 05:15 | 连续事件时间线已审阅 | 技能设置、卡片遮罩、收益汇总、加倍挂机页；不含阶段转换 |
| [测试版本批评与系统分析](https://www.bilibili.com/video/BV1QyT964EHc/) | 07:20 | 完整转写、storyboard 复核 + 1 帧入库 | 养成、公会、生活职业正式标签和版本评价 |
| [启燃测试结束小结](https://www.bilibili.com/video/BV1YbNy6fEzE/) | 03:13 | 完整转写、storyboard 复核 + 3 帧入库 | 宠物助战五槽、公会活动日历、自动战斗设置 |
| [RO3 的宠物系统是什么](https://www.bilibili.com/video/BV14gTK6LELc/) | 16:41 | 完整转写、storyboard 复核 + 2 帧入库 | 孵化房升级字段、一个主战位与三个支援位；30% 继承仍仅属解说 |
| [RO3 真的很烂吗](https://www.bilibili.com/video/BV19HTn6PEo2/) | 06:33 | 完整转写、storyboard 复核 + 2 帧入库 | 精炼槽位、成功率、材料预算与来源入口 |
| [Twitch VOD 2805645541](https://www.twitch.tv/videos/2805645541) | 03:18:50 | 故事板＋目标区间＋8 帧入库 | 活跃奖励、公会商队 `7/8 → 8/8 → 奖励 → 2/4` |
| [Twitch VOD 2804892798](https://www.twitch.tv/videos/2804892798) | 03:35:59 | 故事板＋目标区间＋3 帧入库 | 空背包与高倍运行倒计时 |
| [Twitch VOD 2804807809](https://www.twitch.tv/videos/2804807809) | 08:26:10 | 故事板＋目标区间＋耗尽后 190 秒逐秒连续复核＋4 帧入库 | 正常背包、高倍耗尽稳定态，以及耗尽期间奖励通知继续变化 |
| [Twitch VOD 2805739995](https://www.twitch.tv/videos/2805739995) | 01:58:58 | 故事板＋聊天定位＋5 帧入库 | 高倍可开启、快捷自动用药、数量变化与缺药反馈 |
| [Twitch Clip：十人本死亡等待](https://www.twitch.tv/fans1021/clip/AggressiveAmusedCodChocolateRain-G93cCHbtRSzole42) | 00:59 | 全片 1 秒复核＋1 帧入库 | TEST-B 十人本持续个人死亡等待；没有触发或恢复边界 |
| [攻城战初体验](https://www.bilibili.com/video/BV1QRTq61EHH/) | 12:08 | 两张 storyboard 已审阅 | 大量玩家、团队 UI、区域、器械与阶段 |
| [PIONEER-A 模拟对抗赛第二场](https://www.bilibili.com/video/BV1QwTM6bESg/) | 05:21 | 全程 2 秒复核＋首轮 0.25／0.02 秒边界精抽＋7 帧入库 | 两轮竞技死亡自动复活；旧构建隔离，不替代开放世界证据 |
| [PIONEER-A 先锋公会战](https://www.bilibili.com/video/BV1WGbhz2EMB/) | 12:34 | 全程 2 秒复核，负向登记 | 战场传送／控制点变化；无可靠玩家死亡 UI |
| [TEST-B 七日心得转载剪版](https://www.bilibili.com/video/BV1wJTb6BEdY/) | 03:58 | 全程 2 秒复核，负向登记 | 副本、PVP、活动、商城与普通战斗；无目标异常或新图标 |
| [经典 RO 标题误标](https://www.bilibili.com/video/BV1w9736mETV/) | 00:40 | 全程 0.5 秒复核，D 级排除 | 标题中的“小站Ro3”不是《仙境传说3》；画面为经典 RO，不保存模板 |
| [巴哈 RO3 板目录快照](https://m.gamer.com.tw/forum/B.php?bsn=81475) | 74 主题 | TEST-B 时段正文／留言关键词扫描＋39 个原图引用复核 | 只补到分类背包接近满与疲劳后低收益的文字报告；原图无对应 UI，零帧入库 |
| [全职业三转试玩＋跑图](https://www.bilibili.com/video/BV1vhhizdEeX/) | 09:46 | storyboard 已审阅 | 职业技能、跑图、旧先锋构建 HUD |
| [制作人对搬砖／宏的回应切片](https://www.bilibili.com/video/BV1aqMc6LEN7/) | 07:28 | 已审阅，语义有歧义 | 只能作运营态度线索，不能推翻正式协议 |

## 3. Day1 精细时间轴

| 时间 | 内容 |
|---:|---|
| 00:45–00:55 | 三种操作模式；经典鼠标点地、现代 WASD |
| 01:10–01:18 | 设置入口、画面与 UI 缩放 |
| 05:30–05:40 | 自动战斗 HUD、宠物开放线索 |
| 05:55–06:05 | 精灵塔、生活职业 |
| 06:20–06:32 | 活力、公会商队、活跃箱／每日面板 |
| 06:35–06:40 | 定时活动／日历 |
| 06:45–06:58 | 五人本、奖励、队伍配置 |
| 07:00–07:12 | 摆摊、定价、上架槽位 |
| 07:20–07:37 | 野外挂机、加倍时长和规则 |
| 07:40–07:50 | 扩展每日面板、狩猎挑战 |

## 4. Day2 精细时间轴

| 时间 | 内容 |
|---:|---|
| 00:30 | 活跃面板 |
| 00:35–00:55 | 五人／MVP 副本、Boss 走位、队内拍卖 |
| 02:15 | 嘉奖宝库／裂隙周常 |
| 02:30 | 地图选择、蝴蝶翅膀／传送 |
| 02:54–03:09 | 开放时段、每周宝箱与旧测试刷新时间 |
| 03:54 | 活跃度 100 状态 |
| 03:59–04:29 | 每日加倍、今日击杀、掉落模式、疲劳后卡片限制 |
| 04:44–04:59 | 地图魔物图鉴与示例击杀目标 |

## 5. 生活与连续挂机补充时间轴

### BV18H756KEhz：生活采集

| 时间 | 内容 |
|---:|---|
| 15:50 | 厨师／矿工职业卡、等级进度、活力 `700/5000` |
| 16:00 | 绿色药水材料、数量、活力 `20` 和职业等级锁 |
| 16:38–16:42 | 选择 `1 级矿脉`、4.5 秒采集、首次活力／经验日志 |
| 16:42–17:28 | 在相邻节点间重复移动和采集；不能证明游戏内自动连采 |

### BV1FkKd6CEYL：持续挂机和卡片遮罩

| 时间 | 内容 |
|---:|---|
| 00:00 起 | 开放地图组队挂机，目标、伤害、经验和掉落持续变化 |
| 00:20 | 战斗中打开技能／辅助设置，背景战斗继续 |
| 02:25–02:29 | 第一张狸猫卡片大遮罩；随后继续战斗 |
| 02:35 | 挂机收益窗口显示距上次查看约 `00:01:44` 的汇总 |
| 04:31–04:34 | 第二张狸猫卡片遮罩，背景仍可见战斗数字 |
| 04:36 | 打开加倍挂机沙漏、剩余时间和目标列表 |

该录像自身没有加倍归零、进入低倍或进入疲劳的连续边界，也没有死亡、满包、卡位和掉线样本。另一条 Twitch 录像现已补到高倍耗尽页以及耗尽时仍变化的经验／物品通知；这只证明归零后并非必然零收益，仍没有客户端命名的低倍、掉率对照或疲劳稳定态。

## 6. 后续关键帧入库条件

新截图必须同时满足：

1. 能支持一个尚无视觉证据的重要事实；
2. 精确记录来源 URL、视频 ID、发布时间、秒数和测试版本；
3. 标明字幕、水印、后期标注和画质限制；
4. 不把整段视频或大量连续帧提交仓库；
5. SHA-256 与 Manifest 一起提交；
6. 明确 `recheck_in_cn_test: true`；
7. 如果含账号、UID、聊天或其他玩家信息，先做隐私审查。

## 7. 国服实机证据的目标质量

8 月采样优先使用原生客户区截图，不使用二次转码视频帧。每个关键状态至少采集：

- 干净初始帧；
- 鼠标悬停／选中帧；
- 操作后的成功帧；
- 不满足前置条件帧；
- 加载／动画中间帧；
- 一种可恢复异常帧；
- 对应环境指纹和客户端版本。

这样才能支持多帧识别和后置条件验证，而不仅是训练一张“看起来像按钮”的模板。
