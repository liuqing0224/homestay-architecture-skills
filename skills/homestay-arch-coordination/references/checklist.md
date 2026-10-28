# 专业与成本协调检查表

## 冲突与可建造性（GH-C改写）

记录issue_id、model/drawing_revision、object_ids、location、conflict_type、evidence、late_fix_consequence、proposed_options、decision_owner、required_reply、recheck_status。优先处理会造成大范围返工的接口；不照搬统一的“谁必须让谁”。

## 数量对账（GH-A改写）

比较键至少包含对象/类型、楼栋、楼层、阶段、方案、修订与单位。保留两边原始行和定位；明确汇总规则后才聚合。不把缺项、未知量和实际零值合并，不默认模糊名称是同一对象。

## 有IFC输入时（GH-E改写）

先确认实际可用工具，读取schema、项目/单项数量的单位及楼层、放置/坐标关系。以GlobalId结合模型文件修订追踪对象；记录量来自Qto、Pset还是几何计算。不同来源不一致时并列报告，不强选一个“真值”。

只读提取即可满足的任务不改模型。需要修改时按本次授权另存新修订、重开核对，保留原文件；IfcOpenShell未安装或文件不支持时列明工具缺口，不声称完成提取、碰撞或修复。

外部方法标识：GH-A、GH-C、GH-E。采用位置、改写说明和许可见[方法来源](../../homestay-arch-orchestrator/references/upstream-methods.md)。
