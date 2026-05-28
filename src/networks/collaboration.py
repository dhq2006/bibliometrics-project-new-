import pandas as pd
import networkx as nx

def build_collaboration_network(df):
    """构建机构合作网络"""
    G = nx.Graph()
    
    for _, row in df.iterrows():
        institutions = str(row['C1']).split('; ')
        for i in range(len(institutions)):
            for j in range(i+1, len(institutions)):
                inst1 = institutions[i].strip()
                inst2 = institutions[j].strip()
                if G.has_edge(inst1, inst2):
                    G[inst1][inst2]['weight'] += 1
                else:
                    G.add_edge(inst1, inst2, weight=1)
    
    return G

if __name__ == "__main__":
    df = pd.read_csv("../../data/processed/final.csv")
    G = build_collaboration_network(df)
    
    print(f"机构合作网络节点数：{G.number_of_nodes()}")
    print(f"机构合作网络边数：{G.number_of_edges()}")
    
    # 计算度中心性
    degree_centrality = nx.degree_centrality(G)
    top10_institutions = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:10]
    
    print("\nTop10 高中心性机构：")
    for i, (inst, centrality) in enumerate(top10_institutions):
        print(f"{i+1}. {inst} (中心性：{centrality:.4f})")