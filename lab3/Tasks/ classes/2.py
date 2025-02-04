class Shape:
    def __init__(self):
        self.Shape_of_area = 0  
    
    def area(self):
        print(f"Площадь фигуры - {self.Shape_of_area}")

class Square(Shape):
    def __init__(self):
        super().__init__() 
        self.len = int(input("Введите длину квадрата: "))  
        self.Shape_of_area = self.len * self.len  
    
    def printarea(self):
        return f"Площадь квадрата равно {self.Shape_of_area}"

x = Square()

print(x.printarea())  
        
        