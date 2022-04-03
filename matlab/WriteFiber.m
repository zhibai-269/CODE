function WriteFiber(Fiber,fname,label_tag)
    %% point_Label.scalar.data  point_Label.scalar.name
    %% point_Label.vector.data  point_Label.vector.name
    %% cell_Label.scalar.data  cell_Label.scalar.name
    %% cell_Label.vector.data  cell_Label.vector.name
    
    vtx = [];
    fib = [];
    fid = fopen(fname,'wt');
    fprintf(fid,'# vtk DataFile Version 3.0\n');
    fprintf(fid,'Fiber point_L_C\n');
    fprintf(fid,'ASCII\n');
    fprintf(fid,'DATASET POLYDATA\n');
    if iscell(Fiber.fiber)&~isempty(Fiber.fiber)
        Num = size(Fiber.fiber,2);
        for mm = 1:Num
            tem = Fiber.fiber{mm};
            vtx = [vtx,tem];
            fib = [fib;size(tem,2)];
        end
        fprintf(fid,'POINTS %d float\n',size(vtx,2));
        fprintf(fid,'%f %f %f\n',vtx);
        fprintf(fid,'LINES %d %d\n',Num,sum(fib)+Num);
        indx = 0;
        for k = 1:Num
            fprintf(fid,'%d',fib(k));
            for kk = 1:fib(k)
                fprintf(fid,' %d',indx);
                indx = indx + 1;
            end
            fprintf(fid,'\n');
        end  
    elseif ~isempty(Fiber.fiber)
        fprintf(fid,'POINTS %d float\n',size(Fiber.fiber,2)*size(Fiber.fiber,3));
        fprintf(fid,'%f %f %f\n',reshape(Fiber.fiber,3,size(Fiber.fiber,2)*size(Fiber.fiber,3)));
        lines = 0:size(Fiber.fiber,2)*size(Fiber.fiber,3)-1;
        lines = reshape(lines,size(Fiber.fiber,2),size(Fiber.fiber,3));
        lines = [ones(size(Fiber.fiber,3),1)*size(Fiber.fiber,2) lines'];
        fprintf(fid,'LINES %d %d\n',size(Fiber.fiber,3),size(Fiber.fiber,2)*size(Fiber.fiber,3)+size(Fiber.fiber,3));
        for i = 1:size(lines,1)
            for j = 1:size(lines,2)
                fprintf(fid,'%d ',lines(i,j));
            end
            fprintf(fid,'\n');
        end
        vtx = reshape(Fiber.fiber,3,size(Fiber.fiber,2)*size(Fiber.fiber,3));
    else
        fprintf(fid,'POINTS 0 float\n');
       
        fprintf(fid,'LINES 0 0\n');       
    end

    if ~isempty(label_tag)
        if(isfield(label_tag,'POINT_DATA'))
            if ~isempty(label_tag.POINT_DATA)
                fprintf(fid,'POINT_DATA %d\n',size(vtx,2));
                if(isfield(label_tag.POINT_DATA,'SCALARS'))
                    if ~isempty(label_tag.POINT_DATA.SCALARS)
                        for i = 1:size(label_tag.POINT_DATA.SCALARS,2)
                            temp = Fiber.POINT_DATA.SCALARS{i};
                            fprintf(fid,'SCALARS %s float\n',label_tag.POINT_DATA.SCALARS{i});
                            fprintf(fid,'LOOKUP_TABLE %sTable\n',label_tag.POINT_DATA.SCALARS{i});
                            fprintf(fid,'%f\n',temp);
                        end
                    end                    
                end
                if(isfield(label_tag.POINT_DATA,'VECTORS'))
                    if ~isempty(label_tag.POINT_DATA.VECTORS)
                        for i = 1:size(label_tag.POINT_DATA.VECTORS,2)
                            temp = Fiber.POINT_DATA.VECTORS{i};
                            temp = (temp - min(min(temp)))./(max(max(temp)) - min(min(temp)));
                            fprintf(fid,'VECTORS %s unsigned_char\n',label_tag.POINT_DATA.VECTORS{i});
                            fprintf(fid,'%d %d %d\n',round(temp*255));     
                        end
                    end                    
                end

            end            
        end
        if(isfield(label_tag,'CELL_DATA'))
            if ~isempty(label_tag.CELL_DATA)
               fprintf(fid,'CELL_DATA %d\n',size(fiber,2));
               if(isfield(label_tag.CELL_DATA,'SCALARS'))
                   if ~isempty(label_tag.CELL_DATA.SCALARS)
                       for i = 1:size(label_tag.CELL_DATA.SCALARS,2)
                           temp = Fiber.CELL_DATA.SCALARS{i};
                           fprintf(fid,'SCALARS %s float\n',label_tag.CELL_DATA.SCALARS{i});
                           fprintf(fid,'LOOKUP_TABLE %sTable\n',label_tag.CELL_DATA.SCALARS{i});
                           fprintf(fid,'%f\n',temp);
                       end
                   end                   
               end
               if(isfield(label_tag.CELL_DATA,'VECTORS'))
                   if ~isempty(label_tag.CELL_DATA.VECTORS)
                       for i = 1:size(label_tag.CELL_DATA.VECTORS,2)
                           temp = Fiber.CELL_DATA.VECTORS{i}
                           fprintf(fid,'VECTORS %s unsigned_char\n',label_tag.CELL_DATA.VECTORS{i});
                           fprintf(fid,'%d %d %d\n',round(temp*255));
                       end 
                   end
               end

            end            
        end
        
    end
    
    
    fclose(fid);
    
    