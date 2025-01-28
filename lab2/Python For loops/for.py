# Цикл for используется для итерации последовательности (которая является списком, кортежем, словарем, набором или строкой).

# Это меньше похоже на ключевое слово for в других языках программирования и работает скорее как метод итератора, который встречается в других объектно-ориентированных языках программирования.

# С помощью цикла for мы можем выполнить набор операторов, один раз для каждого элемента в списке, кортеже, наборе и т. д.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
for x in "banana":
  print(x)
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
for x in range(6):
  print(x) #range()




for x in range(6):
      print(x)
else:
  print("Finally finished!")
  
for x in range(6):
    if x == 3: break
    print(x)
else :
  print("Finally finished!")

# Вложенный цикл — это цикл внутри цикла.

# «Внутренний цикл» будет выполняться один раз для каждой итерации «внешнего цикла»:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
# forциклы не могут быть пустыми, но если по какой-то причине у вас есть forцикл без содержимого, вставьте passоператор, чтобы избежать возникновения ошибки.
for x in [0, 1, 2]:
  pass