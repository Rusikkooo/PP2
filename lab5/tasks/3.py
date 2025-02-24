import re 
with open("row.txt") as f:
    txt = f.read()

pattern = r'[a-z]_[a-z]'
result = re.findall(pattern,txt)
print(result)