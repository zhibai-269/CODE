function Fiber = ReadFiber(fname,label_tag)
%% extract the label_tag feature
Fiber = struct;
Fiber.fiber = {};
Fiber.vertice = {};
Fiber.POINT_DATA = struct;
Fiber.CELL_DATA = struct;
Fiber.POINT_DATA.SCALARS = {};
Fiber.POINT_DATA.VECTORS = {};
Fiber.CELL_DATA.SCALARS = {};
Fiber.CELL_DATA.VECTORS = {};

fiber = [];
vtx = [];
fid = fopen(fname,'rt');
s = fscanf(fid,'%s',1);
while(~strcmp(s,'POINTS'))
   s = fscanf(fid,'%s',1);  
end
vtxNum = fscanf(fid,'%d',1);
if vtxNum <= 0
    return;
end
s = fscanf(fid,'%s',1);
vtx = fscanf(fid,'%f',[3,vtxNum]);
Fiber.vertice = vtx;
s = fscanf(fid,'%s',1);
fiberNum = fscanf(fid,'%d',1);
s = fscanf(fid,'%d',1);
for i = 1:fiberNum
    s = fscanf(fid,'%d',1);
    tem = fscanf(fid,'%d',s);
    tem = (tem+1)';
%     fiber{i} = tem+1;
    Fiber.fiber{i} = vtx(:,tem);%for matlab index
end

if(~isempty(label_tag))
    if(isfield(label_tag,'POINT_DATA'))
        s = fscanf(fid,'%s',1);
        while(~strcmp(s,'POINT_DATA'))
            s = fscanf(fid,'%s',1);
        end 
        if(~isempty(label_tag.POINT_DATA))
            if(isfield(label_tag.POINT_DATA,'SCALARS'))         
                if(~isempty(label_tag.POINT_DATA.SCALARS))
                    for i = 1:size(label_tag.POINT_DATA.SCALARS,2)
                        s = fscanf(fid,'%s',1);
                        while(~strcmp(s,label_tag.POINT_DATA.SCALARS{i}))
                            s = fscanf(fid,'%s',1);
                        end   
                        s = fscanf(fid,'%s',3);
                        Fiber.POINT_DATA.SCALARS{i} = fscanf(fid,'%f',vtxNum)';
                    end
                end
            end           

            if(isfield(label_tag.POINT_DATA,'VECTORS'))
                 if(~isempty(label_tag.POINT_DATA.VECTORS))
                    for i = 1:size(label_tag.POINT_DATA.VECTORS,2)
                        s = fscanf(fid,'%s',1);
                        while(~strcmp(s,label_tag.POINT_DATA.VECTORS{i}))
                            s = fscanf(fid,'%s',1);
                        end   
                        s = fscanf(fid,'%s',1);
                        tmp = fscanf(fid,'%f',vtxNum*3);
                        Fiber.POINT_DATA.VECTORS{i} = reshape(tmp,3,vtxNum);
                    end            
                end           
            end

        end       
    end

    if(isfield(label_tag,'CELL_DATA'))
        if(~isempty(label_tag.CELL_DATA))
            if(isfield(label_tag.CELL_DATA,'SCALARS'))
                 if(~isempty(label_tag.CELL_DATA.SCALARS))
                    for i = 1:size(label_tag.CELL_DATA.SCALARS,2)
                        s = fscanf(fid,'%s',1);
                        while(~strcmp(s,label_tag.CELL_DATA.SCALARS{i}))
                            s = fscanf(fid,'%s',1);
                        end   
                        s = fscanf(fid,'%s',3);
                        Fiber.CELL_DATA.SCALARS{i} = fscanf(fid,'%f',fiberNum)';
                    end

                end           
            end
            if(isfield(label_tag.CELL_DATA,'VECTORS'))
                 if(~isempty(label_tag.CELL_DATA.VECTORS))
                    for i = 1:size(label_tag.CELL_DATA.VECTORS,2)
                        s = fscanf(fid,'%s',1);
                        while(~strcmp(s,label_tag.CELL_DATA.VECTORS{i}))
                            s = fscanf(fid,'%s',1);
                        end   
                        s = fscanf(fid,'%s',1);
                        tmp = fscanf(fid,'%f',Face_num*3);
                        Fiber.CELL_DATA.VECTORS{i} = reshape(tmp,3,fiberNum);
                    end            
                end                 
            end
      
        end        
    end

end

fclose(fid);

