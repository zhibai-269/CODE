# Generated with SMOP  0.41
# from libsmop import *
# .\cal_fiber_end_face_new.m

    
# @function
def cal_fiber_end_face_new(Surf=None,Fibers=None,*args,**kwargs):
    varargin = cal_fiber_end_face_new.varargin
    nargin = cal_fiber_end_face_new.nargin


    # addpath '/disk2/three-hinge/Surface';
# addpath '/disk2/three-hinge/Fiber';
# addpath '/disk2/three-hinge/HCP_fiber';
# addpath '/disk2/three-hinge/dtiSurface/surface_rl';
# 
# input_surf_fname = sprintf('#d_dti_cluster_offset.vtk',subject_id);
# input_fiber_fname = sprintf('fiber#d_acs.vtk',subject_id);
# output_fname = sprintf('fiber_end_surface#d.mat',subject_id);
    fiber_end_ratio=0.5
# .\cal_fiber_end_face_new.m:13
    ## fiber_end_ratio: # end points used to compute cross the surface # radius: the distance between searching vertex and fiber end
## output vertex ID: C style
## output file format: fiberID fiber-first-end vertex ID fiber-second-end vertex ID (-1 denotes fiber does not reach any vertex within radius)
    
    #Surf=gpuArray(Surf)
#Fibers=gpuArray(Surf)
    
    SEG_THR=0.001
# .\cal_fiber_end_face_new.m:22
    AREA_THR=0.001
# .\cal_fiber_end_face_new.m:23
    nearest_face_thre=2
# .\cal_fiber_end_face_new.m:25
    end_length=3
# .\cal_fiber_end_face_new.m:26
    # if ~exist(input_surf_fname,'file')        
#        
#     return
# else
#     Surf = ReadSurf(input_surf_fname,[],0);
# end
# 
# if isfield(input_fiber_fname,'vertice')
#     Fibers = input_fiber_fname.fiber;
# else
#     tmp = ReadFiber(input_fiber_fname,{});
#     Fibers = tmp.fiber;
#     
# end
    
    ##++++++++++++++++++++++compute all face normal
    face_normal=zeros(3,size(Surf.faces,2))
# .\cal_fiber_end_face_new.m:45
    # Operate on each small triangle face
    for face_id in arange(1,size(Surf.faces,2)).reshape(-1):
        #the three vertices of the triangle face
        vtx_1=Surf.vertice(arange(),Surf.faces(1,face_id))
# .\cal_fiber_end_face_new.m:49
        vtx_2=Surf.vertice(arange(),Surf.faces(2,face_id))
# .\cal_fiber_end_face_new.m:50
        vtx_3=Surf.vertice(arange(),Surf.faces(3,face_id))
# .\cal_fiber_end_face_new.m:51
        vector_1=vtx_1 - vtx_2
# .\cal_fiber_end_face_new.m:53
        vector_2=vtx_1 - vtx_3
# .\cal_fiber_end_face_new.m:54
        tmp_norm=cross(vector_1,vector_2)
# .\cal_fiber_end_face_new.m:55
        tmp_norm=tmp_norm / sqrt(sum(tmp_norm ** 2))
# .\cal_fiber_end_face_new.m:56
        face_normal[arange(),face_id]=tmp_norm
# .\cal_fiber_end_face_new.m:57
    
    ##++++++++++++++++++++++compute all face normal
    
    output=zeros(2,size(Fibers,2))
# .\cal_fiber_end_face_new.m:61
    # Operate on each fiber
    for fiber_id in arange(1,size(Fibers,2)).reshape(-1):
        fiber_id
        #     Determine whether the program is running and the degree of running
        if mod(fiber_id,10) == 1:
            #         The disp function will directly output the content in the Matlab command window
            disp(fiber_id / size(Fibers,2))
        fiber=Fibers[fiber_id]
# .\cal_fiber_end_face_new.m:70
        if size(fiber,2) < 10:
            output[1,fiber_id]=- 1
# .\cal_fiber_end_face_new.m:72
            output[2,fiber_id]=- 1
# .\cal_fiber_end_face_new.m:73
        else:
            fiber_end_1=fiber(arange(),arange(1,round(dot(size(fiber,2),fiber_end_ratio))))
# .\cal_fiber_end_face_new.m:76
            fiber_end_2=fiber(arange(),arange(round(dot(size(fiber,2),(1 - fiber_end_ratio))),end()))
# .\cal_fiber_end_face_new.m:77
            tmp_dist=pdist2(fiber_end_1.T,Surf.vertice.T)
# .\cal_fiber_end_face_new.m:81
            x,y=ind2sub(size(tmp_dist),find(tmp_dist <= nearest_face_thre),nargout=2)
# .\cal_fiber_end_face_new.m:83
            y=unique(y)
# .\cal_fiber_end_face_new.m:84
            f_1=[]
# .\cal_fiber_end_face_new.m:85
            f_2=[]
# .\cal_fiber_end_face_new.m:86
            f_3=[]
# .\cal_fiber_end_face_new.m:87
            for iii in arange(1,size(y,1)).reshape(-1):
                f_1=concat([f_1,find(concat([Surf.faces(1,arange()) + 1]) == y(iii))])
# .\cal_fiber_end_face_new.m:90
                f_2=concat([f_2,find(concat([Surf.faces(2,arange()) + 1]) == y(iii))])
# .\cal_fiber_end_face_new.m:91
                f_3=concat([f_3,find(concat([Surf.faces(3,arange()) + 1]) == y(iii))])
# .\cal_fiber_end_face_new.m:92
            f_indx_1=union(f_1,f_2)
# .\cal_fiber_end_face_new.m:95
            f_indx_1=union(f_indx_1,f_3)
# .\cal_fiber_end_face_new.m:96
            tmp_dist=pdist2(fiber_end_2.T,Surf.vertice.T)
# .\cal_fiber_end_face_new.m:99
            x,y=ind2sub(size(tmp_dist),find(tmp_dist <= nearest_face_thre),nargout=2)
# .\cal_fiber_end_face_new.m:100
            y=unique(y)
# .\cal_fiber_end_face_new.m:101
            f_1=[]
# .\cal_fiber_end_face_new.m:102
            f_2=[]
# .\cal_fiber_end_face_new.m:103
            f_3=[]
# .\cal_fiber_end_face_new.m:104
            for iii in arange(1,size(y,1)).reshape(-1):
                f_1=concat([f_1,find(concat([Surf.faces(1,arange()) + 1]) == y(iii))])
# .\cal_fiber_end_face_new.m:107
                f_2=concat([f_2,find(concat([Surf.faces(2,arange()) + 1]) == y(iii))])
# .\cal_fiber_end_face_new.m:108
                f_3=concat([f_3,find(concat([Surf.faces(3,arange()) + 1]) == y(iii))])
# .\cal_fiber_end_face_new.m:109
            f_indx_2=union(f_1,f_2)
# .\cal_fiber_end_face_new.m:111
            f_indx_2=union(f_indx_2,f_3)
# .\cal_fiber_end_face_new.m:112
            stop_flag=0
# .\cal_fiber_end_face_new.m:115
            cross_face_id=- 1
# .\cal_fiber_end_face_new.m:116
            if logical_not(isempty(f_indx_1)):
                for seg_id in arange(2,size(fiber_end_1,2)).reshape(-1):
                    seg_v1.x = copy(fiber_end_1(1,seg_id))
# .\cal_fiber_end_face_new.m:122
                    seg_v1.y = copy(fiber_end_1(2,seg_id))
# .\cal_fiber_end_face_new.m:122
                    seg_v1.z = copy(fiber_end_1(3,seg_id))
# .\cal_fiber_end_face_new.m:122
                    seg_v2.x = copy(fiber_end_1(1,seg_id - 1))
# .\cal_fiber_end_face_new.m:123
                    seg_v2.y = copy(fiber_end_1(2,seg_id - 1))
# .\cal_fiber_end_face_new.m:123
                    seg_v2.z = copy(fiber_end_1(3,seg_id - 1))
# .\cal_fiber_end_face_new.m:123
                    for ii in arange(1,size(f_indx_1,2)).reshape(-1):
                        face_id=f_indx_1(ii)
# .\cal_fiber_end_face_new.m:125
                        surf_vtx.x = copy(Surf.vertice(1,Surf.faces(1,face_id)))
# .\cal_fiber_end_face_new.m:127
                        surf_vtx.y = copy(Surf.vertice(2,Surf.faces(1,face_id)))
# .\cal_fiber_end_face_new.m:128
                        surf_vtx.z = copy(Surf.vertice(3,Surf.faces(1,face_id)))
# .\cal_fiber_end_face_new.m:129
                        surf_norm.x = copy(face_normal(1,face_id))
# .\cal_fiber_end_face_new.m:131
                        surf_norm.y = copy(face_normal(2,face_id))
# .\cal_fiber_end_face_new.m:132
                        surf_norm.z = copy(face_normal(3,face_id))
# .\cal_fiber_end_face_new.m:133
                        cross_output=seg_line_cross_surf(seg_v1,seg_v2,surf_vtx,surf_norm,SEG_THR)
# .\cal_fiber_end_face_new.m:136
                        if cross_output.cross_flag == 1:
                            tmp_vtx_1=Surf.vertice(arange(),Surf.faces(1,face_id))
# .\cal_fiber_end_face_new.m:139
                            tmp_vtx_2=Surf.vertice(arange(),Surf.faces(2,face_id))
# .\cal_fiber_end_face_new.m:140
                            tmp_vtx_3=Surf.vertice(arange(),Surf.faces(3,face_id))
# .\cal_fiber_end_face_new.m:141
                            tmp_center=concat([[cross_output.cross_vtx.x],[cross_output.cross_vtx.y],[cross_output.cross_vtx.z]])
# .\cal_fiber_end_face_new.m:143
                            if abs(triangle_area(tmp_center,tmp_vtx_1,tmp_vtx_2) + triangle_area(tmp_center,tmp_vtx_1,tmp_vtx_3) + triangle_area(tmp_center,tmp_vtx_2,tmp_vtx_3) - triangle_area(tmp_vtx_1,tmp_vtx_2,tmp_vtx_3)) < AREA_THR:
                                stop_flag=1
# .\cal_fiber_end_face_new.m:145
                                cross_face_id=copy(face_id)
# .\cal_fiber_end_face_new.m:146
                                break
                    if stop_flag == 1:
                        break
            if stop_flag == 1:
                output[1,fiber_id]=cross_face_id
# .\cal_fiber_end_face_new.m:161
            else:
                if stop_flag == logical_and(0,logical_not(isempty(f_indx_1))):
                    ## last try
                    direction=fiber_end_1(arange(),1) - fiber_end_1(arange(),2)
# .\cal_fiber_end_face_new.m:165
                    direction=direction / sqrt(sum(direction ** 2))
# .\cal_fiber_end_face_new.m:166
                    direction=dot(direction,end_length)
# .\cal_fiber_end_face_new.m:167
                    segment=fiber_end_1(arange(),1) + direction
# .\cal_fiber_end_face_new.m:168
                    seg_v1.x = copy(fiber_end_1(1,1))
# .\cal_fiber_end_face_new.m:170
                    seg_v1.y = copy(fiber_end_1(2,1))
# .\cal_fiber_end_face_new.m:170
                    seg_v1.z = copy(fiber_end_1(3,1))
# .\cal_fiber_end_face_new.m:170
                    seg_v2.x = copy(segment(1))
# .\cal_fiber_end_face_new.m:171
                    seg_v2.y = copy(segment(2))
# .\cal_fiber_end_face_new.m:171
                    seg_v2.z = copy(segment(3))
# .\cal_fiber_end_face_new.m:171
                    for ii in arange(1,size(f_indx_1,2)).reshape(-1):
                        face_id=f_indx_1(ii)
# .\cal_fiber_end_face_new.m:174
                        surf_vtx.x = copy(Surf.vertice(1,Surf.faces(1,face_id)))
# .\cal_fiber_end_face_new.m:176
                        surf_vtx.y = copy(Surf.vertice(2,Surf.faces(1,face_id)))
# .\cal_fiber_end_face_new.m:177
                        surf_vtx.z = copy(Surf.vertice(3,Surf.faces(1,face_id)))
# .\cal_fiber_end_face_new.m:178
                        surf_norm.x = copy(face_normal(1,face_id))
# .\cal_fiber_end_face_new.m:180
                        surf_norm.y = copy(face_normal(2,face_id))
# .\cal_fiber_end_face_new.m:181
                        surf_norm.z = copy(face_normal(3,face_id))
# .\cal_fiber_end_face_new.m:182
                        cross_output=seg_line_cross_surf(seg_v1,seg_v2,surf_vtx,surf_norm,SEG_THR)
# .\cal_fiber_end_face_new.m:184
                        if cross_output.cross_flag == 1:
                            tmp_vtx_1=Surf.vertice(arange(),Surf.faces(1,face_id))
# .\cal_fiber_end_face_new.m:187
                            tmp_vtx_2=Surf.vertice(arange(),Surf.faces(2,face_id))
# .\cal_fiber_end_face_new.m:188
                            tmp_vtx_3=Surf.vertice(arange(),Surf.faces(3,face_id))
# .\cal_fiber_end_face_new.m:189
                            tmp_center=concat([[cross_output.cross_vtx.x],[cross_output.cross_vtx.y],[cross_output.cross_vtx.z]])
# .\cal_fiber_end_face_new.m:191
                            if abs(triangle_area(tmp_center,tmp_vtx_1,tmp_vtx_2) + triangle_area(tmp_center,tmp_vtx_1,tmp_vtx_3) + triangle_area(tmp_center,tmp_vtx_2,tmp_vtx_3) - triangle_area(tmp_vtx_1,tmp_vtx_2,tmp_vtx_3)) < AREA_THR:
                                stop_flag=1
# .\cal_fiber_end_face_new.m:193
                                cross_face_id=copy(face_id)
# .\cal_fiber_end_face_new.m:194
                                break
                    if stop_flag == 1:
                        output[1,fiber_id]=cross_face_id
# .\cal_fiber_end_face_new.m:202
                    else:
                        output[1,fiber_id]=- 1
# .\cal_fiber_end_face_new.m:204
                else:
                    if stop_flag == logical_and(0,isempty(f_indx_1)):
                        output[1,fiber_id]=- 1
# .\cal_fiber_end_face_new.m:207
            ##+++++++++++++++ second end
            stop_flag=0
# .\cal_fiber_end_face_new.m:212
            cross_face_id=- 1
# .\cal_fiber_end_face_new.m:213
            if logical_not(isempty(f_indx_2)):
                for seg_id in arange(2,size(fiber_end_2,2)).reshape(-1):
                    seg_v1.x = copy(fiber_end_2(1,seg_id))
# .\cal_fiber_end_face_new.m:218
                    seg_v1.y = copy(fiber_end_2(2,seg_id))
# .\cal_fiber_end_face_new.m:218
                    seg_v1.z = copy(fiber_end_2(3,seg_id))
# .\cal_fiber_end_face_new.m:218
                    seg_v2.x = copy(fiber_end_2(1,seg_id - 1))
# .\cal_fiber_end_face_new.m:219
                    seg_v2.y = copy(fiber_end_2(2,seg_id - 1))
# .\cal_fiber_end_face_new.m:219
                    seg_v2.z = copy(fiber_end_2(3,seg_id - 1))
# .\cal_fiber_end_face_new.m:219
                    for ii in arange(1,size(f_indx_2,2)).reshape(-1):
                        face_id=f_indx_2(ii)
# .\cal_fiber_end_face_new.m:222
                        surf_vtx.x = copy(Surf.vertice(1,Surf.faces(1,face_id)))
# .\cal_fiber_end_face_new.m:224
                        surf_vtx.y = copy(Surf.vertice(2,Surf.faces(1,face_id)))
# .\cal_fiber_end_face_new.m:225
                        surf_vtx.z = copy(Surf.vertice(3,Surf.faces(1,face_id)))
# .\cal_fiber_end_face_new.m:226
                        surf_norm.x = copy(face_normal(1,face_id))
# .\cal_fiber_end_face_new.m:228
                        surf_norm.y = copy(face_normal(2,face_id))
# .\cal_fiber_end_face_new.m:229
                        surf_norm.z = copy(face_normal(3,face_id))
# .\cal_fiber_end_face_new.m:230
                        cross_output=seg_line_cross_surf(seg_v1,seg_v2,surf_vtx,surf_norm,0.1)
# .\cal_fiber_end_face_new.m:232
                        if cross_output.cross_flag == 1:
                            tmp_vtx_1=Surf.vertice(arange(),Surf.faces(1,face_id))
# .\cal_fiber_end_face_new.m:234
                            tmp_vtx_2=Surf.vertice(arange(),Surf.faces(2,face_id))
# .\cal_fiber_end_face_new.m:235
                            tmp_vtx_3=Surf.vertice(arange(),Surf.faces(3,face_id))
# .\cal_fiber_end_face_new.m:236
                            tmp_center=concat([[cross_output.cross_vtx.x],[cross_output.cross_vtx.y],[cross_output.cross_vtx.z]])
# .\cal_fiber_end_face_new.m:238
                            if abs(triangle_area(tmp_center,tmp_vtx_1,tmp_vtx_2) + triangle_area(tmp_center,tmp_vtx_1,tmp_vtx_3) + triangle_area(tmp_center,tmp_vtx_2,tmp_vtx_3) - triangle_area(tmp_vtx_1,tmp_vtx_2,tmp_vtx_3)) < AREA_THR:
                                stop_flag=1
# .\cal_fiber_end_face_new.m:240
                                cross_face_id=copy(face_id)
# .\cal_fiber_end_face_new.m:241
                                break
                    if stop_flag == 1:
                        break
            if stop_flag == 1:
                output[2,fiber_id]=cross_face_id
# .\cal_fiber_end_face_new.m:256
            else:
                if stop_flag == logical_and(0,logical_not(isempty(f_indx_2))):
                    ## last try
                    direction=fiber_end_2(arange(),end()) - fiber_end_2(arange(),end() - 1)
# .\cal_fiber_end_face_new.m:259
                    direction=direction / sqrt(sum(direction ** 2))
# .\cal_fiber_end_face_new.m:260
                    direction=dot(direction,end_length)
# .\cal_fiber_end_face_new.m:261
                    segment=fiber_end_2(arange(),end()) + direction
# .\cal_fiber_end_face_new.m:262
                    seg_v1.x = copy(fiber_end_2(1,end()))
# .\cal_fiber_end_face_new.m:264
                    seg_v1.y = copy(fiber_end_2(2,end()))
# .\cal_fiber_end_face_new.m:264
                    seg_v1.z = copy(fiber_end_2(3,end()))
# .\cal_fiber_end_face_new.m:264
                    seg_v2.x = copy(segment(1))
# .\cal_fiber_end_face_new.m:265
                    seg_v2.y = copy(segment(2))
# .\cal_fiber_end_face_new.m:265
                    seg_v2.z = copy(segment(3))
# .\cal_fiber_end_face_new.m:265
                    for ii in arange(1,size(f_indx_2,2)).reshape(-1):
                        face_id=f_indx_2(ii)
# .\cal_fiber_end_face_new.m:268
                        surf_vtx.x = copy(Surf.vertice(1,Surf.faces(1,face_id)))
# .\cal_fiber_end_face_new.m:270
                        surf_vtx.y = copy(Surf.vertice(2,Surf.faces(1,face_id)))
# .\cal_fiber_end_face_new.m:271
                        surf_vtx.z = copy(Surf.vertice(3,Surf.faces(1,face_id)))
# .\cal_fiber_end_face_new.m:272
                        surf_norm.x = copy(face_normal(1,face_id))
# .\cal_fiber_end_face_new.m:274
                        surf_norm.y = copy(face_normal(2,face_id))
# .\cal_fiber_end_face_new.m:275
                        surf_norm.z = copy(face_normal(3,face_id))
# .\cal_fiber_end_face_new.m:276
                        cross_output=seg_line_cross_surf(seg_v1,seg_v2,surf_vtx,surf_norm,SEG_THR)
# .\cal_fiber_end_face_new.m:278
                        if cross_output.cross_flag == 1:
                            tmp_vtx_1=Surf.vertice(arange(),Surf.faces(1,face_id))
# .\cal_fiber_end_face_new.m:281
                            tmp_vtx_2=Surf.vertice(arange(),Surf.faces(2,face_id))
# .\cal_fiber_end_face_new.m:282
                            tmp_vtx_3=Surf.vertice(arange(),Surf.faces(3,face_id))
# .\cal_fiber_end_face_new.m:283
                            tmp_center=concat([[cross_output.cross_vtx.x],[cross_output.cross_vtx.y],[cross_output.cross_vtx.z]])
# .\cal_fiber_end_face_new.m:285
                            if abs(triangle_area(tmp_center,tmp_vtx_1,tmp_vtx_2) + triangle_area(tmp_center,tmp_vtx_1,tmp_vtx_3) + triangle_area(tmp_center,tmp_vtx_2,tmp_vtx_3) - triangle_area(tmp_vtx_1,tmp_vtx_2,tmp_vtx_3)) < AREA_THR:
                                stop_flag=1
# .\cal_fiber_end_face_new.m:287
                                cross_face_id=copy(face_id)
# .\cal_fiber_end_face_new.m:288
                                break
                    if stop_flag == 1:
                        output[2,fiber_id]=cross_face_id
# .\cal_fiber_end_face_new.m:296
                    else:
                        output[2,fiber_id]=- 1
# .\cal_fiber_end_face_new.m:298
                else:
                    if stop_flag == logical_and(0,isempty(f_indx_2)):
                        output[2,fiber_id]=- 1
# .\cal_fiber_end_face_new.m:301
    
    output_2_file=concat([[concat([arange(1,size(Fibers,2))])],[output]]).T
# .\cal_fiber_end_face_new.m:308
    toc
    # save(output_fname,'output_2_file');

cal_fiber_end_face_new(Fibers,Surf,"result.mat")