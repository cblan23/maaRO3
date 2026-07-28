# MaaFramework Schema 快照

本目录的四个 Schema 从 MaaFramework 官方仓库下载，用于在没有 RO3 客户端时校验工程骨架。

- 上游仓库：<https://github.com/MaaXYZ/MaaFramework>
- 固定提交：[`25dff4c98eacadd6328685858f8981b52f3b56e2`](https://github.com/MaaXYZ/MaaFramework/commit/25dff4c98eacadd6328685858f8981b52f3b56e2)
- 上游提交时间：2026-07-19
- 本地同步日期：2026-07-26

包含：

- `interface.schema.json`
- `interface_config.schema.json`
- `interface_import.schema.json`
- `pipeline.schema.json`

更新时必须同时记录新的上游提交，并重新运行：

```powershell
py -3 tools/validate_schema.py `
  --schema-dir deps/tools `
  --resource-dirs assets/resource `
  --interface-files assets/interface.json
```
