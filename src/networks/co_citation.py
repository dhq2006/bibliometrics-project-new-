import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def build_cocitation_network(df):
    """构建参考文献共被引网络"""
    G = nx.Graph()
    
    for _, row in df.iterrows():
        refs = str(row['CR']).split('; ')
        for i in range(len(refs)):
            for j in range(i+1, len(refs)):
                ref1 = refs[i].strip()
                ref2 = refs[j].strip()
                if G.has_edge(ref1, ref2):
                    G[ref1][ref2]['weight'] += 1
                else:
                    G.add_edge(ref1, ref2, weight=1)
    
    return G

if __name__ == "__main__":
    df = pd.read_csv("../../data/processed/final.csv")
    G = build_cocitation_network(df)
    
    print(f"共被引网络节点数：{G.number_of_nodes()}")
    print(f"共被引网络边数：{G.number_of_edges()}")
    
    # 计算中心性
    degree_centrality = nx.degree_centrality(G)
    top10_cited = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:10]
    
    print("\nTop10 高中心性参考文献：")
    for i, (ref, centrality) in enumerate(top10_cited):
        print(f"{i+1}. {ref} (中心性：{centrality:.4f})")