file_path="D:\PROJECT\CODE/matfile/surface_vtk_file/114621_input_surface.vtk"
surf=vtkSurfRead(file_path);
sulc_data=surf.Pdata{6}
save("sulc_data","sulc_data")