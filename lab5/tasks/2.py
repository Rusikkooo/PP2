import re

with open("/Users/ruslanmyrzabaev/Desktop/py/lab5/tasks/row.txt") as f:
    data =  f.read()

x = re.findall("ab{2,3}",data)
print(x)
