import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

if __name__ == "__main__":
    df = pd.read_csv("../data/processed/final.csv")

    # 1. 生成年度发文趋势图（2015-2025）
    year_count = df['PY'].value_counts().sort_index()
    plt.figure(figsize=(12, 6))
    bars = plt.bar(year_count.index.astype(str), year_count.values, color='#2c7bb6', width=0.6)
    
    # 添加数值标签
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'{int(height)}',
                 ha='center', va='bottom', fontsize=12)
    
    plt.title('AIGC in Humanities & Digital Humanities (2015-2025)', fontsize=16, pad=20)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Number of Publications', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig("../outputs/figures/annual_trend.png", dpi=300, bbox_inches='tight')
    print("✅ 年度发文趋势图已保存")

    # 2. 生成Top10作者表格
    top_authors = df['AU'].str.split('; ').explode().value_counts().head(10)
    top_authors.to_csv("../outputs/tables/top10_authors.csv", header=['Publications'])
    print("✅ Top10作者表已保存")

    # 3. 生成Top10期刊表格
    top_journals = df['SO'].value_counts().head(10)
    top_journals.to_csv("../outputs/tables/top10_journals.csv", header=['Publications'])
    print("✅ Top10期刊表已保存")

    # 4. 生成Top10机构表格
    top_institutions = df['C1'].str.extract(r'^([^,]+)')[0].value_counts().head(10)
    top_institutions.to_csv("../outputs/tables/top10_institutions.csv", header=['Publications'])
    print("✅ Top10机构表已保存")

    print("\n🎉 M1里程碑所有产出全部生成完成！")