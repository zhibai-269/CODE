
matrix_edge=load("../new_result/matfile/structual_min_matrix.mat").matrix;
vertex_index=load("../new_result/matfile/hub_index.mat").hub_index;
surface_name="../matfile/surface_vtk_file/114621_input_surface.vtk";
fiber_name="../matfile/115017_input_fiber.vtk";
save_name_v="../new_result/structual_result_vtk/114621surface_withhub.vtk";
save_name_e="../new_result/structual_result_vtk/114621fiber_withhub.vtk";
view_point_edge(matrix_edge, vertex_index, surface_name, fiber_name, save_name_v, save_name_e);


%Fiber = ReadFiber(fiber_name,[]);
surface_na="D:/material/114621_32k_orig.vtk"
name="../new_result/structual_result_vtk/114621_oringin_expect_nodes.vtk"

 Surf = vtkSurfRead(surface_na)
 %取出不包含fix_index的点
   %  present_vertex = Surf.vertice(:,~fix_indexs);
   present_vertex = Surf.vertice(:,fix_indexs_no);
   
    
    vtkWrite_vertex(name,present_vertex);
    
   % Fiber = ReadFiber(fiber_name,[]);