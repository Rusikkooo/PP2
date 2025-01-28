# Вы можете перебирать словари с помощью forцикла.
# При циклическом переборе словаря возвращаемым значением являются ключи словаря, но существуют методы, позволяющие также возвращать значения 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
  

# Вывести все значения в словаре по одному:
for x in thisdict:
      print(thisdict[x])
  
# Вы также можете использовать values()метод для возврата значений словаря:
for x in thisdict.values():
  print(x)
  
  
# keys()Для возврата ключей словаря можно использовать метод:
for x in thisdict.keys():
  print(x)
  
# Переберите ключи и значения , используя items()метод:
for x, y in thisdict.items():
  print(x, y)