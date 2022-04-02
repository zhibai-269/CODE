import scipy.io as sio
import numpy as np

#load
node = sio.loadmat('node.mat')
print(len(node["ans"][0][0][0].T))

fiber=sio.loadmat('fiber.mat')
# print((fiber ["ans"][0][0][1].T))
