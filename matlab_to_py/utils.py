def sub2ind(array_shape, rows, cols):

    ind = rows*array_shape[1] + cols

    ind[ind < 0] = -1

    ind[ind >= array_shape[0]*array_shape[1]] = -1

    return ind

def ind2sub(array_shape, ind):
    rows = (ind.astype('int') / array_shape[1])
    cols = (ind.astype('int') % array_shape[1]) # or numpy.mod(ind.astype('int'), array_shape[1])
    return (rows, cols)
# def find(array, value):
#     return np.where(array == value)
def seg_line_cross_surf(seg_v1,seg_v2,surf_vtx,surf_norm,cross_thre):
    pass