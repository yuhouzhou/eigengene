import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    df = pd.read_csv('../data/network_tf_gene.txt', sep='\t', header=None, comment='#').drop([3, 4, 5], axis=1)
    # df = df[:200]
    df.columns = ['tf', 'gene', 'effect']

    # G = nx.from_pandas_edgelist(df=df, source='tf', target='gene', edge_attr='effect', create_using=nx.DiGraph())
    G = nx.from_pandas_edgelist(df=df, source='tf', target='gene', edge_attr='effect')
    plt.rc('figure', figsize=(30, 30))
    # # layout 1
    k = 5/np.sqrt(G.order())
    layout = nx.spring_layout(G, k=0.05, iterations=50, seed=5)
    # # layout 2
    # df1 = pd.DataFrame(index=G.nodes(), columns=G.nodes())
    # for row, data in nx.shortest_path_length(G):
    #     for col, dist in data.items():
    #         df1.loc[row, col] = dist
    # df1 = df1.fillna(df1.max().max())
    # layout = nx.kamada_kawai_layout(G, dist=df1.to_dict())

    tfs = list(df.tf.unique())
    genes = list(df.gene.unique())
    # tf_size = [G.degree(tf) * 40 for tf in tfs]
    # nx.draw_networkx_nodes(G, layout, nodelist=tfs, node_color='lightblue', node_size=tf_size, edgecolors='#cccccc')
    nx.draw_networkx_nodes(G, layout, nodelist=tfs, node_color='lightblue', node_size=100, edgecolors='#cccccc')
    nx.draw_networkx_nodes(G, layout, nodelist=genes, node_color='orange', node_size=100, edgecolors="#cccccc")
    nx.draw_networkx_edges(G, layout, width=1, edge_color="#cccccc")
    node_labels = dict(zip(tfs, tfs))
    # nx.draw_networkx_labels(G, layout, labels=node_labels)
    plt.axis('off')
    plt.title("TF-Gene Regulatory Network")
    plt.tight_layout()
    plt.savefig('../images/main.png')
    plt.show()
