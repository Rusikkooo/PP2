import re

with open("/Users/ruslanmyrzabaev/Desktop/py/lab5/tasks/row.txt") as f:
    data =  f.read()
    
x = re.findall("ab*",data)
print(x)