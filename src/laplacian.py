import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv('../data/network_tf_gene.txt', sep='\t', header=None, comment='#').drop([3, 4, 5], axis=1)

    df.columns = ['tf', 'gene', 'effect']

    G = nx.from_pandas_edgelist(df=df, source='tf', target='gene', edge_attr='effect')
    # Laplacian matrix of a graph is symmetric, positive semidefinite, and singular
    L = nx.laplacian_matrix(G)
    L_eigen = nx.laplacian_spectrum(G)

    plt.rc('figure', figsize=(30, 30))
    layout = nx.spring_layout(G, k=0.05, iterations=50, seed=5)
    # TODO: node_color shoule be changed to the coefficient of eigenvectors
    nx.draw(G, layout, node_size=100, node_color=range(2052), edge_color="#cccccc", cmap=plt.cm.Greens)
    plt.axis('off')
    plt.title("TF-Gene Regulatory Network")
    plt.tight_layout()
    plt.savefig('../images/laplacian.png')
    plt.show()

