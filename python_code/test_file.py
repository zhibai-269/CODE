import scipy.io as sio
import numpy as np
import os
from utils import *
from tqdm import tqdm,trange

structual_path="../matfile/distance_4/"
function_path="../matfile/res_fmri_data/"

structual_keys=os.listdir(structual_path)
structual_keys=[i[:6]for i in structual_keys if i.endswith("keys.mat")] 
function_keys=os.listdir(function_path)
function_keys=[i[:6]for i in function_keys ]
keys_all=set(structual_keys).intersection(set(function_keys))
keys_all=list(keys_all)
 
def save_all_index(index,name):
    save_path="../matfile/functional_and_structual_matrix/" 
    with open(save_path+name+"all_inde.txt",'w') as f:
        for i in index:
            f.write(str(i)+'\n')



for key_test in tqdm(keys_all):

    # key_test=keys_all[0]
    INDEX_path="../matfile/surfaces/"
    # INDEX=sio.loadmat(INDEX_path+key_test+"_INDEX.mat")["INDEX"]
    keys_path="../matfile/distance_4/"
    #拿到index标签数据
    # +key_test+"INDEX.mat")["INDEX"][0][0][0]
    indexs=list(index_data[1:])
    index_to_oringin_dic={}
    oringin_to_index_dic={}
    for i in range(len(indexs)):
        index_to_oringin_dic[i+1]=indexs[i]
        oringin_to_index_dic[indexs[i]]=i+1

    #去除structual index
    fmri_data=sio.loadmat(function_path+key_test+"_rfMRI_REST1_LR_Atlas.dtseries.mat")["fmri_mat"]
    #取出的仅仅是取了index之后的那些数据
    fmri_data=fmri_data[indexs]
    fmri_data.shape

    #求需要去除的nan对应的index
    remove_index=list(set(np.where(np.isnan(fmri_data))[0]))
    remove_index=[i for i in remove_index]
    remove_index.sort()
    fmri_dic={}
    for i in range(len(indexs)):
        fmri_dic[i]=indexs[i]

    # print(remove_index)
    remove_index_anti=[fmri_dic[i] for i in remove_index]
    # print(remove_index_anti)


    edge_list=load_edge(structual_path+key_test+"keys.mat")
    edge_list=[(int(i[0]),int(i[1])) for i in edge_list]
    edge_list_new,node1,node2=reindex(edge_list)
    structual_index=[index_to_oringin_dic[i] for i in node1]

    all_index=list(set(structual_index)-set(remove_index_anti))
    all_index.sort()
    print("最终保存的节点数："+str(len(all_index)))
    save_all_index(all_index,key_test)
    #读取fmri数据并求出corr
    fmri_data_new=sio.loadmat(function_path+key_test+"_rfMRI_REST1_LR_Atlas.dtseries.mat")["fmri_mat"]
    # fmri_data=fmri_data[all_index]
    functional_matrix=fmri_data_new[all_index]
    functional_matrix
    fun_corr=np.corrcoef(functional_matrix)
    #计算structual数据
    structual_matrix=np.zeros((len(all_index),len(all_index)))
    edge_list=load_edge(structual_path+key_test+"keys.mat")
    edge_list=[(int(i[0]),int(i[1])) for i in edge_list]
    for edge in tqdm(edge_list,desc="structual"):
        if index_to_oringin_dic[edge[0]] in all_index and index_to_oringin_dic[edge[1]] in all_index:
            # print("ss")
            index_matrix_x=all_index.index(index_to_oringin_dic[edge[0]])
            index_matrix_y=all_index.index(index_to_oringin_dic[edge[1]])
            structual_matrix[index_matrix_x,index_matrix_y]=1
            structual_matrix[index_matrix_y,index_matrix_x]=1

    #保存数据
    save_path="../matfile/functional_and_structual_matrix/"
    sio.savemat(f"{save_path}{key_test}structual_matrix.mat",{"structual_matrix":structual_matrix})