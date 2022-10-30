import scipy.io as sio
def load_edge(filename):
    """
    Loads the edge list from a file.
    """
    edge_list = sio.loadmat(filename)
    # print(edge_list['edge_info_key'][0])
    edgelist=[]
    for edge in edge_list['key'][0]:
        edgelist.append(edge[0].split("+"))
    # print(edgelist)
    # return edge_list['edge_list']
    return edgelist
# load_edge('../matFile/edge_keys.mat')