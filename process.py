import scipy.io as sio
import numpy as np

#load
node = sio.loadmat('node.mat')
# print(len(node["ans"][0][0][0].T))

fiber=sio.loadmat('fiber.mat')
# print((fiber ["ans"][0][0][1].T))

maps=sio.loadmat("map_key.mat")
# for key in maps["map_key"][0]:
#     print(key)
print(len(maps["map_key"][0]))
# print(maps["map_key"])
