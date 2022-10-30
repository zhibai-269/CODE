import load_edge
from tqdm import tqdm
# print(edge)
def remove_some(edge_key_list):
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
    print(remove_list)
    # value__remove_list=[edge_value_list[i] for i,_ in remove_list]

    for i,ele in remove_list:

        edge_key_list.remove(ele)
    return edge_key_list
def save_graph_txt():
    pass

filename="../matFile/edge_keys.mat"
edge_key_list=load_edge.load_edge(filename)
edge_list=remove_some(edge_key_list)
print(edge_list)