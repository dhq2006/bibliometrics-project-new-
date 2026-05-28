import pandas as pd

if __name__ == "__main__":
    raw = pd.read_csv("../data/processed/parsed.csv")
    final = pd.read_csv("../data/processed/final.csv")

    print("=== PRISMA 2020 筛选数据 ===")
    print(f"1. 数据库初检文献数：{len(raw)} 篇")
    print(f"2. 去重后文献数：{len(raw.drop_duplicates(subset=['UT']))} 篇")
    print(f"3. 筛选文献类型后：{len(raw[raw['DT'].isin(['Article', 'Review Article'])])} 篇")
    print(f"4. 剔除无参考文献后：{len(raw.dropna(subset=['CR']))} 篇")
    print(f"5. 剔除无机构信息后：{len(raw.dropna(subset=['C1']))} 篇")
    print(f"6. 最终纳入分析：{len(final)} 篇")