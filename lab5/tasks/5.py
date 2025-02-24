import re
with open("row.txt") as f:
     txt = f.read()
    
x = r"a.*b"
y = re.findall(x,txt)
print(y)