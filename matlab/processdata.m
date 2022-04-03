%surf=vtkSurfRead("114621_32k_orig.vtk")

%fiber=ReadFiber("114621_fiber_mrtrix_5W_SIFT_v2.vtk","[]")
%save fiber
load("surf.mat","surf")
load("data.mat","data")
% load("fiber.mat","fiber")
% data=cal_fiber_end_face_new(surf,fiber.fiber)
%save data


%data=load("data.mat")


%[INDEX,temp]=select_vertex(Surf.surf,2,0)

%[file1,file2]=cal_vertex_structual_1222(Surf.surf,data,INDEX,1);
[savedile]=last_new_file(surf,data)
%map_key=keys(load("result_map.mat").savedile)