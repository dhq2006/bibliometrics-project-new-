👥 团队信息
表格
姓名	角色	主要职责
董恒清	组长	统筹协调、项目管理与最终成果审核
温明辉	成员	文献检索策略制定、数据采集与预处理（检索式构建、数据导出与清洗）
杨永康	成员	文献筛选流程设计、PRISMA 报告撰写与研究空白分析
马子雄	成员	数据质量评估、图数据模型构建与数据清洗规则制定
职明东	成员	计量分析指标定义、知识图谱可视化与最终报告撰写及汇报
🎯 研究方向
本项目聚焦于 ** 生成式人工智能（AIGC）** 在人文社科与人文计算领域的应用态势与发展趋势，旨在通过文献计量学与知识图谱分析方法，系统梳理该领域的研究热点、核心技术演进路径、关键研究团队与机构合作网络，揭示其在人文社科各学科中的应用模式与未来发展方向。
📅 项目计划
第一阶段：数据准备与方案确立 (M1)
目标：完成高质量数据集的构建与研究方案的最终确定
关键任务：
精准检索：基于 WOS 核心合集，构建并优化检索式，确保查全率与查准率
数据采集：导出包含作者、机构、关键词、参考文献等核心字段的文献数据
质量评估：完成数据质量报告，分析缺失率、重复率等关键指标
筛选流程：制定并执行三阶段文献筛选流程
第二阶段：计量分析与可视化 (M2)
目标：完成核心计量分析并生成可视化知识图谱
关键任务：
数据清洗：执行作者、机构、关键词的消歧与标准化处理
指标计算：计算年度发文量、作者 / 机构合作网络、关键词共现等核心指标
网络构建：构建文献共被引网络、作者合作网络等知识图谱
可视化呈现：使用 VOSviewer/CiteSpace 等工具生成科学知识图谱
第三阶段：成果整合与汇报 (M3)
目标：完成最终研究报告与学术汇报
关键任务：
结果解读：深入分析可视化结果，总结研究热点、演化趋势与关键发现
报告撰写：撰写包含研究背景、方法、结果与讨论的完整学术报告（Mini Review）
可复现性优化：确保项目代码、数据与文档的版本化管理，实现研究可复现
汇报准备：制作学术汇报 PPT，准备汇报
📊 数据说明
原始数据：Web of Science 核心合集导出 savedrecs_full.txt（1001 篇，2015-2026）
最终纳入数据：837 篇（筛选期刊文章 / 综述，剔除纯技术文献）
数据格式：WoS 原生 txt 格式（CiteSpace 兼容）、标准 CSV 格式（Python 分析用）
数据质量：完整性 99.3%，一致性 100%，人工抽样验证准确率 99.5%
🛠️ 分析工具
数据处理：Python 3.12 + pandas
文献计量分析：CiteSpace 6.4.2
可视化：CiteSpace + matplotlib
版本控制：Git + GitHub
📁 文件结构
plaintext
bibliometrics-project/
├── config/                 # 配置文件
│   ├── query.yaml          # 最终版检索式配置
│   ├── synonyms.yaml       # CiteSpace同义词合并规则
│   └── query_changelog.md  # 检索式迭代记录
├── data/                   # 数据文件
│   ├── raw/                # 原始WoS数据
│   │   └── savedrecs_full.txt
│   ├── processed/          # 处理后数据
│   │   ├── parsed.csv      # 解析后的结构化数据
│   │   ├── final.csv       # 清洗后的最终分析数据
│   │   └── wos_for_citespace.txt  # CiteSpace专用格式文件
│   ├── README.md           # 数据说明
│   └── field_dictionary.md # WoS字段说明
├── src/                    # 源代码
│   ├── networks/           # 网络分析代码
│   │   ├── co_citation.py  # 共被引网络分析
│   │   └── collaboration.py # 机构合作网络分析
│   ├── parse_wos.py        # WoS数据解析
│   ├── clean_data.py       # 数据清洗
│   ├── convert_to_citespace.py # 转换为CiteSpace格式
│   ├── generate_stats.py   # 生成统计图表
│   ├── generate_prisma.py  # 生成PRISMA筛选数据
│   ├── generate_m1_report.py # 自动生成M1报告
│   └── generate_m2_report.py # 自动生成M2报告
├── outputs/                # 输出结果
│   ├── figures/            # 图表
│   │   ├── annual_trend.png    # 年度发文趋势图
│   │   ├── keyword_cooccurrence.png # 关键词共现图谱
│   │   ├── institution_collab.png # 机构合作图谱
│   │   └── cocitation_network.png # 参考文献共被引图谱
│   └── tables/             # 表格
│       ├── top10_authors.csv
│       ├── top10_journals.csv
│       └── top10_institutions.csv
├── reports/                # 里程碑报告
│   ├── milestone1_report.md # M1里程碑报告
│   ├── milestone2_report.md # M2里程碑报告
│   ├── data_quality.md     # 数据质量报告
│   ├── query_rationale.md  # 检索式设计理由
│   ├── screening_rules.md  # 文献筛选规则
│   └── citespace_params.md # CiteSpace参数记录
├── paper/                  # 最终成果
│   ├── final_paper.md      # 最终学术报告
│   └── presentation.pptx   # 汇报PPT
├── requirements.txt        # 项目依赖
└── README.md               # 项目主页
