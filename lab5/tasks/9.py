import re 
txt = "HelloWorldAiIsAmazing"
y = re.findall(r"[A-Z][a-z]*",txt)
print(y)
