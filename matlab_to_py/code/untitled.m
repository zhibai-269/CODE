
filename=""
%[fiber,surface]=process("114823_32k_orig.vtk","114823_fiber_mrtrix_5W_SIFT_v2.vtk");
%
surface=load("E:\本科毕业设计\数据集\第一周\数据\matFile\surface.mat").surface;
data=load('E:\本科毕业设计\数据集\第一周\数据\matFile\begin_end_data.mat').begin_end_data;
edge_info=last_new_file(surface,data)
save("./matFile/edge_info.mat","edge_info")
key=load("./matFile/edge_info.mat").edge_info;
edge_info_key=keys(key);
save("./matFile/edge_keys.mat","edge_info_key")