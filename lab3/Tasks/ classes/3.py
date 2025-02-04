class Shape:
    def area(self):
        return 0
class Rectangle:
    
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def area(self):
        result = self.length*self.width
        return f"result = {result}"

length = int(input("Длина: "))
width  = int(input("Ширина: "))
x = Rectangle(length,width)
print(x.area())



