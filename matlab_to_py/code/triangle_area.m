function s = triangle_area(vtx_1,vtx_2,vtx_3)
e_1_2 = sqrt(sum((vtx_1 - vtx_2).^2));
e_2_3 = sqrt(sum((vtx_2 - vtx_3).^2));
e_1_3 = sqrt(sum((vtx_3 - vtx_1).^2));
p = (e_1_2 + e_2_3 + e_1_3)/2;
s = sqrt(p*(p - e_1_2)*(p - e_2_3)*(p - e_1_3));