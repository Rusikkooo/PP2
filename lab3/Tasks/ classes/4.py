import math
class Point:
    
    def __init__(self,x,y): 
        self.x = x
        self.y = y
        
    def show(self):
        return self.x , self.y
    
    def move(self,dx,dy):
        self.x+=dx
        self.y+=dy
        
    def dist(self,other_point):
        distance = math.sqrt((x2-x)**2+(y2-y)**2)
        return distance 
    
x = int(input("X  координаты: "))
y = int(input("Y  координаты: "))
d = Point(x,y)
print("Coordinates: " , d.show())

dx = int(input("Изменение по X: "))
dy = int(input("Изменение по Y: "))
d.move(dx,dy)
print("New Coordinates: " ,d.show())

x2 = int(input("X второй точки: "))
y2 = int(input("Y второй точки: "))
other_point = Point(x2, y2)
print("Distance: ",d.dist(other_point))