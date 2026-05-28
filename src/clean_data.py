import pandas as pd

if __name__ == "__main__":
    # 读取解析后的原始数据
    df = pd.read_csv("../data/processed/parsed.csv")
    print(f"原始数据量：{len(df)} 篇")

    # 1. 只保留期刊文章和综述（课程要求）
    df = df[df['DT'].isin(['Article', 'Review Article'])]
    print(f"筛选期刊/综述后：{len(df)} 篇")

    # 2. 去重（按WoS唯一标识符UT去重）
    df = df.drop_duplicates(subset=['UT'])
    print(f"去重后：{len(df)} 篇")

    # 3. 剔除无参考文献、无机构信息的文献（后续分析必须用到）
    df = df.dropna(subset=['CR', 'C1'])
    print(f"剔除无效文献后：{len(df)} 篇")

    # 保存最终清洗后的数据集
    df.to_csv("../data/processed/final.csv", index=False, encoding='utf-8')
    print("✅ 清洗完成！最终数据已保存到 ../data/processed/final.csv")