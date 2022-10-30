
from opcode import opname
from utils import *


# filename="../matFile/106319.mat"

# edge_key,node_dict=mat_transfer(filename)
# print(len(edge_key))
# with open("../test_many/106319.txt","w") as f:
#     for i in edge_key:
#         f.write(str(i[0])+" "+str(i[1])+"\n")
# with open("../test_many/106319.dic","w") as f:
#     for i,ele in node_dict.items():
#         f.write(str(i)+" "+str(ele)+"\n")
#
anti_dict={}
with open("../test_many/106319_second.dic","r") as f:
    for i in f:
        i=i.strip().split(" ")
        anti_dict[int(i[0])]=int(i[1])

first_results_nodes=[]
with open("../test_many/106319_result2.txt","r") as f:
    for i in f:
        first_results_nodes.append(int(i.strip()) )
#
#
#
#
#第一次的结果，首先返回原始索引
second_edge=[]
#获取包含第一次结果的边
with open("../test_many/106319_second.txt","r") as f:
    for i in f:
        i=i.strip().split(" ")
        if int(i[0]) in first_results_nodes and int(i[1]) in first_results_nodes:
            second_edge.append([int(i[0]),int(i[1])])
second_edge,node_unique_dict,second_dic=reindex(second_edge)


with open("../test_many/106319_third.txt","w") as f:
    for i in second_edge:
        f.write(str(i[0])+" "+str(i[1])+"\n")

with open("../test_many/106319_third.dic","w") as f:
    for i in second_dic:
        f.write(str(i)+" "+str(second_dic[i])+"\n")


import scipy.io as sio
surface=sio.loadmat("../matFile/106319surface.mat")
print(surface.keys())
points=surface["surface"][0][0][0].T
# print(points)

#
# 将节点信息写入到vtk



def save_vtk(result,filename):
    with open(filename,"w") as f:
        f.write("# vtk DataFile Version 3.0\nmesh surface\nASCII\nDATASET POLYDATA\n")
        f.write("POINTS "+str(len(result))+" float\n")
        for i in result:
            point=points[edge_dic_rever[int(i)]]
            f.write(str(point[0])+" "+str(point[1])+" "+str(point[2])+"\n")
save_vtk(result_weight,"graph2.vtk")
