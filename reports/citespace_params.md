# CiteSpace参数记录
## 基础设置
- 软件版本：CiteSpace 6.4.2
- 数据来源：data/processed/wos_for_citespace.txt
- 时间范围：2015-2026
- 时间切片长度：1年
- 节点标签显示：前35个高频节点

## 各图谱详细参数
### 1. 关键词共现图谱
- 节点类型：Keyword
- TopN per slice：35
- 阈值设置：g-index, k=24
- 聚类方法：Modularity算法
- 剪枝策略：Pathfinder + Pruning sliced networks
- 结果指标：Modularity Q=XXX, Silhouette=XXX
- 可视化设置：节点大小=频次，颜色=首次出现年份（2015-2025渐变）

### 2. 机构合作图谱
- 节点类型：Institution
- TopN per slice：25
- 阈值设置：g-index, k=20
- 剪枝策略：Pathfinder + Pruning sliced networks
- 结果指标：网络密度=XXX，连通分量数=XXX

### 3. 参考文献共被引图谱
- 节点类型：Cited Reference
- TopN per slice：30
- 阈值设置：g-index, k=25
- 聚类方法：LSI潜在语义索引
- 剪枝策略：Pathfinder + Pruning sliced networks
- 结果指标：Modularity Q=XXX, Silhouette=XXX
