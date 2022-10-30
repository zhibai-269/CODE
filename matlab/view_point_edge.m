function [] = view_point_edge(matrix_edge, vertex_index, surface_name, fiber_name, save_name_v, save_name_e)

    Surf = vtkSurfRead(surface_name)
    present_vertex = Surf.vertice(:, vertex_index);
    
    vtkWrite_vertex(save_name_v,present_vertex);
    
    Fiber = ReadFiber(fiber_name,[]);
    count= 1;
    fiber= {};
    for i = 1:size(matrix_edge,2) - 1
        for j = i + 1:size(matrix_edge,2)
            if(matrix_edge (i,j)~= 0)
                fiber{count} = [present_vertex(:,i), present_vertex(:,j)];
                count = count + 1;
            end
        end
    end
    Fiber.fiber = fiber
    WriteFiber(Fiber,save_name_e,0);
end
