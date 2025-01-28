# Создать набор:
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Повторяющиеся значения будут игнорироваться:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# значения True и 1считаются одинаковыми в наборах и рассматриваются как дубликаты:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# Чтобы определить, сколько элементов в наборе, используйте len() функцию:
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Каков тип данных набора?
myset = {"apple", "banana", "cherry"}
print(type(myset))

# Для создания набора также можно использовать конструктор set() .
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)