import load_edge
import scipy.io as sio
import os
from tqdm import tqdm,trange
class Edge:
    def __init__(self,edge0,edge1) -> None:
        self.edge0=edge0 if edge0<edge1 else edge1
        self.edge1=edge1 if edge0<edge1 else edge0
        
        
    def __eq__(self, o: object) -> bool:
        return self.edge0==o.edge0 and self.edge1==o.edge1
    def __hash__(self) -> int:
        return hash((self.edge0,self.edge1))
def save_txt_for_edges(edges,file_name):
    with open(file_name,'w') as f:
        for edge in edges:
            f.write(str(edge[0])+' '+str(edge[1])+'\n')


#去除图中的自环并排序
def remove_and_sort(edge_key_list):
    removed_list=[]
    edge_list_sort=[[int(x[0]),int(x[1])]if int(x[0])<int(x[1]) else [int(x[1]),int(x[0])] for x in edge_key_list]
    edge_set=set()
    
    for item in (edge_list_sort):
        if item[0]!=item[1]:
            edge_set.add(Edge(item[0],item[1]))
    for item in edge_set:
        removed_list.append([item.edge0,item.edge1])
    list_sort=[value for index, value in sorted(enumerate(removed_list), key=lambda d:d[1])]
  
    return list_sort
#压缩边的索引
def reindex(edge_list):

    node_unique=[]
    for it in (edge_list) :
        node_unique.append(it[0])
        node_unique.append( it[1])
    node_unique=list(set(node_unique))
    node_unique.sort()


    anti_dict={}

    node_unique_dict={}
    for i,ele in enumerate(node_unique):
        node_unique_dict[ele]=i
        anti_dict[i]=ele

    edge_list_new=[[node_unique_dict[x[0]],node_unique_dict[x[1]]] for x in edge_list]

    return edge_list_new,node_unique_dict,anti_dict


def load_edge(filename):
    """
    Loads the edge list from a m mat file.
    """
    edge_list = sio.loadmat(filename)
    # print(edge_list['edge_info_key'][0])
    edgelist=[]
    for edge in edge_list['edge_key'][0]:
        edgelist.append(map(int,list(edge[0].split("+"))))
    # print(edgelist)
    # return edge_list['edge_list']
    return edgelist    
# def 
#-------------------------提取节点的信息，存储为vtk文件-------------------------
def get_node_verticve_from_result_and_surface(INDEX_mat_file,node_anti_dic,result_node_file,surface_mat_file):
    """根据结果文件和原始的surface文件，获取节点对应的顶点信息

    Args:
        INDEX_mat_file (_type_): 存储索引的mat文件目录
        node_anti_dic (_type_): 压缩索引时的反索引字典
        result_node_file (_type_): 从FINDER中得到的结果节点文件
        surface_mat_file (_type_):从VTK中读取之后的surface mat文件

    Returns:
     """
    nodes=[]
    with open(result_node_file,"r") as f:
        for line in f.readlines()[:200]:
            nodes.append(int(line))
    nodes_for_origin=[node_anti_dic[node] for node in nodes]
    INDEX_dic=[]
    data=sio.loadmat(INDEX_mat_file)
    INDEX_dic=data["INDEX"][0][0][0][1:]
    
    surface_data=sio.loadmat(surface_mat_file)
    vetice_data=surface_data["surface"][0][0][0].T
    vertice=[]
    for node in nodes_for_origin:
        
        vertice.append(vetice_data[int(INDEX_dic[int(node)-1])-1])
    return vertice
def save_vtk(result,filename):
    """将坐标信息保存为vtk文件

    Args:
        result (_type_): 坐标信息，三维数组
        filename (_type_): 要保存的文件名及地址
    """
    with open(filename,"w") as f:
        f.write("# vtk DataFile Version 3.0\nmesh surface\nASCII\nDATASET POLYDATA\n")
        f.write("POINTS "+str(len(result))+" float\n")
        for ve in result:
        
            f.write(str(ve[0])+" "+str(ve[1])+" "+str(ve[2])+"\n")

#------------------------------------------------------------------------

#-------------------------------------------测试两个个体之间一致性的函数-------------------------------------------
def get_result_INDEX(person_name,distance_type="distance_4"):
    """_summary_: 根据个体的名字，获取其在surface上的索引关系

    Args:
        person_name (_type_): 个体名称
        distance_type (str, optional):  计算时的距离. Defaults to "distance_4".

    Returns:
        _type_: _description_
    """
    INDEX_result=[]
    result_file=f"../graph_file/{distance_type}_result/{person_name}.txt"
    edge_list=load_edge(f"../matfile/{distance_type}/{person_name}keys.mat")
    _,_,anti_dic=reindex(edge_list)
    INDEX_file=f"../matfile/surfaces/{person_name}INDEX.mat"
    INDEX_dic=[]
    data=sio.loadmat(INDEX_file)
    INDEX_dic=data["INDEX"][0][0][0][1:]
    result_nodes_from_finder=[]
    with open(result_file,"r") as f:
        for line in f.readlines():
            result_nodes_from_finder.append(int(line))

    for node in result_nodes_from_finder[:200]:
        INDEX_result.append(INDEX_dic[int(anti_dic[node])-1])




    return INDEX_result






#------------------------------------------------以下为历史文件，暂未用到------------------------------------------------
#根据索引字典，获取原始的边信息
def get_origin_index(edge_list,node_unique_dict):
    origin_index=[]
    for i in edge_list:
        origin_index.append([node_unique_dict[i[0]],node_unique_dict[i[1]]])
    return origin_index
#获取原始的节点索引信息
def get_oringin_node_index(node_lists,node_unique_dict):
    origin_node_index=[]
    for i in node_lists:
        origin_node_index.append(node_unique_dict[i])
    return origin_node_index

def get_contains_edges(nodes,edge_list):
    contains_edges=[]
    for edge in edge_list:
        if edge[0] in nodes and edge[1] in nodes:
            contains_edges.append(edge)
    return contains_edges


def mat_transfer(file_name):
    edge_list=load_edge.load_edge(file_name)
    
    edge_list_unique_sort=remove_and_sort(edge_list)
    edge_list_unique,node_unique_dict,antidict=reindex(edge_list_unique_sort)
    return edge_list_unique,antidict
def load_dict(file_name):
    dicts={}
    with open(file_name,'r') as f:
        for line in f.readlines():
            line=line.strip()
            line=line.split(' ')
            dicts[line[0]]=line[1]

    return dicts    
def load_nodes(file_name):
    nodes=[]
    with open(file_name,'r') as f:
        for line in f.readlines():
            line=line.strip()
            nodes.append(line)
    return nodes
#原名load_edge
def load_edge_from_result(file_name):
    edge_list=[]
    with open(file_name,'r') as f:
        for line in f.readlines():
            line=line.strip()
            line=line.split(' ')
            edge_list.append([line[0],line[1]])
    return edge_list
import scipy.io as sio
#从mat文件提取数据
def load_edge(filename):
    """
    Loads the edge list from a file.
    """
    edge_list = sio.loadmat(filename)
    # print(edge_list['edge_info_key'][0])
    edgelist=[]
    for edge in edge_list['edge_key'][0]:
        edgelist.append(edge[0].split("+"))
    # print(edgelist)
    # return edge_list['edge_list']
    return edgelist
# load_edge('../matFile/edge_keys.mat')
# def get_oringin_vertice(filename):
# 