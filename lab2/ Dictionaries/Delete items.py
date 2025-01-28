# Метод pop()удаляет элемент с указанным именем ключа:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# Метод popitem()удаляет последний вставленный элемент (в версиях до 3.7 вместо этого удаляется случайный элемент):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# Ключевое delслово удаляет элемент с указанным именем ключа:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# Метод clear()очищает словарь:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)




