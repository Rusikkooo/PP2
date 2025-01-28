# Когда мы создаем кортеж, мы обычно присваиваем ему значения. Это называется «упаковкой» кортежа:
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# Packing a tuple:
fruits = ("apple", "banana", "cherry")

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
# Но в Python нам также разрешено извлечь значения обратно в переменные. Это называется «распаковка»:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Использование Астериск*
# Если количество переменных меньше количества значений, вы можете добавить *к имени переменной, и значения будут присвоены переменной в виде списка:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
print("------------------------------")
# Если звездочка добавлена ​​к другому имени переменной, отличному от последнего, Python будет присваивать значения переменной до тех пор, пока количество оставшихся значений не совпадет с количеством оставшихся переменных.
fruits = ["apple", "banana", "cherry", "strawberry", "raspberry"]
(green,*yellow,black) = fruits
print(green)
print(yellow)
print(black)


