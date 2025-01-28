# Доступ к элементам словаря можно получить, указав его ключевое имя в квадратных скобках:
thisdict = {
  "name": "Ford",
  "model": "Mustang",
  "year": 1964
}
r = thisdict["name"]
print(r)

# Существует также метод get(), который даст вам тот же результат:
x = thisdict.get("model")
print(x)

# Метод keys()вернет список всех ключей в словаре.
x = thisdict.keys()
print(x)

# Список ключей представляет собой представление словаря, то есть любые изменения, внесенные в словарь, будут отражены в списке ключей.
car  = {
    "name" : "toyota" ,
    "nomer" : "085EBA" ,
    "year" : "2024" 
}
print(car)#before the change
car['color'] = 'black'
print(car) #after the change

# Метод values()вернет список всех значений в словаре.
x = thisdict.values()
print(x)

# Метод items()вернет каждый элемент словаря в виде кортежей в списке.
x = thisdict.items()
print(x)

# Возвращаемый список представляет собой представление элементов словаря, то есть любые изменения, внесенные в словарь, будут отражены в списке элементов.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

# Чтобы определить, присутствует ли указанный ключ в словаре, используйте inключевое слово:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")