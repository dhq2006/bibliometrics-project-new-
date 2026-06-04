import pandas as pd
import re
from collections import Counter

def generate_correct_stats():
    """
    终极修复版统计脚本：彻底解决多作者合并问题
    使用正则表达式直接匹配WoS作者格式，无视分隔符错误
    """
    print("📊 正在读取清洗后的数据...")
    df = pd.read_csv("../data/processed/final.csv")
    total = len(df)
    print(f"✅ 共读取 {total} 篇有效文献")

    # ====================== 1. Top10 作者统计（终极修复） ======================
    print("\n📝 正在统计Top10作者...")
    authors = []
    # WoS作者标准格式：姓氏, 名字首字母（如Bozkurt, A; Chan, CKY）
    author_pattern = re.compile(r'[A-Za-z-]+, [A-Z]+')
    
    for au in df['AU'].dropna():
        au_str = str(au).strip()
        if not au_str:
            continue
        
        # 用正则表达式直接提取所有符合格式的作者
        # 无视分隔符是分号、空格还是其他错误字符
        found_authors = author_pattern.findall(au_str)
        for author in found_authors:
            author = author.strip()
            if author:
                authors.append(author)
    
    author_counts = Counter(authors).most_common(10)
    author_df = pd.DataFrame(author_counts, columns=['Author', 'Publications'])
    author_df.to_csv("../outputs/tables/top10_authors.csv", index=False, encoding='utf-8-sig')
    print("✅ Top10作者表格已生成：outputs/tables/top10_authors.csv")

    # ====================== 2. Top10 机构统计（已修复） ======================
    print("\n🏢 正在统计Top10机构...")
    institutions = []
    for c1 in df['C1'].dropna():
        for addr in str(c1).split('; '):
            addr = addr.strip()
            if not addr:
                continue
            
            match = re.match(r'\[.*?\]\s*(.*?)(,|$)', addr)
            if match:
                inst = match.group(1).strip()
                if inst:
                    institutions.append(inst)
    
    inst_counts = Counter(institutions).most_common(10)
    inst_df = pd.DataFrame(inst_counts, columns=['Institution', 'Publications'])
    inst_df.to_csv("../outputs/tables/top10_institutions.csv", index=False, encoding='utf-8-sig')
    print("✅ Top10机构表格已生成：outputs/tables/top10_institutions.csv")

    # ====================== 3. Top10 期刊统计（正确） ======================
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