% Generate vertex-fiber matrix
function[save_map] = cal_vertex_structual_1222(Surf,output_file)
% subject_id: the id of subject;
% j: the INDEX number

tic

% distance: The distance of the fiber passing through the vertex from the fixed point

distance = 0.9;

% index=output_file(:,2)==-1||output_file(:,2)==-1;
% output_file(index,:)=[];
% size(output_file)

vertices = Surf.vertice;

save_file= uint16(zeros(size(vertices+1,2),3));
save_map=containers.Map()
% vertex_structual = zeros(size(vertices,2),size(vertices,2));
% vertex_structual = uint16(vertex_structual);
% Vertex_Structual = cell(size(vertices,2),size(vertices,2));
%
count=1
for i = 1:size(output_file,1)
    
    i
    if output_file(i,2) == -1 || output_file(i,3) == -1
        continue;
    end
    head_face = output_file(i,2);
%   head_cor : The head vertice where the fiber pass
% 
    head_cor = (Surf.vertice(:,Surf.faces(1,head_face) ) + Surf.vertice(:,Surf.faces(2,head_face) ) + Surf.vertice(:,Surf.faces(3,head_face) )) /3;
    tail_face = output_file(i,3);
%   tail_cor : The tail vertice where the fiber pass  
    tail_cor = (Surf.vertice(:,Surf.faces(1,tail_face) ) + Surf.vertice(:,Surf.faces(2,tail_face) ) + Surf.vertice(:,Surf.faces(3,tail_face) )) /3;
%   head_num : Number of vertices around the head of fiber  
    head_num = 0;
%   tail_num : Number of vertices around the tail of fiber  
    tail_num = 1;
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
    if(tail_num>1&&head_num>1)
        for j = 1:head_num
            for l = 1:tail_num
                % vertex_structual(head_vertex(j),tail_vertex(l)) = vertex_structual(head_vertex(j),tail_vertex(l)) + 1;
                % vertex_structual(tail_vertex(l),head_vertex(j)) = vertex_structual(tail_vertex(l),head_vertex(j)) + 1;
                % Vertex_Structual{head_vertex(j),tail_vertex(l)}(end+1) = i;
                % save_file(count,1)=head_vertex(j);
                name=[num2str(head_vertex(j)),'+',num2str(tail_vertex(l))];
                if (isKey(save_map,name))
                    save_map(name)=save_map(name)+1;
                else
                    save_map(name)=1;
                end

            end
        end
    end
    count=count+1;
    
end
toc
end