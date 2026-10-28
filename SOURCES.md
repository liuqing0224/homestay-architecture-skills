# GitHub方法融入记录

核验日期：2026-10-28。共5个来源仓库，读取13份Skills的相关章节及5份许可证。提交与文件哈希固定在[source-register.json](source-register.json)。

| 来源 | 采用内容 | 融入位置 | 许可 |
|---|---|---|---|
| [AlpacaLabsLLC/skills-for-architects](https://github.com/AlpacaLabsLLC/skills-for-architects/tree/78a17571623708acb31984655a5df873c88bb734) | 环境与到达分析、逐空间面积、同范围数量对账 | homestay-arch-site、program、siteplan、circulation、coordination、delivery | MIT |
| [Abhinavbwj/Skills-Architects](https://github.com/Abhinavbwj/Skills-Architects/tree/30a0845dddcaebd765fc396059573d02e99c5b63) | 邻接矩阵、房间数据表、空间组织、方案比选及围护控制层 | homestay-arch-program、massing、guestrooms、public-spaces、back-of-house、circulation、envelope | MIT |
| [constructelligence-lab/construction-agent-skills](https://github.com/constructelligence-lab/construction-agent-skills/tree/f05ffdf70b650582a4a12181d6fedcc9b3ae56f1) | 按后期修复影响排序的可建造性问题、区分真实冲突与模型误差、责任答复与复查 | homestay-arch-sections、envelope、coordination | CC BY 4.0 |
| [mohitagw15856/pm-claude-skills](https://github.com/mohitagw15856/pm-claude-skills/tree/4391fb006db13fe898f40a897bc369337a64e4e5) | 从活动形成任务书、早期面积投资对照、将场地约束转为设计后果 | homestay-arch-brief、site、program、public-spaces | MIT |
| [nbharathik/ifc-skills](https://github.com/nbharathik/ifc-skills/tree/5b52282c3e1423dd6172044d504c6fcc3aa0798c) | 模型schema/单位/坐标检查、GlobalId对象追踪、区分数量来源与只读查询 | project-contract、homestay-arch-coordination、delivery | MIT |

## 文件到方法

### GH-A · AlpacaLabsLLC/skills-for-architects

- [skills/environmental-analysis/SKILL.md](https://github.com/AlpacaLabsLLC/skills-for-architects/blob/78a17571623708acb31984655a5df873c88bb734/skills/environmental-analysis/SKILL.md)：site执行3及场地专题：地理/统计期/原始来源和未核实事项。
- [skills/mobility-analysis/SKILL.md](https://github.com/AlpacaLabsLLC/skills-for-architects/blob/78a17571623708acb31984655a5df873c88bb734/skills/mobility-analysis/SKILL.md)：site执行4、siteplan及circulation：到达方式与末段服务联系。
- [skills/schedule-quantity-reconcile/SKILL.md](https://github.com/AlpacaLabsLLC/skills-for-architects/blob/78a17571623708acb31984655a5df873c88bb734/skills/schedule-quantity-reconcile/SKILL.md)：coordination执行5及检查表：同范围、修订、单位、重复/缺失与零值区分。
- [skills/workplace-programmer/SKILL.md](https://github.com/AlpacaLabsLLC/skills-for-architects/blob/78a17571623708acb31984655a5df873c88bb734/skills/workplace-programmer/SKILL.md)：program执行2—3：数量、单元面积、口径与余量；改为民宿空间与人数口径。
### GH-B · Abhinavbwj/Skills-Architects

- [skills/building-envelope/SKILL.md](https://github.com/Abhinavbwj/Skills-Architects/blob/30a0845dddcaebd765fc396059573d02e99c5b63/skills/building-envelope/SKILL.md)：envelope执行3及围护检查：控制层与窗、屋面、门槛交接，不采用数值表。
- [skills/building-programming/SKILL.md](https://github.com/Abhinavbwj/Skills-Architects/blob/30a0845dddcaebd765fc396059573d02e99c5b63/skills/building-programming/SKILL.md)：program邻接矩阵及guestrooms房型数据表：空间关系与实例，不采用原面积配比。
- [skills/concept-design/SKILL.md](https://github.com/Abhinavbwj/Skills-Architects/blob/30a0845dddcaebd765fc396059573d02e99c5b63/skills/concept-design/SKILL.md)：massing：同任务范围的候选、场地响应与解释选择理由。
- [skills/spatial-planning/SKILL.md](https://github.com/Abhinavbwj/Skills-Architects/blob/30a0845dddcaebd765fc396059573d02e99c5b63/skills/spatial-planning/SKILL.md)：circulation寻路节点、public-spaces和back-of-house关系检查。
### GH-C · constructelligence-lab/construction-agent-skills

- [skills/constructability-risk-review/SKILL.md](https://github.com/constructelligence-lab/construction-agent-skills/blob/f05ffdf70b650582a4a12181d6fedcc9b3ae56f1/skills/constructability-risk-review/SKILL.md)：sections问题交接、envelope施工维护、coordination可建造性问题排序。
- [skills/mep-coordination-clash-triage/SKILL.md](https://github.com/constructelligence-lab/construction-agent-skills/blob/f05ffdf70b650582a4a12181d6fedcc9b3ae56f1/skills/mep-coordination-clash-triage/SKILL.md)：coordination执行3、6及冲突表：真冲突/模型误差、责任决策与复查。
### GH-D · mohitagw15856/pm-claude-skills

- [plugins/pm-architecture/skills/architectural-programme-brief/SKILL.md](https://github.com/mohitagw15856/pm-claude-skills/blob/4391fb006db13fe898f40a897bc369337a64e4e5/plugins/pm-architecture/skills/architectural-programme-brief/SKILL.md)：brief执行1、4、5：活动优先、预算范围与显式排除事项。
- [plugins/pm-architecture/skills/site-analysis-report/SKILL.md](https://github.com/mohitagw15856/pm-claude-skills/blob/4391fb006db13fe898f40a897bc369337a64e4e5/plugins/pm-architecture/skills/site-analysis-report/SKILL.md)：site执行2、5：区分现状与建设条件、约束到设计后果。
### GH-E · nbharathik/ifc-skills

- [skills/ifc/SKILL.md](https://github.com/nbharathik/ifc-skills/blob/5b52282c3e1423dd6172044d504c6fcc3aa0798c/skills/ifc/SKILL.md)：共享约定与coordination的IFC检查：schema、独立单位、对象映射和量的来源。

## 使用方式

采用的是已核对的工作方法，经中文重写后融入阶段步骤、表单字段及验收条件。外部仓库代码未执行，未安装其宿主插件，也未将外部AGENTS或提示词当作本项目指令。地区规范数值、面积配比及固定性能阈值没有导入。

本机既有民宿、自建房、室内及校审Skills用于核对职责和设计交接；新套件以`homestay-arch-*`命名。具体衔接见[阶段与交接](skills/homestay-arch-orchestrator/references/routing-and-handoffs.md)。

许可证、署名与已改写部分见[第三方说明](THIRD_PARTY_NOTICES.md)。
