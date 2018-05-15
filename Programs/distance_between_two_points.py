import math
class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def __str__(self):
        my_str="point: ({0},{1},{2})".format(self.x,self.y,self.z)
        return my_str
    def distance(self,point1,point2):
        return math.sqrt((point2.x-point1.x)**2+(point2.y-point1.y)**2+(point2.z-point1.z)**2)

p1=Point(4,2,1)
p2=Point(5,2,1)
print(p1.distance(p1,p2))
