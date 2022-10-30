import scipy.io as sio
from tqdm import tqdm
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

from tqdm import tqdm
# print(edge)
def remove_and_sort(edge_key_list):
#去除自环
    remove_list=[]
    for i in tqdm(range(len(edge_key_list))) :
        #自环
        if edge_key_list[i][0]==edge_key_list[i][1]:
            remove_list.append((i,edge_key_list[i]))
        #重复边
        elif edge_key_list.count(edge_key_list[i])>1:

            remove_list.append((i,edge_key_list[i]))
        # print(i)
    # print(remove_list)
    # value__remove_list=[edge_value_list[i] for i,_ in remove_list]

    for i,ele in remove_list:

        edge_key_list.remove(ele)
    edge_list_sort=[[int(x[0]),int(x[1])]if int(x[0])<int(x[1]) else [int(x[1]),int(x[0])] for x in edge_key_list]
# edge_list_sort
    sort_d = [value for index, value in sorted(enumerate(edge_list_sort), key=lambda d:d[1])]
    # sort_d
    return sort_d

def reindex(edge_list):
    print("正在处理索引压缩")
    node_unique=[]
    for it in edge_list:
        if it[0] not in node_unique:
            node_unique.append(it[0])
        if it[1] not in node_unique:
            node_unique.append(it[1])
    node_unique.sort()
    node_unique_dict={}
    for i,ele in enumerate(node_unique):
        node_unique_dict[ele]=i
    edge_list_new=[[node_unique_dict[x[0]],node_unique_dict[x[1]]] for x in edge_list]
    edge_list_unique=[]
    for i in tqdm(range(len(edge_list_new))):
        if edge_list_new[i] not in edge_list_unique:
            edge_list_unique.append(edge_list_new[i])
    return edge_list_unique,node_unique_dict

def save_text(filename,edges):

    with open(filename, "w") as f:
        for edge in edges:
            f.write(str(edge[0]) + " " + str(edge[1]) + "\n")


# filename="../matFile/116221.mat"
# edge_key_list=load_edge.load_edge(filename)
# edge_list=remove_and_sort(edge_key_list)
# print(edge_list)
# edge_list_sort=[[int(x[0]),int(x[1])]if int(x[0])<int(x[1]) else [int(x[1]),int(x[0])] for x in edge_list]
# # edge_list_sort
# sort_d = [value for index, value in sorted(enumerate(edge_list_sort), key=lambda d:d[1])]
# sort_d

def process(person):
    for p in person:
        edges=load_edge(f'../matFile/{p}.mat')
        edges_remove=remove_and_sort(edges)
        print(len(edges_remove))
        edge_list_sort = [[int(x[0]), int(x[1])] if int(x[0]) < int(x[1]) else [int(x[1]), int(x[0])] for x in
                          edges_remove]
        # edge_list_sort
        sort_d = [value for index, value in sorted(enumerate(edge_list_sort), key=lambda d: d[1])]
        sort_d
        edge_index,unique_dict=reindex(sort_d)
        new=[]

        for i in edge_index:
            if i not in new:
                new.append(i)
            else:
                # print(i)
                pass
        print(len(new))

        save_text(f'../graph_file/{p}.txt',new)
if __name__=='__main__':
    # person = ["106319", "116221", "110007"]
    person=["119732","123420"]
    # x=sio.loadmat("../matFile/106319.mat")
    # print(x)
    process(person)