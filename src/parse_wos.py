import pandas as pd

def parse_wos(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    records = text.split('\nER\n')
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

    return pd.DataFrame(data)

if __name__ == "__main__":
    df = parse_wos("../data/raw/savedrecs_full.txt")
    print("✅ 解析完成，文献数量：", len(df))
    df.to_csv("../data/processed/parsed.csv", index=False, encoding='utf-8')