# 数据说明
## 数据来源
- 数据库：Web of Science Core Collection
- 检索日期：2026年5月28日
- 时间范围：2015-01-01 至 2026-4-30
- 检索式版本：v3.0

## 文件说明
- `raw/savedrecs_full.txt`：WoS导出的原始数据（1001篇）
- `processed/parsed.csv`：解析后的结构化原始数据
- `processed/final.csv`：清洗后的最终分析数据（837篇）
- `processed/wos_for_citespace.txt`：CiteSpace专用格式文件（837篇，100%保留原始格式）

## 数据清洗流程
1. 文献类型筛选：仅保留Article和Review Article
2. 去重：基于WoS唯一标识符UT去重
3. 完整性检查：剔除无参考文献和无机构信息的文献
4. 字段标准化：统一作者、机构名称格式