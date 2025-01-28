# Кортеж — это упорядоченная и неизменяемая коллекция :
myTuple=('a','b','c')
print(myTuple)

# Когда мы говорим, что кортежи упорядочены, это означает, что элементы имеют определенный порядок, и этот порядок не изменится.
# Кортежи неизменяемы, то есть мы не можем изменять, добавлять или удалять элементы после создания кортежа.

# Кортежи допускают повторяющиеся значения:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Чтобы определить количество элементов в кортеже, используйте len()функцию:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Чтобы создать кортеж, содержащий только один элемент, необходимо добавить запятую после элемента, иначе Python не распознает его как кортеж.
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Кортеж может содержать различные типы данных:
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

# Для создания кортежа также можно использовать конструктор tuple() :
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)