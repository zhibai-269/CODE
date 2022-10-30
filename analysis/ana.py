result_path="../new_result/fix_gtoup_10_result.txt"
mat_file_path="../matfile/surfaces/"
fmri_path="../matfile/resfmri_data/"
structual_path="../matfile/index_fixed/structual_matrix_1/"
functional_path="../matfile/index_fixed/functional_matrix/"
select_key="114621"
fix_index_path="../graph_file/fix_index.txt"

import numpy as np
import scipy.io as sio
import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from tqdm import tqdm
fix_index=[]
fix_result=[]
with open(result_path,"r") as f:
    for line in f.readlines():
        fix_result.append(int(line.strip()))

# keys=['114621', '114823', '115017', '115219', '115320', '115825', '116221', '116524', '116726', '117122']
keys1=['117324', '117930', '118023', '118124', '118225', '118528', '118730', '118932', '119126', 
'119732', '119833', '120111', '120212', '120515', '120717', '121416', '121618', '121921', '122317',
 '122620', '122822', '123117', '123420', '123521', '123824', '123925', '124220', '124422', '124624', 
 '124826', '125525', '126325', '126628', '127327', '127630', 
'127933', '128026', '128127', '128632', '128935', '129028', '129129', '129331']
with  open(fix_index_path,"r") as f:
    for line in f:
        fix_index.append(int(line))
index_anti_dict={}
for i in range(len(fix_index)):
    index_anti_dict[fix_index[i]]=i
#映射回结构矩阵的index
def map_index(index):
    return index_anti_dict[index]
anti_index=[map_index(i) for i in fix_index]
fix_rsult_anti_index=[map_index(i) for i in fix_result]


columns=["person","degree_centrality","hub_degree_centrality","betweenness_centrality","hub_betweenness_centrality",
"closeness_centrality","hub_closeness_centrality","clustering","hub_clustering","degree","hub_degree"
]

data_frame=pd.DataFrame(columns=columns)

for select_key in tqdm(keys1):
    structual_matrix=sio.loadmat(structual_path+select_key+".mat")["matrix"]
    print(structual_matrix.shape)
    #读取图
    print("read graph")
    g=nx.from_numpy_matrix(structual_matrix)
    print("degree_ce")
    degree_centrality=nx.degree_centrality(g)

    betweenness_centrality=nx.betweenness_centrality(g)
    closeness_centrality=nx.closeness_centrality(g)
    betweenness_centrality=nx.betweenness_centrality(g)
    clustering=nx.clustering(g)
    degree=nx.degree(g)
    degree=[n[1] for n in degree]
    hub_degree_centrality={}
    hub_betweenness_centrality={}
    hub_closeness_centrality={}
    hub_clustering={}
    hub_degree={}
    row={}
    for i in fix_rsult_anti_index:
        hub_degree_centrality[i]=degree_centrality[i]
        hub_betweenness_centrality[i]=betweenness_centrality[i]
        hub_closeness_centrality[i]=closeness_centrality[i]
        hub_clustering[i]=clustering[i]
        hub_degree[i]=degree[i]
    row["person"]=select_key
    row["degree_centrality"]=np.mean(list(degree_centrality.values()))
    row["hub_degree_centrality"]=np.mean(list(hub_degree_centrality.values()))
    row["betweenness_centrality"]=np.mean(list(betweenness_centrality.values()))
    row["hub_betweenness_centrality"]=np.mean(list(hub_betweenness_centrality.values()))
    row["closeness_centrality"]=np.mean(list(closeness_centrality.values()))
    row["hub_closeness_centrality"]=np.mean(list(hub_closeness_centrality.values()))
    row["clustering"]=np.mean(list(clustering.values()))
    row["hub_clustering"]=np.mean(list(hub_clustering.values()))
    row["degree"]=np.mean(degree)
    # print(degree)
    row["hub_degree"]=np.mean(list(hub_degree.values()))
    
    data_frame=pd.concat([data_frame,pd.DataFrame(row,index=[0])])
    data_frame.to_csv("../new_result/fix_group_10_result_others.csv")



data_frame.to_csv("../new_result/fix_group_10_result_others.csv")





