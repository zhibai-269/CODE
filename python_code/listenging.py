#从融合结果中提取网络边，并写入文件中
import os
import scipy.io as sio
import numpy as np
import os
from utils import *
from tqdm import tqdm,trange
import time

fix_key=os.listdir("../matfile/index_fixed/fix_result_1/")
fix_key=[i[:6] for i in fix_key if i.endswith(".mat")]

def get_result_matrix_from_intermat(key):
    #从融合后的mat数据中提取matrix
    result_path="../matfile/index_fixed/fix_result_1/"
    # key="120212"
    result_matrix=sio.loadmat(result_path+key+".mat")["A"]
    result_matrix
    return result_matrix
def get_edge_list_from_matrix(matrix):
    #从matrix中提取符合条件的数据
    edge_list=[]
    for i in range(len(matrix)):
        for j in range(i,len(matrix)):
            if matrix[i][j]>0.01:
                edge_list.append((i,j))
    return edge_list
def save_edges_txt(edges,path):
    #将边的信息保存到txt文件中，以备FINDER使用
    with open(path,"w") as f:
        for edge in edges:
            f.write(str(edge[0])+" "+str(edge[1])+"\n")

kyes_now=[]
def get_and_save(key):
    result_matrix=get_result_matrix_from_intermat(key)
    
    edge_list=get_edge_list_from_matrix(result_matrix)
    # print(len(edge_list))
    save_edges_txt(edge_list,"../new_result/pre_oringin_fix_index/"+key+".txt")


    edge_new,dic,dic2=reindex(edge_list)
    save_edges_txt(edge_new,"../new_result/oringin_fix_index/"+key+".txt")



# for key in fix_key:
#     #在所有key中，将mat数据处理成txt文件

#     result_matrix=get_result_matrix_from_intermat(key)
    
#     edge_list=get_edge_list_from_matrix(result_matrix)
#     print(len(edge_list))
#     save_edges_txt(edge_list,"../new_result/pre_oringin_fix_index/"+key+".txt")


#     edge_new,dic,dic2=reindex(edge_list)
#     save_edges_txt(edge_new,"../new_result/oringin_fix_index/"+key+".txt")

def get_strucutla_result():
    path="../new_result/oringin_fix_index/"
    keys=os.listdir(path)
    keys=[i[:6] for i in keys if i.endswith(".txt")]
    return keys

def get_fix_result():
    path="../matfile/index_fixed/fix_result_1/"
    keys=os.listdir(path)
    keys=[i[:6] for i in keys if i.endswith(".mat")]
    return keys

if __name__=="__main__":
    
    mat_keys=get_fix_result()
    txt_keys=get_strucutla_result()
    for i in mat_keys:
        if i not in txt_keys:
            print(i)
            get_and_save(i)
            
        # time.sleep(60)




    # print(dic)
#抽象小网络，分析节点之间的相连情况
#字典学习
#抽象出小网络，分析之间的关系
#

