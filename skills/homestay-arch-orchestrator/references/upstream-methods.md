# 外部方法与许可

核验日期：2026-10-28。以下为已经阅读相关段落并实际改写到本套技能中的方法。来源仓库的角色提示词、宿主协议、默认审批和工具名称不作为本套执行指令。

## 采用位置

| 标识 | 仓库及固定提交 | 方法 | 本套位置 | 许可 |
|---|---|---|---|---|
| GH-A | [AlpacaLabsLLC/skills-for-architects · 78a175716237](https://github.com/AlpacaLabsLLC/skills-for-architects/tree/78a17571623708acb31984655a5df873c88bb734) | 环境与到达分析、逐空间面积、同范围数量对账 | homestay-arch-site、program、siteplan、circulation、coordination、delivery | [MIT](licenses/GH-A.txt) |
| GH-B | [Abhinavbwj/Skills-Architects · 30a0845dddca](https://github.com/Abhinavbwj/Skills-Architects/tree/30a0845dddcaebd765fc396059573d02e99c5b63) | 邻接矩阵、房间数据表、空间组织、方案比选及围护控制层 | homestay-arch-program、massing、guestrooms、public-spaces、back-of-house、circulation、envelope | [MIT](licenses/GH-B.txt) |
| GH-C | [constructelligence-lab/construction-agent-skills · f05ffdf70b65](https://github.com/constructelligence-lab/construction-agent-skills/tree/f05ffdf70b650582a4a12181d6fedcc9b3ae56f1) | 按后期修复影响排序的可建造性问题、区分真实冲突与模型误差、责任答复与复查 | homestay-arch-sections、envelope、coordination | [CC BY 4.0](licenses/GH-C.txt) |
| GH-D | [mohitagw15856/pm-claude-skills · 4391fb006db1](https://github.com/mohitagw15856/pm-claude-skills/tree/4391fb006db13fe898f40a897bc369337a64e4e5) | 从活动形成任务书、早期面积投资对照、将场地约束转为设计后果 | homestay-arch-brief、site、program、public-spaces | [MIT](licenses/GH-D.txt) |
| GH-E | [nbharathik/ifc-skills · 5b52282c3e14](https://github.com/nbharathik/ifc-skills/tree/5b52282c3e1423dd6172044d504c6fcc3aa0798c) | 模型schema/单位/坐标检查、GlobalId对象追踪、区分数量来源与只读查询 | project-contract、homestay-arch-coordination、delivery | [MIT](licenses/GH-E.txt) |

## 改写说明

- 用中文重写为民宿建筑阶段任务，连接经营、客房、公区、后勤及建筑交付。
- 外部的固定面积、比例、法规阈值和地区限定示例没有导入；项目运行时核实适用依据。
- IFC仅作为可选输入的处理约定，未捆绑或安装IfcOpenShell，也未宣称已实现模型解析或自动碰撞。
- GH-C的方法改写位置为sections/envelope/coordination的可建造性与专业冲突说明；已调整为问题、依据、责任回复及复查，不复制统一让位规则或施工身份设定。

## 署名与许可

GH-A：Alpaca Labs, LLC；GH-B：Abhinav Bhardwaj；GH-D：Mohit Aggarwal；GH-E：Bharathi Kannan N。MIT许可及版权声明保留在上表链接文件中。

GH-C内容源自Constructelligence，仓库与固定提交见上表，按[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)署名使用；已将相关方法改写为上述中文检查流程。原许可说明见[GH-C.txt](licenses/GH-C.txt)。这些改写部分按CC BY 4.0提供。外部作者不为本套项目背书。
