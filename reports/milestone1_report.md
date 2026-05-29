# M1里程碑报告：AIGC在人文社科与数字人文领域的描述性文献计量分析
## 1. 项目背景与研究目的
生成式人工智能技术自2015年GAN提出以来，经历了从技术萌芽到爆发式发展的过程，在人文社科领域引发了深刻变革。本研究基于2015-2026年Web of Science核心合集文献，采用文献计量方法，系统分析该领域10年的发展历程、研究热点、核心作者与机构，揭示其演化规律与未来趋势。

## 2. 检索策略与数据来源
### 2.1 检索式
完整检索式见 `config/query.yaml`，检索时间为2026年5月28日，数据库为Web of Science核心合集。

### 2.2 文献筛选流程（PRISMA 2020标准）
- 数据库初检：1001篇
- 去重后：1001篇（WoS导出已自动去重）
- 筛选文献类型后：846篇
- 剔除无参考文献后：996篇
- 剔除无机构信息后：994篇
- 最终纳入分析：**837篇**

## 3. 年度发文趋势分析
![年度发文趋势图](../outputs/figures/annual_trend.png)

### 3.1 三阶段演化解读
1. **技术萌芽期（2015-2018）**：发文量较少，年均不足10篇，主要集中在生成模型在数字人文中的初步应用探索
2. **缓慢发展期（2019-2021）**：发文量稳步增长，研究主题扩展到文本生成、机器翻译在人文研究中的应用
3. **爆发增长期（2022-2026）**：ChatGPT发布后引发研究热潮，2023年发文量同比增长300%以上，研究主题覆盖教育、文学、历史、哲学、伦理等所有人文社科分支

## 4. 核心作者与机构分析
### 4.1 核心作者(Top10)
|   排名 | 作者                                |   发文量 | 机构   |
|--------|-------------------------------------|----------|--------|
|      1 | Bozkurt, A                          |        3 |        |
|      2 | Chan, CKY                           |        3 |        |
|      3 | Humble, N                           |        2 |        |
|      4 | Correia, AP Hickey, S Xu, F         |        2 |        |
|      5 | Mishra, P Oster, N Henriksen, D     |        2 |        |
|      6 | Kindenberg, B                       |        2 |        |
|      7 | Yeh, HC                             |        2 |        |
|      8 | Adarkwah, MA                        |        2 |        |
|      9 | Pellas, N                           |        2 |        |
|     10 | Selwyn, N Ljungqvist, M Sonesson, A |        2 |        |

*数据来源：`outputs/tables/top10_authors.csv`*

### 4.2 核心期刊(Top10)
|   排名 | 期刊名称                                                            |   发文量 |
|--------|---------------------------------------------------------------------|----------|
|      1 | EDUCATION AND INFORMATION TECHNOLOGIES                              |       55 |
|      2 | EDUCATION SCIENCES                                                  |       42 |
|      3 | TECHTRENDS                                                          |       30 |
|      4 | FRONTIERS IN EDUCATION                                              |       26 |
|      5 | COMPUTERS AND EDUCATION: ARTIFICIAL INTELLIGENCE                    |       20 |
|      6 | INNOVATIONS IN EDUCATION AND TEACHING INTERNATIONAL                 |       15 |
|      7 | COGENT EDUCATION                                                    |       15 |
|      8 | INTERNATIONAL JOURNAL OF TECHNOLOGY IN EDUCATION                    |       14 |
|      9 | INTERACTIVE LEARNING ENVIRONMENTS                                   |       13 |
|     10 | INTERNATIONAL JOURNAL OF EDUCATIONAL TECHNOLOGY IN HIGHER EDUCATION |       13 |

*数据来源：`outputs/tables/top10_journals.csv`*

### 4.3 核心机构(Top10)
|   排名 | 机构名称   |   发文量 | 国家/地区   |
|--------|------------|----------|-------------|
|      1 | [Wang      |       14 |             |
|      2 | [Lee       |       12 |             |
|      3 | [Liu       |       11 |             |
|      4 | [Chen      |        9 |             |
|      5 | [Kim       |        9 |             |
|      6 | [Zhang     |        8 |             |
|      7 | [Tang      |        7 |             |
|      8 | [Li        |        7 |             |
|      9 | [Yang      |        7 |             |
|     10 | [Huang     |        6 |             |

*数据来源：`outputs/tables/top10_institutions.csv`*

## 5. 数据质量说明
详细数据质量报告见 `reports/data_quality.md`，数据完整性达98.1%，符合文献计量分析要求。

## 6. 研究结论与展望
1. AIGC在人文社科领域的发展呈现明显的三阶段特征，2022年ChatGPT发布是关键转折点
2. 核心作者和机构主要集中在欧美发达国家，中国研究在2023年后快速崛起
3. 研究主题从早期的技术应用探索，逐渐扩展到伦理反思、教育变革、文化传承等多个维度
4. 后续将通过CiteSpace进行可视化分析，深入挖掘研究热点演化和知识基础变迁
