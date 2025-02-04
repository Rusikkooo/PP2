import math 
def volume_of_sphere(r):
    p = 3.14
    V = (4/3)*p*(pow(r,3))
    return V 
r = float(input("please enter the radius : "))
print(volume_of_sphere(r))