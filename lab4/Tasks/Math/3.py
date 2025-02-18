import math
n = int(input("сторона: "))#number of sides
a = int(input("длина сторона: ")) #length of a side
d = math.tan(math.pi/n)
s = int((n*pow(a,2))/(4*d))
print(s)