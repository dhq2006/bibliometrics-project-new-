# CiteSpace参数记录
## 基础设置
- 软件版本：CiteSpace 6.4.2 Basic（免费版）
- 数据来源：data/processed/wos_for_citespace.txt
- 文献数量：837篇
- 时间范围：2015-2026
- 时间切片长度：1年
- 节点标签显示：前35个高频节点
- 数据来源：Web of Science
- 文本处理：默认设置

## 各图谱详细参数
### 1. 关键词共现图谱
- 节点类型：Keyword
- TopN per slice：35
- 阈值设置：g-index, k=24（适配免费版300节点限制）
- 聚类方法：Modularity算法
- 剪枝策略：Pathfinder + Pruning sliced networks
- 结果指标：
  - 节点数：251
  - 边数：269
  - 网络密度：0.00866
- 可视化设置：
  - 节点大小：频次
  - 节点颜色：首次出现年份（2015-2026渐变）
  - 标签阈值：4

### 2. 机构合作图谱
- 节点类型：Institution
- TopN per slice：25
- 阈值设置：g-index, k=20（适配免费版300节点限制）
- 剪枝策略：Pathfinder + Pruning sliced networks
- 结果指标：
  - 节点数：187
  - 边数：213
  - 网络密度：0.0122
  - 连通分量数：76
- 可视化设置：
  - 节点大小：发文量
  - 节点颜色：首次出现年份
  - 标签阈值：5

### 3. 参考文献共被引图谱
- 节点类型：Cited Reference
- TopN per slice：30
- 阈值设置：g-index, k=25（适配免费版300节点限制）
- 聚类方法：LSI潜在语义索引
- 剪枝策略：Pathfinder + Pruning sliced networks
- 结果指标：
  - 节点数：224
  - 边数：317
  - 网络密度：0.0127
- 可视化设置：
  - 节点大小：被引频次
  - 节点颜色：首次被引年份
  - 标签阈值：10

## 说明
所有参数均已适配CiteSpace 6.4.2免费版的300节点限制，在保证分析质量的前提下，最大限度保留了核心信息。Modularity Q值和Silhouette值因免费版节点数限制未自动计算，但网络结构和核心分析结果不受影响。