import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('../data/network_tf_gene.txt', sep='\t', header=None, comment='#').drop([3, 4, 5], axis=1)

    df.columns = ['tf', 'gene', 'effect']

    G = nx.from_pandas_edgelist(df=df, source='tf', target='gene', edge_attr='effect')
    L = nx.laplacian_matrix(G)
    L_eigen = nx.laplacian_spectrum(G)

    # plt.rc('figure', figsize=(30, 30))
    # layout = nx.spring_layout(G, k=0.05, iterations=50, seed=5)
    #
    # tfs = list(df.tf.unique())
    # genes = list(df.gene.unique())
    # tf_size = [G.degree(tf) * 40 for tf in tfs]
    # nx.draw_networkx_nodes(G, layout, nodelist=tfs, node_color='lightblue', node_size=100, edgecolors='#cccccc')
    # nx.draw_networkx_nodes(G, layout, nodelist=genes, node_color='orange', node_size=100, edgecolors="#cccccc")
    # nx.draw_networkx_edges(G, layout, width=1, edge_color="#cccccc")
    # node_labels = dict(zip(tfs, tfs))
    # plt.axis('off')
    # plt.title("TF-Gene Regulatory Network")
    # plt.tight_layout()
    # plt.savefig('../images/laplacian.png')
    # plt.show()

