# RegEx или регулярное выражение — это последовательность символов, образующая шаблон поиска.
# RegEx можно использовать для проверки того, содержит ли строка указанный шаблон поиска.
import re
# Найдите строку, чтобы увидеть, начинается ли она с «The» и заканчивается ли на «Spain»:
txt = "The rain in Spain"
a = re.search("The.*Spain$",txt)
if a:
    print("Ия, таптым")
else:
    print("жоқ,таппадым")
    
    
 # Модуль reпредлагает набор функций, позволяющий нам искать строку на предмет совпадения:
x = "bugingi kunge rakhmeеt"
j = re.search("bugingi",x)
k = re.findall(" ",x)
j = re.split("i",x)
o = re.sub("i","o",x)
print(j[0])
print(k)
print(j)
print(o)

txt = "the rain in Spain"
x = re.findall("[a-m]",txt)
print(x)

txt = "That will be 58 dollars"
x = re.findall("\d",txt)
print(x)  ##Find all digit characters:

txt = "hello Ruslan"
x = re.findall("..o",txt)
print(x)

with open("/Users/ruslanmyrzabaev/Desktop/py/lab5/tasks/row.txt") as f:
    data = f.read()
x = re.findall("a..bb",data)
print(x)