from email import utils
from telnetlib import SE
from tkinter.messagebox import NO
import pydist2
import numpy as np
import cupy as cp
import scipy.io  as sio
from tqdm import tqdm,trange
from utils import *
class Surface:
    def __init__(self,filename):
        self.vetice=None
        self.surface=None
        self.Pdata=None
        self.init(filename)
    def init(self,filename):
        surf_data=sio.loadmat(filename)["surface"][0][0]
        self.vetice=surf_data[0]
        self.surface=surf_data[1]
        self.Pdata=surf_data[2]
    
class Fibers:
    def __init__(self,filename):
        self.fiber=None
        self.vetice=None
        self.Pdata=None
        self.init(filename)
    def init(self,filename):
        fiber_data=sio.loadmat(filename)["fiber"][0][0]
        self.fiber=np.array(fiber_data[0][0])
        self.vetice=cp.array(fiber_data[1])

class Seg:
    def __init__(self) -> None:
        self.x=None
        self.y=None
        self.z=None




def cal_fiber_end_face(Surf_name,Fibers_name):
#     %Surf : 用ReadSurf(name_surf,0,0)读出，faces索引是减一的，
# %Fibers : ReadFiber(name_fiber,{}).fiber读出，里面的.fiber
# % save current time
#return
# 
#  
    Surf=Surface(Surf_name)
    Fiber=Fibers(Fibers_name).fiber
    
   
    fiber_end_ratio=0.5
    SEG_THR = 0.001
    AREA_THR = 0.001
    nearest_face_thre = 2
    end_length = 3

    face_normal = cp.zeros(3,Surf.surface.shape[1])
    # #Operate on each small triangle face
    for face_id in range(Surf.surface.shape[1]):
        vtx_1=Surf.vetice[:,Surf.surface[0,face_id]]
        vtx_2=Surf.vetice[:,Surf.surface[1,face_id]]
        vtx_3=Surf.vetice[:,Surf.surface[2,face_id]]

        #Generate
        vector_1=vtx_1-vtx_2
        vector_2=vtx_1-vtx_3
        tmp_norm=cp.cross(vector_1,vector_2)
        tmp_norm=tmp_norm/cp.sqrt(sum(tmp_norm**2))
        face_normal[:,face_id]=tmp_norm
    output = cp.zeros(2,Fiber.shape[0])
    for fiber_id in trange(Fiber.shape[0]):
        if fiber_id%10==0:
            pass
        fiber=Fiber[fiber_id]
        if fiber.shape[1]<10:
            output[1,fiber_id]=-1
            output[2,fiber_id]=-1
        else:
            fiber_end_1=fiber[:,:round(fiber.shape[1]*fiber_end_ratio)]
            fiber_end_2=fiber[:,round(fiber.shape[1]*(1-fiber_end_ratio)):]
            #使用一个新增库实现
            tmp_dist=pydist2.pdist2(fiber_end_1.T,Surf.vetice.T)
            #找到点之间距离小于阈值的下标，find找到的是索引，ind2sub转换成下标，x代表行
            x,y=cp.where(tmp_dist<nearest_face_thre)
            y=list(set(y))
            f_1=[]
            f_2=[]
            f_3=[]

            #记录下有符合标准的顶点穿过的三角形索引
            for iii in range(len(y)):
                f_1=np.where(Surf.surface[0,:]==y[iii])[0]
                f_2=np.where(Surf.surface[1,:]==y[iii])[0]
                f_3=np.where(Surf.surface[2,:]==y[iii])[0]
            f_indx_1=list(set(f_1).union(set(f_2)).union(set(f_3)))



            
            tmp_dist=pydist2.pdist2(fiber_end_2.T,Surf.vetice.T)
            
            x,y=cp.where(tmp_dist<nearest_face_thre)
            y=list(set(y))
            f_1=[]
            f_2=[]
            f_3=[]

            for iii in range(len(y)):
                f_1=np.where(Surf.surface[0,:]==y[iii])[0]
                f_2=np.where(Surf.surface[1,:]==y[iii])[0]
                f_3=np.where(Surf.surface[2,:]==y[iii])[0]
            f_indx_2=list(set(f_1).union(set(f_2)).union(set(f_3)))
            #first end
            stop_flag = 0;
            cross_face_id = -1;

            if len(f_indx_1)!=0:
                for seg_id in range(1,fiber_end_1.shape[1]):
                    seg_v1=Seg()
                    seg_v1.x=fiber_end_1[0,seg_id]
                    seg_v1.y=fiber_end_1[1,seg_id]
                    seg_v1.z=fiber_end_1[2,seg_id]
                    seg_v2=Seg()

                    seg_v2.x=fiber_end_2[0,seg_id-1]
                    seg_v2.y=fiber_end_2[1,seg_id-1]
                    seg_v2.z=fiber_end_2[2,seg_id-1]
                    for ii in range(len(f_indx_1)):
                        face_id=f_indx_1[ii]
                        surf_vtx=Seg()
                        surf_vtx.x=Surf.vetice[0,Surf.surface[0,face_id]]
                        surf_vtx.y=Surf.vetice[1,Surf.surface[0,face_id]]
                        surf_vtx.z=Surf.vetice[2,Surf.surface[0,face_id]]

                        #每个三角形的垂直单位向量
                        surf_norm=Seg()
                        surf_norm.x=face_normal[0,face_id]
                        surf_norm.y=face_normal[1,face_id]
                        surf_norm.z=face_normal[2,face_id]



                    #这个线段是否穿过小三角形，cross_output
                        cross_output=seg_line_cross_surf(seg_v1,seg_v2,surf_vtx,surf_norm,SEG_THR)
                        if cross_output.cross_flag==1:
                            tmp_vtx_1=Surf.vertices[:,Surf.surface[0,face_id]]
                            tmp_vtx_2=Surf.vertices[:,Surf.surface[1,face_id]]
                            tmp_vtx_3=Surf.vertices[:,Surf.surface[2,face_id]]


cal_fiber_end_face("../matfile/100206surface.mat","../matfile/100206fiber.mat")




