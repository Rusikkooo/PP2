# Вы не можете скопировать список, просто набрав list2 = list1, поскольку: list2будет только ссылкой на list1, а изменения, внесенные в , list1автоматически будут также внесены в list2.

# copy()Для копирования списка можно использовать встроенный метод List .
list1 = ["apple", "banana", "cherry"]
list2 = list1.copy()
print(list2)

# Другой способ сделать копию — использовать встроенный метод list().
list1 = ["apple", "banana", "mandarin"]
list2 =list(list1)
print(list2)

# Вы также можете сделать копию списка, используя :оператор (срез).
# You can also make a copy of a list by using the : (slice) operator.

list1 = ["apple", "banana", "cherry"]
list2 = list1[:]
print(list2)