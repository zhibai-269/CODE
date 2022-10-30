function [fiber,surface]=processdata(fibername,surfacename)

surface=vtkSurfRead(fibername);
fiber=ReadFiber(surfacename,[]);
save("./matFile/surface.mat","surface")
save("./matFile/fiber.mat","fiber")
begin_end_data=cal_fiber_end_face_new(surface,fiber.fiber)
save("./matFile/begin_end_data.mat","begin_end_data")
edge_info=last_new_file(surface,begin_end_data)
save("edge_info.mat","edge_info")

end
