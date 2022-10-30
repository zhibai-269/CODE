filepath="/disk1/wjunx/data/HCP900/"
% fiber=vtkSurfRead(filepath)
persons=[ "119732","123420","127933" ,"130619" ,"133928"]
for i= persons
    display(i)
    fibername=filepath+i+"/input_surface.vtk";
    surfacename=filepath+i+"/input_fiber.vtk"
    surface=vtkSurfRead(fibername);
    fiber=ReadFiber(surfacename,[]);
    save("/disk1/haiyang/matFile/"+i+"surface.mat","surface")
    save("/disk1/haiyang/matFile/"+i+"fiber.mat","fiber")
    begin_end_data=cal_fiber_end_face_new(surface,fiber.fiber);
    save("/disk1/haiyang/matFile/"+i+"begin_end_data.mat","begin_end_data")
    
    
    %edge_info=last_new_file(surface,begin_end_data)
    %save(i+"edge_info.mat","edge_info")
    % edge_key=keys(edge_info);
     %save("/disk1/haiyang/matFile/"+i+"keys.mat","edge_key")

end