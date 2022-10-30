oring_surf=load("./114621surface.mat").surface;
dic_data=load("./114621_net_01.mat").dic;
dic_len=size(dic_data,1);
node_len=size(dic_data,2);
Pdata=[]
% Pdata=size(dic_len)
for i=1:dic_len
    Pdata{i}.name="net_"+string(i)
    value=zeros(1,node_len);
    for j=1:node_len
        value(j)=dic_data(i,j);
    end
    Pdata{i}.val=value
end
Patch.Vtx=oring_surf.vertice;
Patch.Face=oring_surf.faces-1;
Patch.Pdata=Pdata;
vtkSurfWrite("114621_patch.vtk",Patch);
% save("./114621_patch.vtk")
 

