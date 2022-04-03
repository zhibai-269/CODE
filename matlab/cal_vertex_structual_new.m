% Generate vertex-fiber matrix
function[] = cal_vertex_structual_new(INDEX,subject_id,j)
% subject_id: the id of subject;
% j: the INDEX number

tic

addpath 'G:\matlab\workspace\function';
addpath 'G:\wang\new_postgraduate\fiber';
addpath 'G:\wang\new_postgraduate\surface';
addpath 'G:\wang\new_postgraduate\caiyang\result_mat_1';
save_path = 'G:\wang\new_postgraduate\collect_fiber_2\';

% distance: The distance of the fiber passing through the vertex from the fixed point
distance = INDEX{2,j}/2;
input_surf_fname = sprintf('%d_dti_cluster_offset.vtk',subject_id);
input_fiber_end_file = sprintf('fiber_end_surface%d.mat',subject_id);



% input_index = sprintf('obj_%d_dis_INDEX.mat',subject_id);
% load(input_index);


if ~exist(input_fiber_end_file,'file')        
        return
else
    load(input_fiber_end_file);
end
Surf = ReadSurf(input_surf_fname,[],0);
vertices = Surf.vertice(:,INDEX{1,j});
vertex_structual = zeros(size(vertices,2),size(vertices,2));
vertex_structual = uint16(vertex_structual);
Vertex_Structual = cell(size(vertices,2),size(vertices,2));
%
for i = 1:size(output_2_file,1)
    i
    if output_2_file(i,2) == -1 || output_2_file(i,3) == -1
        continue;
    end
    head_face = output_2_file(i,2);
%   head_cor : The head vertice where the fiber pass
    head_cor = (Surf.vertice(:,Surf.faces(1,head_face) + 1) + Surf.vertice(:,Surf.faces(2,head_face) + 1) + Surf.vertice(:,Surf.faces(3,head_face) + 1)) /3;
    tail_face = output_2_file(i,3);
%   tail_cor : The tail vertice where the fiber pass  
    tail_cor = (Surf.vertice(:,Surf.faces(1,tail_face) + 1) + Surf.vertice(:,Surf.faces(2,tail_face) + 1) + Surf.vertice(:,Surf.faces(3,tail_face) + 1)) /3;
%   head_num : Number of vertices around the head of fiber  
    head_num = 0;
%   tail_num : Number of vertices around the tail of fiber  
    tail_num = 0;
    for j = 1:size(vertices,2)
       
        vertex_cor = vertices(:,j);
%         
        if(norm(head_cor - vertex_cor) < distance)
            head_num = head_num + 1;
%             head_vertex : The indexs of vertices around the head of fiber
            head_vertex(head_num) = j;
        end
        if(norm(tail_cor - vertex_cor) < distance)
            tail_num = tail_num + 1;
%             tail_vertex : The indexs of vertices around the tail of fiber
            tail_vertex(tail_num) = j;
        end        
    end
    
    for j = 1:head_num
        for l = 1:tail_num
            vertex_structual(head_vertex(j),tail_vertex(l)) = vertex_structual(head_vertex(j),tail_vertex(l)) + 1;
            vertex_structual(tail_vertex(l),head_vertex(j)) = vertex_structual(tail_vertex(l),head_vertex(j)) + 1;
            Vertex_Structual{head_vertex(j),tail_vertex(l)}(end+1) = i;
        end
    end
    
end
output_fname = sprintf('fiber_end_surface_obj%d_u%s.mat',subject_id,num2str(distance));
save([save_path output_fname],'vertex_structual','Vertex_Structual')
toc
end