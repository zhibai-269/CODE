function[output_2_file] = cal_fiber_end_face_new(Surf,Fibers)
%Surf : 用ReadSurf(name_surf,0,0)读出，faces索引是减一的，
%Fibers : ReadFiber(name_fiber,{}).fiber读出，里面的.fiber
% save current time
tic

% addpath '/disk2/three-hinge/Surface';
% addpath '/disk2/three-hinge/Fiber';
% addpath '/disk2/three-hinge/HCP_fiber';
% addpath '/disk2/three-hinge/dtiSurface/surface_rl';
% 
% input_surf_fname = sprintf('%d_dti_cluster_offset.vtk',subject_id);
% input_fiber_fname = sprintf('fiber%d_acs.vtk',subject_id);
% output_fname = sprintf('fiber_end_surface%d.mat',subject_id);
fiber_end_ratio =0.5;
%% fiber_end_ratio: % end points used to compute cross the surface % radius: the distance between searching vertex and fiber end
%% output vertex ID: C style
%% output file format: fiberID fiber-first-end vertex ID fiber-second-end vertex ID (-1 denotes fiber does not reach any vertex within radius)


%Surf=gpuArray(Surf)
%Fibers=gpuArray(Surf)

SEG_THR = 0.001;
AREA_THR = 0.001;

nearest_face_thre = 2;
end_length = 3;

% if ~exist(input_surf_fname,'file')        
%        
%     return
% else
%     Surf = ReadSurf(input_surf_fname,[],0);
% end
% 
% if isfield(input_fiber_fname,'vertice')
%     Fibers = input_fiber_fname.fiber;
% else
%     tmp = ReadFiber(input_fiber_fname,{});
%     Fibers = tmp.fiber;
%     
% end


%%++++++++++++++++++++++compute all face normal
face_normal = zeros(3,size(Surf.faces,2));
% Operate on each small triangle face
for face_id = 1:size(Surf.faces,2)
    %the three vertices of the triangle face
    vtx_1 = Surf.vertice(:,Surf.faces(1,face_id) );
    vtx_2 = Surf.vertice(:,Surf.faces(2,face_id) );
    vtx_3 = Surf.vertice(:,Surf.faces(3,face_id) );
    %Generate a unit vector perpendicular to the triangle face     
    vector_1 = vtx_1 - vtx_2;
    vector_2 = vtx_1 - vtx_3;
    tmp_norm = cross(vector_1,vector_2);
    tmp_norm = tmp_norm/sqrt(sum(tmp_norm.^2));
    face_normal(:,face_id) = tmp_norm;
end
%%++++++++++++++++++++++compute all face normal

output = zeros(2,size(Fibers,2));
% Operate on each fiber
for fiber_id = 1:size(Fibers,2)
    fiber_id
%     Determine whether the program is running and the degree of running
    if mod(fiber_id,10) == 1
%         The disp function will directly output the content in the Matlab command window
        disp(fiber_id/size(Fibers,2));
    end
    fiber = Fibers{fiber_id};
    if size(fiber,2) < 10
        output(1,fiber_id) = -1;
        output(2,fiber_id) = -1;
    else
        
        fiber_end_1 = fiber(:,1:round(size(fiber,2)*fiber_end_ratio));
        fiber_end_2 = fiber(:,round(size(fiber,2)*(1 - fiber_end_ratio)):end);
        
%         ??????
        %a'是a的转置矩阵，pdist2计算顶端fiber的点和所有vertice的距离矩阵
        tmp_dist = pdist2(fiber_end_1',Surf.vertice');
        %找到点之间距离小于阈值的下标，find找到的是索引，ind2sub转化成下标，x代表行，y代表列
        [x,y] = ind2sub(size(tmp_dist), find(tmp_dist <= nearest_face_thre));
        y = unique(y);
        f_1 = [];
        f_2 = [];
        f_3 = [];
        %记录下有符合标准的顶点穿过的三角形的索引
        for  iii = 1:size(y,1)
            f_1 = [f_1 find([Surf.faces(1,:)+1] == y(iii))];
            f_2 = [f_2 find([Surf.faces(2,:)+1] == y(iii))];
            f_3 = [f_3 find([Surf.faces(3,:)+1] == y(iii))];
        end
        %求所有三角形的并集
        f_indx_1 = union(f_1,f_2);
        f_indx_1 = union(f_indx_1,f_3);
        
        %对fiber尾端同样操作
        tmp_dist = pdist2(fiber_end_2',Surf.vertice');
        [x,y] = ind2sub(size(tmp_dist), find(tmp_dist <= nearest_face_thre));
        y = unique(y);
        f_1 = [];
        f_2 = [];
        f_3 = [];
        
        for  iii = 1:size(y,1)
            f_1 = [f_1 find([Surf.faces(1,:)+1] == y(iii))];
            f_2 = [f_2 find([Surf.faces(2,:)+1] == y(iii))];
            f_3 = [f_3 find([Surf.faces(3,:)+1] == y(iii))];
        end
        f_indx_2 = union(f_1,f_2);
        f_indx_2 = union(f_indx_2,f_3);
        
        %%+++++++++++++++ first end
        stop_flag = 0;
        cross_face_id = -1;
        
        if ~isempty(f_indx_1)
            
            for seg_id = 2:size(fiber_end_1,2)
                %把fiber前半段分成每两点之间的小线段
                seg_v1.x = fiber_end_1(1,seg_id);
                seg_v1.y = fiber_end_1(2,seg_id);
                seg_v1.z = fiber_end_1(3,seg_id);
                seg_v2.x = fiber_end_1(1,seg_id-1);
                seg_v2.y = fiber_end_1(2,seg_id-1);
                seg_v2.z = fiber_end_1(3,seg_id-1);
                for ii = 1:size(f_indx_1,2)
                    face_id = f_indx_1(ii);
                    %每一个起始三角形的第一个点
                    surf_vtx.x = Surf.vertice(1,Surf.faces(1,face_id));
                    surf_vtx.y = Surf.vertice(2,Surf.faces(1,face_id));
                    surf_vtx.z = Surf.vertice(3,Surf.faces(1,face_id));
                    %每个三角形的垂直单位向量
                    surf_norm.x = face_normal(1,face_id);
                    surf_norm.y = face_normal(2,face_id);
                    surf_norm.z = face_normal(3,face_id);
                    
                    %这个线段是否穿过小三角形，cross_output.cross_vtx：穿出的点，cross_output.cross_flag=1：穿过
                    cross_output = seg_line_cross_surf(seg_v1,seg_v2,surf_vtx,surf_norm,SEG_THR);
                    if cross_output.cross_flag == 1
                        
                        tmp_vtx_1 = Surf.vertice(:,Surf.faces(1,face_id));
                        tmp_vtx_2 = Surf.vertice(:,Surf.faces(2,face_id) );
                        tmp_vtx_3 = Surf.vertice(:,Surf.faces(3,face_id) );
                        
                        tmp_center = [cross_output.cross_vtx.x;cross_output.cross_vtx.y;cross_output.cross_vtx.z];
                        if  abs(triangle_area(tmp_center,tmp_vtx_1,tmp_vtx_2) + triangle_area(tmp_center,tmp_vtx_1,tmp_vtx_3) + triangle_area(tmp_center,tmp_vtx_2,tmp_vtx_3) - triangle_area(tmp_vtx_1,tmp_vtx_2,tmp_vtx_3)) < AREA_THR
                            stop_flag = 1;
                            cross_face_id = face_id;
                            break;
                        end
                    end                 
                end
                
                if stop_flag == 1
                    break;
                end
                
            end
            
        end
        
        if stop_flag == 1
            output(1,fiber_id) = cross_face_id;
        elseif stop_flag == 0 & ~isempty(f_indx_1)
            
            %% last try
            direction = fiber_end_1(:,1) - fiber_end_1(:,2);
            direction = direction/sqrt(sum(direction.^2));
            direction = direction * end_length;
            segment = fiber_end_1(:,1) + direction;
            
            seg_v1.x = fiber_end_1(1,1);seg_v1.y = fiber_end_1(2,1);seg_v1.z = fiber_end_1(3,1);
            seg_v2.x = segment(1);seg_v2.y = segment(2);seg_v2.z = segment(3);
            
            for ii = 1:size(f_indx_1,2)
                face_id = f_indx_1(ii);
                
                surf_vtx.x = Surf.vertice(1,Surf.faces(1,face_id));
                surf_vtx.y = Surf.vertice(2,Surf.faces(1,face_id));
                surf_vtx.z = Surf.vertice(3,Surf.faces(1,face_id));
                
                surf_norm.x = face_normal(1,face_id);
                surf_norm.y = face_normal(2,face_id);
                surf_norm.z = face_normal(3,face_id);
                
                cross_output = seg_line_cross_surf(seg_v1,seg_v2,surf_vtx,surf_norm,SEG_THR);
                if cross_output.cross_flag == 1
                    
                    tmp_vtx_1 = Surf.vertice(:,Surf.faces(1,face_id) );
                    tmp_vtx_2 = Surf.vertice(:,Surf.faces(2,face_id) );
                    tmp_vtx_3 = Surf.vertice(:,Surf.faces(3,face_id));
                    
                    tmp_center = [cross_output.cross_vtx.x;cross_output.cross_vtx.y;cross_output.cross_vtx.z];
                    if  abs(triangle_area(tmp_center,tmp_vtx_1,tmp_vtx_2) + triangle_area(tmp_center,tmp_vtx_1,tmp_vtx_3) + triangle_area(tmp_center,tmp_vtx_2,tmp_vtx_3) - triangle_area(tmp_vtx_1,tmp_vtx_2,tmp_vtx_3)) < AREA_THR
                        stop_flag = 1;
                        cross_face_id = face_id;
                        break;
                    end
                end
                
            end
            
            if stop_flag == 1
                output(1,fiber_id) = cross_face_id;
            else
                output(1,fiber_id) = -1;
            end
        elseif stop_flag == 0 & isempty(f_indx_1)
            output(1,fiber_id) = -1;
        end
        
        
        %%+++++++++++++++ second end
        stop_flag = 0;
        cross_face_id = -1;
        
        if ~isempty(f_indx_2)
            
            for seg_id = 2:size(fiber_end_2,2)
                seg_v1.x = fiber_end_2(1,seg_id);seg_v1.y = fiber_end_2(2,seg_id);seg_v1.z = fiber_end_2(3,seg_id);
                seg_v2.x = fiber_end_2(1,seg_id-1);seg_v2.y = fiber_end_2(2,seg_id-1);seg_v2.z = fiber_end_2(3,seg_id-1);
                for ii = 1:size(f_indx_2,2)
                    
                    face_id = f_indx_2(ii);
                    
                    surf_vtx.x = Surf.vertice(1,Surf.faces(1,face_id));
                    surf_vtx.y = Surf.vertice(2,Surf.faces(1,face_id));
                    surf_vtx.z = Surf.vertice(3,Surf.faces(1,face_id));
                    
                    surf_norm.x = face_normal(1,face_id);
                    surf_norm.y = face_normal(2,face_id);
                    surf_norm.z = face_normal(3,face_id);
                    
                    cross_output = seg_line_cross_surf(seg_v1,seg_v2,surf_vtx,surf_norm,0.1);
                    if cross_output.cross_flag == 1
                        tmp_vtx_1 = Surf.vertice(:,Surf.faces(1,face_id));
                        tmp_vtx_2 = Surf.vertice(:,Surf.faces(2,face_id) );
                        tmp_vtx_3 = Surf.vertice(:,Surf.faces(3,face_id));
                        
                        tmp_center = [cross_output.cross_vtx.x;cross_output.cross_vtx.y;cross_output.cross_vtx.z];
                        if  abs(triangle_area(tmp_center,tmp_vtx_1,tmp_vtx_2) + triangle_area(tmp_center,tmp_vtx_1,tmp_vtx_3) + triangle_area(tmp_center,tmp_vtx_2,tmp_vtx_3) - triangle_area(tmp_vtx_1,tmp_vtx_2,tmp_vtx_3)) < AREA_THR
                            stop_flag = 1;
                            cross_face_id = face_id;
                            break;
                        end
                    end
                    
                end
                if stop_flag == 1
                    break;
                end
                
            end
            
        end
        
        if stop_flag == 1
            output(2,fiber_id) = cross_face_id;
        elseif stop_flag == 0 & ~isempty(f_indx_2)
            %% last try
            direction = fiber_end_2(:,end) - fiber_end_2(:,end - 1);
            direction = direction/sqrt(sum(direction.^2));
            direction = direction * end_length;
            segment = fiber_end_2(:,end) + direction;
            
            seg_v1.x = fiber_end_2(1,end);seg_v1.y = fiber_end_2(2,end);seg_v1.z = fiber_end_2(3,end);
            seg_v2.x = segment(1);seg_v2.y = segment(2);seg_v2.z = segment(3);
            
            for ii = 1:size(f_indx_2,2)
                face_id = f_indx_2(ii);
                
                surf_vtx.x = Surf.vertice(1,Surf.faces(1,face_id));
                surf_vtx.y = Surf.vertice(2,Surf.faces(1,face_id));
                surf_vtx.z = Surf.vertice(3,Surf.faces(1,face_id));
                
                surf_norm.x = face_normal(1,face_id);
                surf_norm.y = face_normal(2,face_id);
                surf_norm.z = face_normal(3,face_id);
                
                cross_output = seg_line_cross_surf(seg_v1,seg_v2,surf_vtx,surf_norm,SEG_THR);
                if cross_output.cross_flag == 1
                    
                    tmp_vtx_1 = Surf.vertice(:,Surf.faces(1,face_id) );
                    tmp_vtx_2 = Surf.vertice(:,Surf.faces(2,face_id) );
                    tmp_vtx_3 = Surf.vertice(:,Surf.faces(3,face_id) );
                    
                    tmp_center = [cross_output.cross_vtx.x;cross_output.cross_vtx.y;cross_output.cross_vtx.z];
                    if  abs(triangle_area(tmp_center,tmp_vtx_1,tmp_vtx_2) + triangle_area(tmp_center,tmp_vtx_1,tmp_vtx_3) + triangle_area(tmp_center,tmp_vtx_2,tmp_vtx_3) - triangle_area(tmp_vtx_1,tmp_vtx_2,tmp_vtx_3)) < AREA_THR
                        stop_flag = 1;
                        cross_face_id = face_id;
                        break;
                    end
                end
                
            end
            
            if stop_flag == 1
                output(2,fiber_id) = cross_face_id;
            else
                output(2,fiber_id) = -1;
            end
        elseif stop_flag == 0 & isempty(f_indx_2)
            output(2,fiber_id) = -1;
        end
        
        
    end
end

output_2_file = [[1:size(Fibers,2)];output]';
toc

% save(output_fname,'output_2_file');