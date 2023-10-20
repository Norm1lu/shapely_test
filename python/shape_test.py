# from shapely import box, LineString, normalize, Polygon
# from shapely.geometry import Point
# from numpy import asarray
# import numpy as np
# from shapely import LinearRing, LineString, MultiPoint, Point
# from shapely import MultiLineString
# import math
# point = Point(0.0, 0)
# point2=Point(0,0)
# pt_buf = point.buffer(1)
# pt_buf=pt_buf.boundary
# # print(pt_buf)
# # a = Point(1, 1).buffer(1.5)
# # b = Point(2, 1).buffer(1.5)

# box1 = box(-1, -1, 1, 1).boundary
# # box1=box1.boundary
# temp=pt_buf.intersects(box1)
# if(temp==1):
#     point1=pt_buf.intersection(box1)
#     print(len(point1.geoms))
# # line = MultiPoint(point1)
# # print(line.disjoint(pt_buf))
# # plt.figure()
# # plt.plot(x1, y1)
# # plt.plot(x2, y2)
# # plt.show()
#     print(point1)
#     point3=point1.geoms[1]
#     length1=point2.distance(point1.geoms[0])
#     length2=point2.distance(point1.geoms[1])
#     length3=point1.geoms[0].distance(point1.geoms[1])
# # list(point1.coords)
# # lines = LineString(point1)
#     print("length1:",length1,"lenght2:",length2,"length3:",length3)
#     degreen=math.acos((length3*length3-length1*length1-length2*length2)/(-2*length2*length1))
#     print
#     degree1 = math.degrees(math.acos(length1 / (point.y - point1.geoms[0].y)))
#     print("jiaodu:",math.degrees(degreen))

from shapely import box, LineString, normalize, Polygon,Point
from shapely.geometry import Point
# print(pt_buf)
from shapely import affinity
import os
import numpy as np
import matplotlib.pyplot as plt  # as将这个库重命名为plt
def point_rotate_test(x,y,start_angel) :
    point1=Point(0,200)
    box2 = box(-100, -200, 100, 0) #柱子位置大小
    # 设置当前位置
    # 画方形块旋转其位置
    box1 = box(point1.x-50, point1.y-20, point1.x+50, point1.y+150)
    x0,y0=box1.boundary.xy
    angle_now=start_angel#读取当前角度位置
    angle_bias =20 
    rotated_a = affinity.rotate(box1, angle_now+angle_bias,point1)
    x1,y1=rotated_a.boundary.xy
    # 读取目标点位初始位置平移过去，判断平移会不会碰撞
    target_point=Point(x,y)
    transform_a=affinity.translate(rotated_a,target_point.x-point1.x,target_point.y-point1.y)
    line = LineString([(1, 3), (1, 1), (4, 1)])
    x2,y2=transform_a.boundary.xy
    x3,y3=box2.boundary.xy
    # plt.figure()
    # plt.grid()
    # plt.gca().set_aspect(1)
    # plt.xlim(-600,600)
    # plt.ylim(-200,600)
    # plt.plot(x0,y0,label="chushi",linestyle="--",color="blue")
    # plt.plot(x1,y1,label="xuanzhuan",linestyle="dotted",color="red")
    # plt.plot(x2,y2,label="pingyi",linestyle=":",color="blue")
    # plt.plot(x3,y3,label="zhuzi",linestyle="-",color="green")
    # plt.legend(loc="best")  # 设置图例位置

    temp=transform_a.intersects(box2)
    print("temp",temp)
    if temp==1:
        point1=transform_a.boundary.intersection(box2.boundary)
        print(point1)
        return_state=0
        # plt.plot(point1.geoms[0].x,point1.geoms[0].y)
    else:
        transform_c= transform_a
        angle=0
        angle2=0
        while transform_a.intersects(box2)==False:
            transform_c= affinity.rotate(transform_a, angle,target_point,False)
            angle=angle+1
            x4,y4=transform_c.boundary.xy
            
            # print("aaaaa")
            if transform_c.intersects(box2)==True:
                print("angle:",angle+angle_bias) 
                return_state=2
                # plt.plot(x4,y4,label="target",linestyle="-",color="grey")
                break
            if angle>360 : 
                return_state=1 
                break
        while transform_a.intersects(box2)==False:
            transform_c= affinity.rotate(transform_a, angle2,target_point,False)
            angle2=angle2-1
            x5,y5=transform_c.boundary.xy
            
            # print("bbbbb")
            if transform_c.intersects(box2)==True:
                print("angle2:",angle2-angle_bias) 
                return_state=1
                # plt.plot(x5,y5,label="target",linestyle="-",color="grey")
                break
            if angle2<-360 :
                return_state=2
                break
    return return_state       
    # plt.show()
if __name__ == '__main__' :  #写在这个语句下的所有代码都不会被调用，只在本文件中运行
    point_rotate_test(100,100,10)
    # print(c)
# point1=pt_buf.intersection(box1)
# print(len(point1.geoms))
# rotated_b = affinity.rotate(line, 90, point1)
# print(rotated_a)
