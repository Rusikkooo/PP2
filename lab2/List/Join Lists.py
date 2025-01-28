# В Python существует несколько способов объединения или конкатенации двух или более списков.

# Один из самых простых способов — использование + оператора.

# There are several ways to join, or concatenate, two or more lists in Python.

# One of the easiest ways are by using the + operator.

list1 = [1 ,  2,  3 ]
list2 = ["a","b","c"]
list3 = list1+list2
print(list3)

# Другой способ объединения двух списков — добавить все элементы из списка list2 в список list1 по одному
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)

# method for extend():
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)