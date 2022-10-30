function[] = vtkWrite_vertex(output_fname,vertex_coordinate)
fp=fopen(output_fname,'w');
if fp<=0
    error(['cannot open file ' fname_output 'for read']);
end
fprintf(fp,'# vtk DataFile Version 3.0\nmesh surface\nASCII\nDATASET POLYDATA\n');
fprintf(fp,'POINTS %d float\n',size(vertex_coordinate,2));
fprintf(fp, '%f %f %f\n',vertex_coordinate);
fclose(fp);