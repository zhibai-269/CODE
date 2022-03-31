import scipy.io as sio
import numpy as np

#load
data = sio.loadmat('node.mat')
print(data["ans"][0][0][0].T)