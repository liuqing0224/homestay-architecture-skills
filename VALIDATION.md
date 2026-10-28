# 验证记录

日期：2026-10-28。

| 检查 | 实际结果 | 证据 |
|---|---|---|
| 官方技能格式 | 15/15通过 | [package.json](validation/package.json) |
| 发现信息 | 15项名称、描述、默认调用与长度检查通过 | [package.json](validation/package.json) |
| 技能内部引用 | 51处有效且位于套件内 | [package.json](validation/package.json) |
| 公开文档链接 | 以本次发布检查记录为准，目标均在公开文件集合内 | [链接检查](validation/document-links.json) |
| 来源与许可 | 5个固定提交、13份技能文件记录、5份原许可证字节核对通过 | [来源台账](source-register.json)及[package.json](validation/package.json) |
| 安装器行为 | 10项测试通过 | [测试输出](validation/installer-tests.txt)及[运行记录](validation/installer-tests.json) |
| 实际安装 | 15项、53文件与主版本字节一致 | 本机安装记录本地留存 |
| 既有相关技能 | 7个目录安装前后字节清单一致 | 本机目录核对记录本地留存 |
| 内容审阅 | 按关键输入与交接问题检查职责说明 | [审阅记录](validation/content-review.md) |

10项安装测试覆盖：试运行无写入、整套安装与检查、同名冲突阻止部分安装、修改/多余文件检测、源/目标符号链接拒绝、复制失败清理、失败时保留其他技能，以及目录与清单不一致阻断。

内容审阅检查的是指令覆盖；官方格式、引用和安装测试不验证建筑设计判断。本次未执行完整民宿设计或IFC处理。
