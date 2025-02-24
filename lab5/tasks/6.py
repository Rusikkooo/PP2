import re 
with open("row.txt") as f:
    txt = f.read()
y = re.sub("[" " , .]",":",txt)
print(y)