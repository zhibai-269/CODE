# def write_vtk_surface():
#将边信息写入到表面中
import scipy.io as sio

surface_mat="../matfile/surfaces/114823surface.mat"
surface=sio.loadmat(surface_mat)["surface"][0][0]
