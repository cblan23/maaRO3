# RO3 图标与状态视觉证据目录

> 快照：2026-07-29。仓库现有 37 份视频 Manifest／175 张视频关键帧、1 份静态 Manifest／1 张论坛一手原图，以及 130 张独立 PNG 裁图，覆盖 70 个机器可读图标／状态键。正式清单以 [`catalog.json`](../../research/evidence/icons/catalog.json) 为准；裁图库中的 `TEST-B` 与 `PIONEER-A` 严格隔离。最新 TEST-B 精抽补入职业天赋节点锁定／可启用／已激活、能力普通／选中、选择弹层和“选中但仍锁定”页签；全部当前裁图都需在国服重采。

## 1. 图片确实保存在哪里

- 视频父帧：[`research/evidence/video/`](../../research/evidence/video/)；
- 静态一手原图：[`research/evidence/still/`](../../research/evidence/still/)；
- 独立裁图：[`research/evidence/icons/crops/`](../../research/evidence/icons/crops/)；
- 每张裁图的父图、坐标、尺寸、哈希和限制：[`catalog.json`](../../research/evidence/icons/catalog.json)；
- 生成与逐像素校验说明：[`icons/README.md`](../../research/evidence/icons/README.md)。

130 张裁图全部未缩放、未抠透明底、未用生成式补图，也没有借用其他 RO 产品。校验器会重新读取父图，按 `x/y/width/height` 裁切并逐像素比对；父图哈希、裁图哈希、尺寸或坐标任一不一致都会失败。

当前置信度分布：127 张 `direct_clear`、3 张 `contextual_candidate`。样本类型为 12 张图标、88 张状态指示、19 张状态行、11 张弹窗／提示；构建分布为 112 张 `TEST-B`、18 张 `PIONEER-A`。

## 2. 130 张正式裁图的完整种类

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
| `spirit_tower_floor_status` | 3 | 同页普通未通关、黄色选中未通关、绿色已通关勾 | 未出现锁定／禁用；三种同屏状态不是点击转换录像 |
| `spirit_tower_milestone_reward` | 2 | 同坐标橙色可领格、点击后绿色已领勾 | 奖励图案会变化；不得把状态模板绑定宠物蛋或固定层数 |
| `talent_profession_ability_option` | 2 | 同坐标白色未选中、稳定金色选中 | 选中仍是待确认；技能名／数值不从 480p 小字固化 |
| `talent_profession_choice_action` | 1 | 选择能力后出现的黄色确定 | 可见不等于已应用；必须等弹层消失和树节点稳定 |
| `talent_profession_choice_dialog` | 1 | “请选择职业天赋”双分支、四能力普通态 | 构筑选择保留人工门；无输入日志 |
| `talent_profession_node` | 3 | 同坐标深灰问号锁定、金色问号可启用／选中、具体图标＋%徽标已激活 | 不外推解锁条件、技能名、重置或升级成本 |
| `talent_profession_primary_action` | 1 | 右侧详情黄色启用 | 启用只进入选择，不代表职业天赋已生效 |
| `talent_rank_tab` | 1 | `II+-1` 黄色当前选中且锁图标仍在 | 直接证明 selected 与 locked 正交；黄色不等于已解锁 |
| `dungeon_dead_wait` | 1 | TEST-B 十人副本复活标志＋等待复活 | Clip 从死亡后开始且复活前结束；不能外推野外选项、费用或 Auto 状态 |
| `dungeon_respawn_opportunities` | 2 | PIONEER-A 印尼语十人本接受复活前 `2`、成功后 `1`，同坐标 | 资源归属、初始上限、重置条件和国服数值 |
| `dungeon_revive_sos` | 1 | PIONEER-A 十人本死亡暗层中的蓝色十字 `SOS` 按钮 | 未点击；请求对象、冷却、资源后果及国服行为未知 |
| `dungeon_revive_success` | 1 | PIONEER-A 印尼语“已由队友复活”成功提示 | 只作后置状态；仍须同时等待死亡层消失与 HUD 恢复 |
| `farming_boost` | 3 | 可开启 `60/180`、运行 `59分40秒`、耗尽 `0秒/180分` | 低倍和疲劳；三态不是同账号连续链 |
| `farming_kill_counter` | 1 | 个人／队伍累计击杀 | 阶段阈值和国服刷新规则 |
| `farming_reward_feed` | 1 | 高倍 `0秒/180分` 父帧中同步变化的经验、齿轮和物品通知 | 裁区必须联合父帧；不等于客户端已命名“低倍”，也不证明掉率／疲劳 |
| `farming_reward_summary` | 1 | 个人／队伍累计收益汇总 | 不证明背包落点、低倍或疲劳资格 |
| `growth_badge_promotion_progress` | 2 | 同坐标领取前 `1/7`、领取后 `2/7`，含晋升任务标签和进度条 | 只证明该次领取增加 1；阶段总数、奖励到账和国服规则未知 |
| `growth_badge_task_row` | 3 | 低于目标 `1/6`＋蓝色前往；同一天赋任务 `126/120`＋金色领取、稍后 `120/120`＋绿色已完成 | 客户端没有字面“未完成”或“已领取”；不能泛化为其他页面的通用领取状态 |
| `growth_badge_tracker` | 1 | 开放世界右侧成长徽章＋绿色可领取 | 不能定位具体任务，且单条领取后仍保留，不是成功后置条件 |
| `guild_caravan_batch` | 2 | 连续刷新为 `2/4`；另一来源直接见 `4/4` 进行中 | `4/4` 装满后的终奖与每日变化 |
| `guild_caravan_dispatch` | 2 | 同一第四批短片段：载货 `4/8` 时禁用／红字提示，`5/8` 时黄色发车可用 | 未点击发车；不能外推其他批次／国服阈值或授权自动发车 |
| `guild_caravan_load` | 2 | 提交前 `7/8`、提交后 `8/8` | 背包扣除量 |
| `guild_caravan_reward` | 1 | 满载奖励覆盖层 | 奖励物品名不可读 |
| `guild_material_requirement` | 2 | 选中且库存满足 `6/6`、未选中且不足 `0/6` | 材料名／数量不可固化；未执行购买／求助 |
| `guild_material_submission` | 1 | “物品已提交”反馈 | 不足、购买、失败 |
| `hud_backpack_entry` | 1 | 普通入口＋`Alt+B` 标签 | 悬停、按下、禁用 |
| `inventory_capacity` | 5 | 空 `0/300`；正常 `36/300`、`56/300`、`62/300`、`110/300` | 最高仅 36.7%，仍非接近满／真正满；扩容后上限未知 |
| `inventory_category_tab` | 2 | 通用物品分类选中、相邻分类普通 | 其他分类、悬停、禁用和国服位置 |
| `launcher_game_entry` | 1 | TEST-B 启动器黄色 Start Game 就绪态，含版本文字和设置入口 | 账号认证、补丁、维护、按钮禁用与输入来源 |
| `life_craft_failure` | 1 | 繁中“所需消耗的道具不足，无法制造！”直接提示 | 不等同于活力不足、满包、等级锁定或通用禁用 |
| `life_green_potion_recipe` | 2 | 同坐标绿色药水选中＋锁图标、解锁后选中＋药水图标 | 可解锁锁态不等同于厨师等级锁；解锁不代表材料足够 |
| `life_profession_cook` | 1 | 已选厨师徽记 | 国服名称和等级 |
| `life_profession_gardener` | 1 | 可用园艺师卡、等级 2 进度 | 未选择态语义和国服职业规则 |
| `life_profession_miner` | 2 | 已选矿工徽记、可用矿工卡 | 工具、节点归属和选职转换 |
| `life_profession_miner_rank` | 2 | 等阶 1 选中、等阶 2 锁定及要求 | 解锁点击和升级结果 |
| `life_recipe_primary_action` | 2 | 同坐标金色主动作由“解锁”切换为“制作” | 金色／看似可用不代表材料充足，也不授权自动点击 |
| `life_recipe_unlock_confirmation` | 1 | “学习”模态框、1000 道具、取消／解锁 | 道具正式名称与国服成本；资源动作保留人工门 |
| `life_recipe_unlock_success` | 1 | “配方解锁／厨师／绿色药水”成功覆盖层 | 未显示扣费后余额，也不等于制作成功 |
| `life_vitality` | 1 | 闪电图标与 `700/5000` | 恢复和国服上限 |
| `notification_red_dot` | 1 | 红点候选 | 红点具体业务语义 |
| `pet_rarity_badge` | 2 | S、A 角标 | 全稀有度与数值规则 |
| `potion_auto_use` | 1 | “HP 低于 70% 自动使用”启用态 | 70% 不是推荐常量；禁用／SP 未采 |
| `potion_quick_slot` | 3 | 数量 36、数量 35、配置缺药提示 | `1 → 0`、自动补槽、购买 |
| `refine_equipment_slot` | 3 | 主手选中、副手普通、鞋子普通 | 铠甲受浮层污染；不执行精炼 |
| `refine_level_badge` | 1 | 0 级徽记 | 其他等级和成功／失败 |
| `refine_result_overlay` | 2 | 同页精炼失败、精炼成功覆盖层 | 经济动作永不自动执行；国服动画相位 |
| `revive_invite` | 2 | TEST-B 繁中五人本、PIONEER-A 印尼语十人本的队友复活邀请弹窗 | 不能外推野外复活；旧十人本接受后可见次数消耗，默认不自动接受 |
| `shop_card_pack` | 2 | 同一卡册金色选中／可买、购买后变暗／已售罄 | 只属商城；永不授权购买 |
| `siege_auto_teleport_countdown` | 2 | PIONEER-A 英文攻城死亡后的 Go to Respawn Point＋自动传送 `10／0 秒` | 这是复活前的第一阶段；裁区含两个常驻管理图标，禁止与后续 Respawn 倒计时混类 |
| `siege_revive_countdown` | 9 | PIONEER-A 攻城／模拟对抗赛 27／20／15／8／5／3／2／1／0 秒；20／1 秒为英文变体，`0 秒`父帧仍未恢复 HUD | 旧竞争构建；页面阶段仍须结合父帧，不能外推 TEST-B、国服或野外复活 |
| `login_character_selection` | 2 | PIONEER-A 三角色页；TEST-B 最近角色金色选中、新建空位和进入游戏 | 国服；角色创建／删除、多角色默认焦点、上限和翻页 |
| `login_title_screen` | 1 | TEST-B 连接失败后标题标志 | 不证明账号已登录或自动进入下一页 |
| `login_notice_loading` | 1 | TEST-B 公告窗口中央载入中 | 公告关闭／确认输入未知 |
| `login_notice_panel` | 1 | TEST-B 启燃测试公告已载入、列表／NEW／正文／关闭控件 | 正文与日期不可固化；关闭输入未知 |
| `login_server_entry` | 1 | TEST-B S1-01 单服、绿色状态图案、黄色“进入游戏” | 绿色图案语义、选服、排队、维护、满员和禁用 |
| `login_scene_loading` | 2 | TEST-B 场景载入 `17%` 与 `95%` | 数值不可固化，完成／卡死阈值未知 |
| `ui_layout_editor` | 1 | TEST-B 自订布局控制框说明、全部／常驻／提示／战斗筛选 | 拖移、保存、取消、恢复预设后的连续结果 |
| `wardrobe_category_tab` | 2 | 普通头饰分类、金色选中脸饰分类 | 两个分类内部图形不同，只比较控件态 |
| `wardrobe_face_item` | 2 | 已装备、白色挂锁 | 静态图不证明解锁／换装流程 |

合计：70 个键、130 张独立文件。

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

### 3.7 TEST-B 正常进入与连接恢复

TEST-B 已保存 `reconnecting → retry_dialog → reconnecting → relogin_required` 四个连接页面状态中的三个独立视觉样本；完整父帧链还覆盖标题、公告载入、场景加载和回到世界。PIONEER-A 另保存英文 `retry_dialog`，用于验证双按钮语义跨旧构建存在，但不得混入 TEST-B 模板。

新增 TEST-B 混合直播又保存：

```text
launcher_game_entry.start_game_ready
→ login_notice_panel.announcement_ready
→ login_server_entry.s1_01_selected_entry_enabled
→ login_character_selection.recent_character_selected_create_slot_visible
→ login_scene_loading.loading_95_percent
→ OpenWorld（只保留父帧）
```

这条同录像链关闭了 TEST-B 启动器就绪、公告就绪、单服入口和单角色页的存在性缺口；PIONEER-A 三角色样本只补充旧构建语义。两条录像均没有输入事件，不能据此建立自动点击序列，国服也仍须全部重采。

### 3.8 可变 UI 布局

`ui_layout_editor.custom_layout_filter_dialog` 直接保存“拖移控制框可以调整位置”、全部／常驻／提示／战斗筛选及恢复预设入口。它证明固定绝对坐标不是可靠前提；录像没有拖移、保存、取消或恢复结果，因此识别器仍须使用锚点、相对 ROI 与运行前布局指纹。

### 3.9 PIONEER-A 竞技自动复活倒计时

[模拟对抗赛第二场](../../research/evidence/video/pioneer-simulation-revive-bv1qwtm6besg/manifest.json)提供同一轮连续链中的 `8／5／2／0 秒`四个裁图，与既有繁中攻城录像的 `27／15／3 秒`组成七个数值变体。父帧显示 `5 秒`时视角已在复活台，`0 秒`时技能栏仍未出现，约 `0.70 秒`后的父帧才恢复 HUD。

[英文攻城第一视角](../../research/evidence/video/pioneer-english-siege-respawn-bv1y7xpzmeyy/manifest.json)进一步证明死亡回场由两个不同页面阶段组成：先显示 `Auto-teleporting to Respawn Point in 10…0 sec.`，相邻边界切换成 `Respawn in 22…0 sec.／Waiting to be respawned`，最后技能栏恢复。正式裁图库为第一阶段新增 `siege_auto_teleport_countdown` 的 `10／0 秒`两图，并为第二阶段补入英文 `20／1 秒`；后者使 `siege_revive_countdown` 扩到九个代表数值。

两类裁图都只能用于区分旧攻城死亡阶段和数值变化；必须联合父帧环境、死亡文案是否消失以及可操作 HUD。录像时间与画面倒计时并非严格一比一，疑似经过加速，任何显示值都不能转换成硬编码睡眠时长。全部 11 张相关裁图都标为 `PIONEER-A`，禁止混入 TEST-B／国服训练与模板集。

### 3.10 TEST-B 十人副本死亡等待

[Twitch Clip 父帧](../../research/evidence/video/twitch-clip-test-b-raid-dead-wait-g93cchbtrszole42/manifest.json)补出十人副本个人死亡后的持续等待态：主画面变暗、常规技能栏消失，底部中央显示复活标志与“等待复活”，队友和 Boss 战仍继续。裁图已排除主播立绘、聊天、技术测试横幅、UID 和队伍栏。

该 Clip 从死亡后开始、在复活前结束，因此它只把 `DungeonDeadWait` 从五人本交叉验证到十人本，不能补足死亡触发、复活邀请、野外复活选项或恢复 HUD 边界。

### 3.11 TEST-B 精灵之塔楼层与里程碑奖励

[阿土 `2804721854` 的四帧 Manifest](../../research/evidence/video/twitch-vod-2804721854/manifest.json)在同一页面先同时显示普通未通关、黄色选中未通关和绿色已通关勾；这三张楼层裁图建立状态字典，但同屏共存本身不证明任何一次挑战结果。

荣誉榜弹层随后给出可复核的领取链：`17662.25s` 第 20 层奖励为橙色可领格，`17662.75s` 同格变为绿色勾；`17663.50s` 第 30 层也由橙色变绿，并出现“宠物蛋 ×3”到账提示。两张正式奖励裁图特意使用同一坐标，只标记通用的 `claimable_orange_item_tile → claimed_green_check_tile`；层数、奖励名称和到账提示留在父帧，不能把裁图误标成固定“第 30 层宠物蛋”模板。

### 3.12 PIONEER-A 十人本队友复活与资源变化

[印尼语十人本六帧 Manifest](../../research/evidence/video/pioneer-ten-player-revive-bv1d4t8zseqw/manifest.json)把旧副本队友复活补成连续可核对链：存活时左侧显示 `Kesempatan Respawn: 2`；死亡后画面变暗、技能栏消失并出现蓝色十字 `SOS`；约 69 秒后出现带头像、时限条、`Tolak／Setuju` 的队友邀请；指针移到 `Setuju` 后相邻 0.1 秒帧恢复战斗 HUD，随后显示“已由 Hroar 复活”且次数变成 `1`。

五张新裁图分别保存 SOS、印尼语邀请弹窗、同坐标的 `2／1` 和成功提示。按钮没有观察到可稳定分离的悬停或按下外观，故没有伪造 hover／pressed 样本；指针帧只留在 Manifest 作转换上下文。次数 `2→1`说明接受复活可能消耗有限资源，但录像不能确定资源是个人、队伍、Boss 还是难度共享。全部五图标为 `PIONEER-A`，既不进入 TEST-B／国服模板，也不授权自动接受队友邀请。

### 3.13 TEST-B 配方解锁与制作材料不足

[绿色药水制作六帧 Manifest](../../research/evidence/video/life-crafting-bv1d67v6pemq/manifest.json)来自已登记巴哈姆特实机的另一 Bilibili 转载；它与既有生活采矿来源指向同一段原始 YouTube，所以不冒充独立交叉佐证。对 `948.0–970.0s` 追加 220 张 0.1 秒帧后，补出：

```text
selected_locked_unlockable
→ awaiting_choice_cost_1000
→ green_potion_unlocked
→ selected_unlocked + craft_available_gold
→ pointer_on_craft_button
→ item_shortage_traditional_chinese
```

七张裁图保存同坐标锁定／解锁行、解锁／制作主动作、确认框、成功覆盖层和“所需消耗的道具不足，无法制造！”提示。制作前后右上活力均为 `700/5000`，远高于单次可见消耗 `20`；因此该分支可以明确归类为材料／道具不足，而不是活力不足。它同时证明金色制作按钮不能作为“材料足够”判据。录像没有输入日志，指针帧只建立 0.1 秒动作边界；解锁与制作仍是资源事务，默认保留人工门。

### 3.14 TEST-B 成长徽章领取、重排与已完成

[成长徽章四帧 Manifest](../../research/evidence/video/growth-badge-bv1d67v6pemq/manifest.json)对 `1118–1138s` 检查 201 张 0.1 秒采样，并把领取边界收紧到原生 `1121.754→1121.787s`：

```text
tracker.claimable
→ 天赋总等级达到120级 126/120 + 金色领取，晋升任务 1/7
→ 相邻原生帧：原行移除、列表重排、晋升任务 2/7
→ 下滚：同任务 120/120 + 绿色已完成
```

六张裁图保存入口可领取、任务行蓝色前往／金色领取／绿色已完成，以及同坐标晋升计数 `1/7／2/7`。原领取坐标在成功后立即被下一条任务的蓝色前往复用，证明固定坐标连点不安全；右侧入口在领取后仍显示可领取，也不能作为单行成功判据。客户端字面是“已完成”，不是“已领取”；`126/120→120/120`更可能是完成态封顶显示，不能解释成天赋属性下降。没有奖励到账 toast／背包账本，也没有稳定 hover／pressed 外观，因此只建立页面事务，不授权自动领取。

### 3.15 TEST-B 职业天赋二选一与锁定正交态

[职业天赋九帧 Manifest](../../research/evidence/video/talent-profession-bv1d67v6pemq/manifest.json)按原生帧复核 `1036–1066s`，建立：

```text
GreyQuestionLocked
→ GoldQuestionSelected + 启用
→ 请选择职业天赋（双分支／四能力）
→ SameOptionWhite → SameOptionGold + 确定
→ TreeReturnedWithChoiceIcon
→ ChoiceIcon + PercentBadge 稳定激活
```

九张裁图中，职业节点三态严格使用同一坐标，能力普通／选中也使用同一坐标；选择确认后先返回树，再等待 `%` 子能力徽标和属性正增量稳定，避免把过渡帧当成功。另一父帧与独立页签裁图直接显示 `II+-1` 黄色选中时锁图标仍保留、整树为灰色 `0/10`、底部是条件提示而非升级按钮，因此 selected 与 locked 必须作为独立维度。构筑选择和升级会改变角色状态／资源，录像无输入日志且技能小字低清，默认只作离线状态字典与国服采样种子。

## 4. 只有父帧、尚未裁成正式样本的视觉种类

以下内容能在 175 张视频父帧中定位，但没有进入 70 键／130 图的正式裁图库：

- 挂机魔物头像、普通品质标签、AutoOn HUD 候选、技能分类／技能行／热键冷却；
- 采矿交互、4.5 秒进度条、拾取／活力／熟练度提示；
- 园艺师未选择态、配方职业等级锁、材料真正足够和活力不足；绿色药水可解锁锁态／解锁态与材料不足已入正式裁图库；
- 宠物孵化房、品质概率、主战／支援／助战槽、星级、技能类型；
- 精炼材料、多个公会活动卡片；
- GSTAR-2024 韩文 Boss 场“原地复活”覆盖层与 HUD 恢复四帧；来源仅 852×480、含官方舞台直播合成区且构建早于 PIONEER-A，故只作流程语义与负例，不生成当前模板；
- 五人本个人死亡父帧、团灭再战、胜利奖励、团队拍卖；十人本死亡等待已有独立裁图；
- 自动挂机地形卡位场景序列。

“父帧中能看到”不等于“已有独立图标文件”。需要作为识别资产使用时，仍应按当前 schema 单独裁切、标注污染和验证像素。

2026-07-28 又逐张查看巴哈五个重点主题的 39 个原图引用（包含跨帖重复图）。这些图只增加宠物、精炼、商城、普通战斗、主线对话、外观和座谈语境；没有画面支持“卡片／灵魂残响接近满载”、疲劳状态、真正满包、野外死亡或公会终局，因此该轮零图入库。第 84 张裁图来自 Twitch 耗尽页同步奖励通知；第 85 张来自后续长评定点回看，直接补到“装运商队 `4/4`”进行中；第 86、87 张分别保存第四批载货 `4/8` 发车禁用和 `5/8` 发车可用。第 88 张是同一长评中另行逐 0.1 秒复核得到的生存竞争模式队友复活弹窗，只扩充竞技负例分类。第 89–94 张来自 `2805774434`：依次保存启动器、公告就绪、服务器入口、TEST-B 角色选择、95% 载入和自订布局编辑器；开放世界只保留父帧作页面链后置状态。第 95–99 张来自 `2804721854`：普通未通关、黄色选中未通关、绿色已通关勾，以及同坐标的里程碑奖励橙色可领格／绿色已领勾。第 100–103 张来自英文旧攻城录像：自动传送 `10／0 秒`及后续复活等待 `20／1 秒`。第 104–108 张来自印尼语旧十人本：SOS、队友邀请、次数 `2／1`和成功提示；第 109–115 张来自 TEST-B 绿色药水精抽；第 116–121 张来自成长徽章精抽；第 122–130 张来自职业天赋精抽，保存节点三态、能力普通／选中、启用／确认、选择弹层和选中仍锁定页签。第 100–108 张严格属于 PIONEER-A，后 22 张重新回到 TEST-B，两个构建不混用。

## 5. 当前仍缺的图标／状态变体

不能从其他 RO 产品或生成式图片补齐：

- 呆呆委托：接取、寻路、子目标进度、交付、最终完成、阻断；
- 成长徽章：已有单任务领取→行移除→晋升计数增加→已完成；仍缺奖励到账账本、入口可领取清空、整阶段 `7/7`／晋升、领取失败与背包满，且“已完成”不能冒充其他页面“已领取”；
- 天赋：已有同节点锁定→可启用→二选一→稳定激活及选中仍锁定页签；仍缺取消、返回不选、重置／改选确认与成本、点数不足、升级失败、满级、方案切换和国服高清文案；
- 公会商队：已有库存不足 `0/6` 行、购买／求助入口、`4/4` 进行中及 `4/8` 禁用 → `5/8` 发车可用；仍缺选中不足项后的禁用／失败、购买价格与结果、求助结果、发车确认／成功／失败及第四批终局；每日 `1/1 已完成`已有裁图但与四批关系未知；
- 生活：已有同配方锁定→解锁、确认、成功和材料不足；仍缺一次真正制作成功及材料／活力／产物账本、批量制作、`80/100`、即时 `100/100`、活力不足、满包、节点被抢／消失和采集中断；
- 精灵之塔：已有楼层普通／选中／已通关及奖励可领／已领；仍缺锁定／禁用、挑战前后、失败／结算、次数／重置、扫荡、领取失败和满包分支；
- 挂机：低倍、疲劳、无目标、自动停止、卡位恢复；
- 背包／药品：接近满、真正满、掉落暂存／丢失、仓库满、药品 `1 → 0`；
- 野外死亡：费用、复活选项、落点、保护状态和 AutoOn 保留／关闭；
- 连接：TEST-B 已有启动器就绪、公告就绪、单服入口、角色选择、17%／95% 载入，以及重连中、双按钮失败和重新登录要求；仍缺账号认证、补丁／版本不符、选服／排队／维护／满员、输入可见的转换结果、开放世界原点与 Auto 状态保留；
- 角色：TEST-B 已有单角色最近选中＋新建空位，PIONEER-A 有三角色语义样本；仍缺国服角色页，以及 TEST-B／国服创建、删除确认、默认焦点、上限／翻页和多角色边界；
- 布局：已有自订布局编辑器入口与可拖移说明；仍缺拖移、保存、取消、恢复预设、重启持久化及 DPI／缩放矩阵；
- 国服简体中文下所有普通、悬停、按下、选中、锁定、可领、已领和禁用变体。

在上述状态补齐前，130 张图片适合做离线分类、差异比较和国服采样种子；它们不能独立授权真实客户端动作。
