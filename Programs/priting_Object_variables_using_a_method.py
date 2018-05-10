class Point:
    
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def __str__(self):
        my_str="point: ({0},{1},{2})".format(self.x,self.y,self.z)
        return my_str

p1=Point(4,2,1)
print(p1)
