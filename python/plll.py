from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

t = np.linspace(0, np.pi * 2, 100)
s = np.linspace(0, np.pi, 100)

t, s = np.meshgrid(t, s)
x = np.cos(t) * np.sin(s)
y = np.sin(t) * np.sin(s)
z = np.cos(s)
# z[>0]=0  # 截取球体的下半部分
ax = plt.subplot(111, projection='3d')
# ax = plt.subplot(121, projection='3d')
# ax.plot_wireframe(x, y, z)
# ax = plt.subplot(122, projection='3d')
# ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='rainbow')
# ax = plt.subplot(122, projection='3d')
ax.set_xlabel('x axis') #x轴名称
ax.set_ylabel('y axis') #y轴名称
ax.set_zlabel('z axis')
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='rainbow')
# plt.gca().set_box_aspect((2,2,1)) #设置坐标比例时2：2：1
plt.show()