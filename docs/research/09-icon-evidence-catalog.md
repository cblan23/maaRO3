# RO3 图标与状态视觉证据目录

> 快照：2026-07-28。仓库现有 29 份视频 Manifest／127 张视频关键帧、1 份静态 Manifest／1 张论坛一手原图，以及 88 张独立 PNG 裁图，覆盖 46 个机器可读图标／状态键。正式清单以 [`catalog.json`](../../research/evidence/icons/catalog.json) 为准；`TEST-B` 与 `PIONEER-A` 严格隔离，全部样本仍需在国服重采。

## 1. 图片确实保存在哪里

- 视频父帧：[`research/evidence/video/`](../../research/evidence/video/)；
- 静态一手原图：[`research/evidence/still/`](../../research/evidence/still/)；
- 独立裁图：[`research/evidence/icons/crops/`](../../research/evidence/icons/crops/)；
- 每张裁图的父图、坐标、尺寸、哈希和限制：[`catalog.json`](../../research/evidence/icons/catalog.json)；
- 生成与逐像素校验说明：[`icons/README.md`](../../research/evidence/icons/README.md)。

88 张裁图全部未缩放、未抠透明底、未用生成式补图，也没有借用其他 RO 产品。校验器会重新读取父图，按 `x/y/width/height` 裁切并逐像素比对；父图哈希、裁图哈希、尺寸或坐标任一不一致都会失败。

当前置信度分布：85 张 `direct_clear`、3 张 `contextual_candidate`。样本类型为 12 张图标、59 张状态指示、11 张状态行、6 张弹窗／提示；构建分布为 79 张 `TEST-B`、9 张 `PIONEER-A`。

## 2. 88 张正式裁图的完整种类

| 机器键 | 数量 | 已保存状态 | 不能外推的内容 |
|---|---:|---|---|
| `activity_reward_chest` | 4 | 早期绿色勾选候选、未达阈值闭合宝箱、金色可领、绿色已领 | 其他阈值、国服动画、自选箱 |
| `auto_battle_skill_grid` | 1 | 彩色／灰阶技能格混合页面 | 单帧不证明启用含义、优先级或 AutoOn |
| `card_item` | 3 | 背包选中、已装备、详情页选中且锁定 | 不同父页不能混成通用选中／锁定模板 |
| `connection_recovery` | 4 | TEST-B 重连中、双按钮重试、单按钮重新登录；PIONEER-A 英文双按钮 | 国服文本；输入来源、启动器、排队与开放世界状态保留 |
| `competitive_teammate_revive_dialog` | 1 | TEST-B 生存竞争模式救护车“复活已死亡队友”弹窗 | 只作竞技队友交互分类；未点击、未见资源扣除或队友恢复，绝非玩家野外自身复活 |
| `daily_daidai_commission` | 2 | 入口徽记、带“已完成”的整行 | 委托接取至交付流程 |
| `daily_field_farming` | 2 | 野外挂机入口徽记、每日 `0/60` 未完成行 | 每日进度不等于低倍／疲劳 |
| `daily_guild_caravan` | 2 | 公会商队入口徽记、参加 `1/1 已完成`整行 | 不能单独代表四批终局或材料扣除 |
| `daily_life_play` | 3 | 入口徽记、`0/100` 未完成、`100/100 已完成`整行 | 即时 `80/100 → 100/100` |
| `daily_mvp` | 2 | MVP 入口徽记、击杀 `1/5` 未完成行 | 竞争动作和国服次数 |
| `daily_spirit_tower` | 1 | 精灵塔入口徽记 | 层数、失败、结算 |
| `dungeon_dead_wait` | 1 | TEST-B 十人副本复活标志＋等待复活 | Clip 从死亡后开始且复活前结束；不能外推野外选项、费用或 Auto 状态 |
| `farming_boost` | 3 | 可开启 `60/180`、运行 `59分40秒`、耗尽 `0秒/180分` | 低倍和疲劳；三态不是同账号连续链 |
| `farming_kill_counter` | 1 | 个人／队伍累计击杀 | 阶段阈值和国服刷新规则 |
| `farming_reward_feed` | 1 | 高倍 `0秒/180分` 父帧中同步变化的经验、齿轮和物品通知 | 裁区必须联合父帧；不等于客户端已命名“低倍”，也不证明掉率／疲劳 |
| `farming_reward_summary` | 1 | 个人／队伍累计收益汇总 | 不证明背包落点、低倍或疲劳资格 |
| `guild_caravan_batch` | 2 | 连续刷新为 `2/4`；另一来源直接见 `4/4` 进行中 | `4/4` 装满后的终奖与每日变化 |
| `guild_caravan_dispatch` | 2 | 同一第四批短片段：载货 `4/8` 时禁用／红字提示，`5/8` 时黄色发车可用 | 未点击发车；不能外推其他批次／国服阈值或授权自动发车 |
| `guild_caravan_load` | 2 | 提交前 `7/8`、提交后 `8/8` | 背包扣除量 |
| `guild_caravan_reward` | 1 | 满载奖励覆盖层 | 奖励物品名不可读 |
| `guild_material_requirement` | 2 | 选中且库存满足 `6/6`、未选中且不足 `0/6` | 材料名／数量不可固化；未执行购买／求助 |
| `guild_material_submission` | 1 | “物品已提交”反馈 | 不足、购买、失败 |
| `hud_backpack_entry` | 1 | 普通入口＋`Alt+B` 标签 | 悬停、按下、禁用 |
| `inventory_capacity` | 5 | 空 `0/300`；正常 `36/300`、`56/300`、`62/300`、`110/300` | 最高仅 36.7%，仍非接近满／真正满；扩容后上限未知 |
| `inventory_category_tab` | 2 | 通用物品分类选中、相邻分类普通 | 其他分类、悬停、禁用和国服位置 |
| `life_profession_cook` | 1 | 已选厨师徽记 | 国服名称和等级 |
| `life_profession_gardener` | 1 | 可用园艺师卡、等级 2 进度 | 未选择态语义和国服职业规则 |
| `life_profession_miner` | 2 | 已选矿工徽记、可用矿工卡 | 工具、节点归属和选职转换 |
| `life_profession_miner_rank` | 2 | 等阶 1 选中、等阶 2 锁定及要求 | 解锁点击和升级结果 |
| `life_vitality` | 1 | 闪电图标与 `700/5000` | 恢复和国服上限 |
| `notification_red_dot` | 1 | 红点候选 | 红点具体业务语义 |
| `pet_rarity_badge` | 2 | S、A 角标 | 全稀有度与数值规则 |
| `potion_auto_use` | 1 | “HP 低于 70% 自动使用”启用态 | 70% 不是推荐常量；禁用／SP 未采 |
| `potion_quick_slot` | 3 | 数量 36、数量 35、配置缺药提示 | `1 → 0`、自动补槽、购买 |
| `refine_equipment_slot` | 3 | 主手选中、副手普通、鞋子普通 | 铠甲受浮层污染；不执行精炼 |
| `refine_level_badge` | 1 | 0 级徽记 | 其他等级和成功／失败 |
| `refine_result_overlay` | 2 | 同页精炼失败、精炼成功覆盖层 | 经济动作永不自动执行；国服动画相位 |
| `revive_invite` | 1 | 副本等待玩家选择弹窗 | 不能外推野外复活 |
| `shop_card_pack` | 2 | 同一卡册金色选中／可买、购买后变暗／已售罄 | 只属商城；永不授权购买 |
| `siege_revive_countdown` | 7 | PIONEER-A 攻城／模拟对抗赛 27／15／8／5／3／2／0 秒；`0 秒`父帧仍未恢复 HUD | 旧竞争构建；页面阶段仍须结合父帧，不能外推 TEST-B、国服或野外复活 |
| `login_character_selection` | 1 | PIONEER-A 三角色、Recent、创建空位、Enter | TEST-B／国服角色页和默认焦点仍缺 |
| `login_title_screen` | 1 | TEST-B 连接失败后标题标志 | 不证明账号已登录或自动进入下一页 |
| `login_notice_loading` | 1 | TEST-B 公告窗口中央载入中 | 公告关闭／确认输入未知 |
| `login_scene_loading` | 1 | TEST-B 场景载入 `17%` | 数值不可固化，加载卡死阈值未知 |
| `wardrobe_category_tab` | 2 | 普通头饰分类、金色选中脸饰分类 | 两个分类内部图形不同，只比较控件态 |
| `wardrobe_face_item` | 2 | 已装备、白色挂锁 | 静态图不证明解锁／换装流程 |

合计：46 个键、88 张独立文件。

## 3. 最重要的状态链

### 3.1 活跃箱

```text
threshold_not_reached_closed_chest
→ claimable_gold_glow
→ short_transition_still_gold
→ claimed_green_check
```

前后帧见 [Twitch VOD 2807782689](../../research/evidence/video/twitch-vod-2807782689/manifest.json)。早期 `green_check_candidate` 保留为历史候选，不再用于混淆“可领”和“已领”。

### 3.2 公会商队

```text
selected_inventory_sufficient_6_of_6
AND seven_of_eight_before_submit
→ submitted_confirmation_visible
AND eight_of_eight_after_submit
→ reward_overlay_visible
→ batch_two_of_four_refreshed

batch_four_of_four_active
AND disabled_at_4_of_8
→ enabled_at_5_of_8
```

第一段适合离线验证“等待业务变化”。第二段来自另一条二次剪辑中的同一短片段，只证明第四批载货量跨过 5 时发车入口由禁用变为可用；视频没有点击发车。提交和发车都涉及材料／公会事务，技术状态可识别不等于动作获授权。

### 3.3 生活完成

`daily_life_play` 同时有入口徽记和 `vitality_100_of_100_completed`。这纠正了旧文档中的 `4/5 → 5/5` 假设；真实 TEST-B 画面按消耗活力值 `100/100` 表示完成。

### 3.4 高倍挂机

```text
available_60_of_180_start_button_visible
active_countdown_59m40s_close_button_visible
exhausted_0_seconds_of_180_next_reset_0500
```

三态是同一测试构建的页面变体，但来自不同账号。不得生成虚假的跨账号“连续转换”标签，也不得把 exhausted 当 fatigue。

同一耗尽直播又保留了[奖励通知父帧](../../research/evidence/video/twitch-vod-2804807809/frames/24420.00-farming-boost-exhausted-reward-feed.jpg)与 `farming_reward_feed` 裁图：页面保持 `0秒/180分` 时，左侧通知在连续九秒内新增齿轮、`Base经验 X3`和`连帽披肩 X1`，背景伤害仍在发生。这能识别“耗尽但奖励通知仍活动”，不能把未显示的阶段硬命名为低倍，也不能推断掉率或疲劳。

### 3.5 背包与用药

容量已有空／正常两个基准；用药已有启用态和 `36 → 35` 数量差。它们足够启动 OCR 与状态字典设计，不足以解决真正满包或药尽。

### 3.6 页面特有的选中／锁定／售罄

[商城卡册](../../research/evidence/video/shop-card-pack-bv15ytg6jenn/manifest.json)和[衣橱论坛原图](../../research/evidence/still/bahamut-system-overview-187/manifest.json)证明：

- 金色选中框必须绑定具体父页面；
- “已售罄”“白色挂锁”“已装备”是不同业务状态；
- 商城商品变暗不能当作通用禁用态；
- 衣橱锁不能当作等级锁、任务锁或奖励锁模板。

### 3.7 连接恢复与旧构建角色选择

TEST-B 已保存 `reconnecting → retry_dialog → reconnecting → relogin_required` 四个连接页面状态中的三个独立视觉样本；完整父帧链还覆盖标题、公告载入、场景加载和回到世界。PIONEER-A 另保存英文 `retry_dialog`，用于验证双按钮语义跨旧构建存在，但不得混入 TEST-B 模板。

PIONEER-A 的 `login_character_selection` 保留三角色、Recent、创建空位和 Enter，是登录状态机的语义种子；它不能关闭 TEST-B／国服角色选择缺口。

### 3.8 PIONEER-A 竞技自动复活倒计时

[模拟对抗赛第二场](../../research/evidence/video/pioneer-simulation-revive-bv1qwtm6besg/manifest.json)新增同一轮连续链中的 `8／5／2／0 秒`四个裁图，与既有攻城录像的 `27／15／3 秒`一起组成七个数值变体。父帧显示 `5 秒`时视角已在复活台，`0 秒`时技能栏仍未出现，约 `0.70 秒`后的父帧才恢复 HUD。

这四张裁图只适合识别底部复活标志与数值变化。裁区本身不含战场／复活台环境，因此不能单独判断流程阶段；必须同时检测全屏场景和可操作 HUD。全部七张都标为 `PIONEER-A`，禁止混入 TEST-B／国服训练与模板集。

### 3.9 TEST-B 十人副本死亡等待

[Twitch Clip 父帧](../../research/evidence/video/twitch-clip-test-b-raid-dead-wait-g93cchbtrszole42/manifest.json)补出十人副本个人死亡后的持续等待态：主画面变暗、常规技能栏消失，底部中央显示复活标志与“等待复活”，队友和 Boss 战仍继续。裁图已排除主播立绘、聊天、技术测试横幅、UID 和队伍栏。

该 Clip 从死亡后开始、在复活前结束，因此它只把 `DungeonDeadWait` 从五人本交叉验证到十人本，不能补足死亡触发、复活邀请、野外复活选项或恢复 HUD 边界。

## 4. 只有父帧、尚未裁成正式样本的视觉种类

以下内容能在 127 张视频父帧中定位，但没有进入 46 键／88 图的正式裁图库：

- 挂机魔物头像、普通品质标签、AutoOn HUD 候选、技能分类／技能行／热键冷却；
- 采矿交互、4.5 秒进度条、拾取／活力／熟练度提示；
- 园艺师未选择态、配方材料足够／锁定候选；
- 宠物孵化房、品质概率、主战／支援／助战槽、星级、技能类型；
- 精炼材料、多个公会活动卡片；
- 五人本个人死亡父帧、团灭再战、胜利奖励、团队拍卖；十人本死亡等待已有独立裁图；
- 自动挂机地形卡位场景序列。

“父帧中能看到”不等于“已有独立图标文件”。需要作为识别资产使用时，仍应按当前 schema 单独裁切、标注污染和验证像素。

2026-07-28 又逐张查看巴哈五个重点主题的 39 个原图引用（包含跨帖重复图）。这些图只增加宠物、精炼、商城、普通战斗、主线对话、外观和座谈语境；没有画面支持“卡片／灵魂残响接近满载”、疲劳状态、真正满包、野外死亡或公会终局，因此该轮零图入库。第 84 张裁图来自 Twitch 耗尽页同步奖励通知；第 85 张来自后续长评定点回看，直接补到“装运商队 `4/4`”进行中；第 86、87 张分别保存第四批载货 `4/8` 发车禁用和 `5/8` 发车可用。第 88 张是同一长评中另行逐 0.1 秒复核得到的生存竞争模式队友复活弹窗，只扩充竞技负例分类，不关闭玩家自身野外复活缺口。

## 5. 当前仍缺的图标／状态变体

不能从其他 RO 产品或生成式图片补齐：

- 呆呆委托：接取、寻路、子目标进度、交付、最终完成、阻断；
- 公会商队：已有库存不足 `0/6` 行、购买／求助入口、`4/4` 进行中及 `4/8` 禁用 → `5/8` 发车可用；仍缺选中不足项后的禁用／失败、购买价格与结果、求助结果、发车确认／成功／失败及第四批终局；每日 `1/1 已完成`已有裁图但与四批关系未知；
- 生活：`80/100`、即时 `100/100`、活力不足、节点被抢／消失、采集中断；
- 挂机：低倍、疲劳、无目标、自动停止、卡位恢复；
- 背包／药品：接近满、真正满、掉落暂存／丢失、仓库满、药品 `1 → 0`；
- 野外死亡：费用、复活选项、落点、保护状态和 AutoOn 保留／关闭；
- 连接：TEST-B 已有重连中、双按钮失败和重新登录要求；仍缺启动器、账号认证、选服／排队、维护、版本不符、输入可见的重试结果、开放世界原点与 Auto 状态保留；
- 角色：TEST-B／国服角色选择、创建、删除确认、默认焦点和多角色边界；
- 国服简体中文下所有普通、悬停、按下、选中、锁定、可领、已领和禁用变体。

在上述状态补齐前，88 张图片适合做离线分类、差异比较和国服采样种子；它们不能独立授权真实客户端动作。
