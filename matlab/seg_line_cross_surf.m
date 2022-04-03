function output = seg_line_cross_surf(seg_v1,seg_v2,surf_vtx,surf_norm,cross_thre)
%seg_v1,seg_v2:线段的两个端点；surf_vtx,surf_norm:三角形的一个顶点和一个垂直单位向量

line_direction.x = seg_v1.x - seg_v2.x;
line_direction.y = seg_v1.y - seg_v2.y;
line_direction.z = seg_v1.z - seg_v2.z;
temp = 0;
temp = (surf_vtx.x - seg_v1.x)*surf_norm.x + (surf_vtx.y - seg_v1.y)*surf_norm.y + (surf_vtx.z - seg_v1.z)*surf_norm.z;
temp = temp/(line_direction.x*surf_norm.x + line_direction.y*surf_norm.y + line_direction.z*surf_norm.z + eps);
cross_vtx.x = temp*line_direction.x + seg_v1.x;
cross_vtx.y = temp*line_direction.y + seg_v1.y;
cross_vtx.z = temp*line_direction.z + seg_v1.z;

if (Dist_2_vtx(cross_vtx,seg_v1) + Dist_2_vtx(cross_vtx,seg_v2) - Dist_2_vtx(seg_v1,seg_v2) < cross_thre)
    cross_flag = 1;
else
    cross_flag = 0;
end

output.cross_vtx = cross_vtx;
output.cross_flag = cross_flag;
end

%两点之间的欧式距离
function distance = Dist_2_vtx(vtx_1,vtx_2)

distance = [vtx_1.x;vtx_1.y;vtx_1.z] - [vtx_2.x;vtx_2.y;vtx_2.z];
distance = distance.^2;
distance = sqrt(sum(distance));
end
