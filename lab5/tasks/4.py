import re
with open("row.txt") as f:
     txt = f.read()
    
x = r"[A-Z][a-z]+"
y = re.findall(x,txt)
print(y)

