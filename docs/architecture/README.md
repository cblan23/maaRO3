# 未来架构边界

参考 `D:\vscode\maaKES` 后，maaRO3 计划复用其“控制面 + Maa 执行壳 + 运行时配置编译 + 独立 Agent + 结构化观测”骨架，不复制 KES 的卡牌、地图和巨型平面路由业务。

预计分层：

```text
UI / Maa interface
  -> Runner 控制面
    -> 不可变 RunSpec
      -> AutomationEngine
        -> 分层场景路由
          -> 小型声明式 Pipeline
          -> Python Agent 的有状态策略
```

开放世界任务应拆成：全局安全、登录/连接、主页/菜单、任务导航、野外挂机、生活玩法、奖励与恢复等上下文路由。每次动作都需要后置验证；未知画面默认停止点击并保存证据。

当前仅保留边界说明，不创建 RO3 Pipeline 或业务 Agent。

详细版本已整理到：

- [`../design/architecture.md`](../design/architecture.md)：模块、RunSpec、场景路由、动作事务、数据存储与测试；
- [`../design/roadmap.md`](../design/roadmap.md)：测试前、8 月采样、离线识别和条件式授权阶段；
- [`../design/compliance_gate.md`](../design/compliance_gate.md)：当前必须保持 `OFFLINE_RESEARCH` 的硬门。
