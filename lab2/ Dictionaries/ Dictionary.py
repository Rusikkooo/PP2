# Словари используются для хранения значений данных в парах ключ:значение.
# Словарь — это упорядоченная*, изменяемая и не допускающая дубликатов кол.
# Словари записываются в фигурных скобках и имеют ключи и значения:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

my_dict = {
    "brand" : "Ford",
    "Name" : "Rusik",
    "Age" : 13   
}
# String, int, boolean, and list data types:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# С точки зрения Python словари определяются как объекты с типом данных «dict»:
# <class 'dict'>

my_dict = {
    "Name" : "Rusik",
    "age" : 18,
    "city" : "aktobe",
    "job" : "IT"
}
print(type(my_dict))

# Также для создания словаря можно использовать конструктор dict() .
thisdict = dict(name = "Rusk",age = 34,city = "almaty")
print(thisdict)
