import pandas as pd
import os

def parse_wos(filepath):
    print(f"🔍 检查文件路径: {filepath}")
    if not os.path.exists(filepath):
        print(f"❌ 错误：文件不存在！请确认路径正确")
        return None

    print("✅ 文件存在，尝试读取文件...")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
        print(f"✅ 文件读取成功，总字符数：{len(text)}")
    except Exception as e:
        print(f"❌ 读取文件失败：{e}")
        return None

    print("🔍 开始按ER分割记录...")
    records = text.split('\nER\n')
    print(f"✅ 分割完成，记录数：{len(records)}")

    data = []
    for rec in records:
        if not rec.strip():
            continue
        item = {}
        lines = rec.split('\n')
        key = None
        val = []

        for line in lines:
            if not line.strip():
                continue
            if line.startswith('  '):
                if key:
                    val.append(line.strip())
            else:
                if key:
                    item[key] = ' '.join(val)
                key = line[:2].strip()
                val = [line[2:].strip()]

        if key:
            item[key] = ' '.join(val)
        data.append(item)

    print(f"✅ 解析完成，有效记录数：{len(data)}")
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = parse_wos("../data/raw/savedrecs_full.txt")
    if df is not None:
        print("✅ 解析成功！")
        print(f"📊 数据列：{list(df.columns)}")
        print(f"📊 数据量：{len(df)} 篇")
        df.to_csv("../data/processed/parsed.csv", index=False, encoding='utf-8')
        print("✅ 已保存解析结果到 ../data/processed/parsed.csv")