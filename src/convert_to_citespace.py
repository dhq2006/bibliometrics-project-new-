import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("../data/processed/final.csv")

    # 严格按照你提供的WoS格式输出，保证CiteSpace能100%识别
    with open("../data/processed/wos_for_citespace.txt", 'w', encoding='utf-8') as f:
        for _, r in df.iterrows():
            f.write(f"PT {r.get('PT', '')}\n")
            f.write(f"AU {r.get('AU', '')}\n")
            f.write(f"AF {r.get('AF', '')}\n")
            f.write(f"TI {r.get('TI', '')}\n")
            f.write(f"SO {r.get('SO', '')}\n")
            f.write(f"LA {r.get('LA', '')}\n")
            f.write(f"DT {r.get('DT', '')}\n")
            f.write(f"DE {r.get('DE', '')}\n")
            f.write(f"ID {r.get('ID', '')}\n")
            f.write(f"AB {r.get('AB', '')}\n")
            f.write(f"C1 {r.get('C1', '')}\n")
            f.write(f"CR {r.get('CR', '')}\n")
            f.write(f"PY {r.get('PY', '')}\n")
            f.write(f"UT {r.get('UT', '')}\n")
            f.write("ER\n\n")

    print("✅ CiteSpace专用格式文件已生成！")
    print("📂 文件路径：../data/processed/wos_for_citespace.txt")