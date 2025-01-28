# Вы не можете скопировать словарь, просто набрав dict2 = dict1, поскольку: dict2будет только ссылкой на dict1, а изменения, внесенные в , dict1автоматически будут внесены и в dict2.

# Есть несколько способов сделать копию, один из которых — использовать встроенный метод словаря copy().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict) #copy()

# Другой способ сделать копию — использовать встроенную функцию dict().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)