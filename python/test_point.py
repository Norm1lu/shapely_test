from shapely import box, LineString, normalize, Polygon,Point,MultiPoint
from shapely.geometry import Point
from shapely import geometry as geo
# print(pt_buf)
from shapely import affinity
import os
import numpy as np
from numpy import random
import matplotlib.pyplot as plt  # as将这个库重命名为plt
import shape_test
plt.figure()
plt.grid()
plt.gca().set_aspect(1)
plt.xlim(-600,600)
plt.ylim(-260,600)
box1 = box(-420, 0, 420, 420) #交集求一半
box2 = box(-420, 0, 420, -420) #交集求一半
a = Point(0, 0).buffer(420) 
a=a.intersection(box1)
b = Point(-220, 0).buffer(200) 
b=b.intersection(box2)

c = Point(220, 0).buffer(200) 
c= c.intersection(box2)
d = Point(0, 0).buffer(62)
e = Point(0, -187).buffer(187)
# e=b.difference(e)
# gc = geo.GeometryCollection([a, b,c])
gc= a.union(b)
gc=gc.union(c)
b=b.difference(e)
c=c.difference(e)
gc=gc.difference(d)
x0,y0=a.boundary.xy
x1,y1=b.boundary.xy
x2,y2=c.boundary.xy
x3,y3=d.boundary.xy
x4,y4=e.boundary.xy
x5,y5=gc.boundary.xy
# x6,y6=gc.contains_xy
x=np.random.uniform(-420,420,(30000,))
y=np.random.uniform(-200,420,(30000,))
points = [geo.Point(i,j) for i,j in zip(x,y)]
multipoints = geo.MultiPoint(points) 
    
point4=multipoints.intersection(gc)
# plt.plot(x,y,'o',color='grey')
# plt.plot(x0,y0,label="xuanzhuan",linestyle="dotted",color="red")
# plt.plot(x1,y1,label="chushi",linestyle="--",color="blue")
# plt.plot(x2,y2,label="chushi",linestyle="--",color="blue")
# plt.plot(x3,y3,label="chushi",linestyle="--",color="blue")
# plt.plot(x4,y4,label="chushi",linestyle="--",color="blue")
plt.plot(x5,y5,label="moving range ",linestyle="--",color="black")
print(len(point4.geoms))
for i in range(len(point4.geoms)):
    mm=shape_test.point_rotate_test(point4.geoms[i].x,point4.geoms[i].y,-20)
    if mm==0 :
        plt.plot(point4.geoms[i].x,point4.geoms[i].y,'o',color='red')
    if mm==1:
        plt.plot(point4.geoms[i].x,point4.geoms[i].y,'o',color='yellow')
    if mm==2:
        plt.plot(point4.geoms[i].x,point4.geoms[i].y,'o',color='green')
        
plt.legend(loc="best")  # 设置图例位置
plt.show()
