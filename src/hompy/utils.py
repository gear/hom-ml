import networkx as nx 
import pickle as pk
import os


def load_adj(nx_graph, sparse=True):
    '''Returns adj matrix from undirected graph nx_graph.'''
    adj = nx.adj_matrix(nx_graph)
    if not sparse:
        return adj
    else:
        return adj.toarray()
        

def load_graph(pk_nx_file):
    '''Simple hander to load a nx graph stored in a pickle file'''
    path = os.path.expanduser(pk_nx_file)
    path = os.path.abspath(path)
    assert os.path.exists(path), "File {} not found!".format(path)
    assert path.endswith(".graph"), "File {} might not be graph!".format(pk_nx_file)
    with open(path, "rb") as f:
        g = pk.load(f)
    return g

