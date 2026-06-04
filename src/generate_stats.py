import pandas as pd
import re
from collections import Counter

def generate_correct_stats():
    """
    修复版统计脚本：正确生成Top10作者、机构、期刊表格
    解决了之前作者合并、机构统计错误的问题
    """
    print("📊 正在读取清洗后的数据...")
    df = pd.read_csv("../data/processed/final.csv")
    total = len(df)
    print(f"✅ 共读取 {total} 篇有效文献")

    # ====================== 1. Top10 作者统计 ======================
    print("\n📝 正在统计Top10作者...")
    authors = []
    for au in df['AU'].dropna():
        # 正确分割多个作者（WoS格式："; "分隔）
        for author in str(au).split('; '):
            author = author.strip()
            if author:
                authors.append(author)
    
    author_counts = Counter(authors).most_common(10)
    author_df = pd.DataFrame(author_counts, columns=['Author', 'Publications'])
    author_df.to_csv("../outputs/tables/top10_authors.csv", index=False, encoding='utf-8-sig')
    print("✅ Top10作者表格已生成：outputs/tables/top10_authors.csv")

    # ====================== 2. Top10 机构统计 ======================
    print("\n🏢 正在统计Top10机构...")
    institutions = []
    for c1 in df['C1'].dropna():
        # 正确分割多个机构地址
        for addr in str(c1).split('; '):
            addr = addr.strip()
            if not addr:
                continue
            
            # 提取机构名称（去掉开头的[作者名]部分）
            # 格式示例：[Dianova, Vera G.] Franklin Univ Switzerland, Div Business & Econ
            match = re.match(r'\[.*?\]\s*(.*?)(,|$)', addr)
            if match:
                inst = match.group(1).strip()
                if inst:
                    institutions.append(inst)
    
    inst_counts = Counter(institutions).most_common(10)
    inst_df = pd.DataFrame(inst_counts, columns=['Institution', 'Publications'])
    inst_df.to_csv("../outputs/tables/top10_institutions.csv", index=False, encoding='utf-8-sig')
    print("✅ Top10机构表格已生成：outputs/tables/top10_institutions.csv")

    # ====================== 3. Top10 期刊统计 ======================
    print("\n📚 正在统计Top10期刊...")
    journal_counts = df['SO'].value_counts().head(10).reset_index()
    journal_counts.columns = ['Journal', 'Publications']
    journal_counts.to_csv("../outputs/tables/top10_journals.csv", index=False, encoding='utf-8-sig')
    print("✅ Top10期刊表格已生成：outputs/tables/top10_journals.csv")

    # ====================== 打印结果预览 ======================
    print("\n" + "="*50)
    print("📊 统计结果预览")
    print("="*50)
    
    print("\n🏆 Top10 作者：")
    for i, (author, count) in enumerate(author_counts, 1):
        print(f"{i}. {author}: {count}篇")
    
    print("\n🏢 Top10 机构：")
    for i, (inst, count) in enumerate(inst_counts, 1):
        print(f"{i}. {inst}: {count}篇")
    
    print("\n📚 Top10 期刊：")
    for i, row in journal_counts.iterrows():
        print(f"{i+1}. {row['Journal']}: {row['Publications']}篇")

    print("\n🎉 所有统计表格已成功生成！")

if __name__ == "__main__":
    generate_correct_stats()