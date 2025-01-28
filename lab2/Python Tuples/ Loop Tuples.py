thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
  

# Вы также можете перебирать элементы кортежа, ссылаясь на их индексные номера.

# Используйте функции range()и len()для создания подходящей итерации.

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
print("-----------------------")


thistuple = ("apple", "banana", "cherry")
i = 0
while len(thistuple)>i:
    print(thistuple[i])
    i+=1