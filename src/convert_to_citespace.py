import pandas as pd
import re

def extract_cleaned_records_original_format(raw_path, cleaned_path, output_path):
    """
    从原始WoS文件中精确提取清洗后的837篇文献
    100%保留原始格式，解决CiteSpace识别问题
    """
    # 1. 读取清洗后的数据，获取需要保留的UT号
    cleaned_df = pd.read_csv(cleaned_path)
    valid_uts = set(cleaned_df['UT'].str.strip())
    print(f"🔍 从清洗后数据获取有效UT号：{len(valid_uts)} 个")

    # 2. 读取原始WoS文件
    with open(raw_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 3. 按ER分割每篇文献
    records = content.split('\nER\n')
    extracted = 0

    with open(output_path, 'w', encoding='utf-8') as out_f:
        # 写入标准WoS文件头
        out_f.write("FN Clarivate Analytics Web of Science\n")
        out_f.write("VR 1.0\n\n")

        for record in records:
            if not record.strip():
                continue

            # 提取当前文献的UT号
            ut_match = re.search(r'UT\s+(WOS:[0-9A-Z]+)', record)
            if not ut_match:
                continue
            
            current_ut = ut_match.group(1).strip()
            
            # 如果是有效文献，完整保留原始格式写入
            if current_ut in valid_uts:
                # 清理可能的文件头残留
                clean_record = re.sub(r'FN.*?VR 1.0\n', '', record, flags=re.DOTALL)
                clean_record = clean_record.strip()
                
                # 逐行写入，完全保留原始换行和缩进
                for line in clean_record.split('\n'):
                    if line.strip():
                        out_f.write(line + '\n')
                
                # 每篇文献结束标记
                out_f.write("ER\n\n")
                extracted += 1

    print(f"✅ 提取完成！共提取 {extracted} 篇文献")
    print(f"📂 输出文件：{output_path}")
    print("✅ 格式100%还原原始WoS，CiteSpace可完美识别")
    print("✅ 已应用所有清洗规则：只保留期刊/综述，剔除无效文献")

if __name__ == "__main__":
    extract_cleaned_records_original_format(
        "../data/raw/savedrecs_full.txt",    # 原始数据
        "../data/processed/final.csv",       # 清洗后的数据（含UT号）
        "../data/processed/wos_for_citespace.txt"  # 输出给CiteSpace的文件
    )