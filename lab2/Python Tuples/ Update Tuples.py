# Кортежи неизменяемы , поэтому вы не можете удалять из них элементы, но вы можете использовать тот же обходной путь, который мы использовали для изменения и добавления элементов кортежа:
tuple1 = (1,2,3,4,5)
y = list(tuple1)
y.append(6)
tuple1 = tuple(y)
print(tuple1)

# Ключевое delслово может полностью удалить кортеж:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists