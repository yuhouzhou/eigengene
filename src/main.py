import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


if __name__ == '__main__':
    df = pd.read_csv('../data/network_tf_gene.txt', sep='\t', header=None, comment='#').drop([3, 4, 5], axis=1)
    df.columns = ['tf', 'gene', 'effect']

    plt.rc('figure', figsize=(10, 6))
    G = nx.from_pandas_edgelist(df=df, source='tf', target='gene', edge_attr='effect')

    nx.draw(G, node_size=0.1)

    plt.tight_layout()
    plt.savefig('../images/network.png')
    plt.show()
