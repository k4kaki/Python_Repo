import math
class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def add_(self,p1,p2):
        return(p1.x+p2.x,p1.y+p2.y,p1.z+p2.z)
p1=Point(4,2,1)
p2=Point(5,2,1)
my_str="Added point is "
print("Added point is :",p1.add_(p1,p2))