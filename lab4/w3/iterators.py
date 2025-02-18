# Итератор — это объект, содержащий счетное количество значений.
# Итератор — это объект, который можно итерировать, то есть можно перебирать все значения.
# Итератор 2 методтан тұрады :  __iter__() и __next__().

# Итератор против итерируемого
# Списки, кортежи, словари и множества — все это итерируемые объекты. Это итерируемые контейнеры , из которых можно получить итератор.
# Все эти объекты имеют iter()метод, который используется для получения итератора:
my_typle  = ("apple","banana","cherry")
myit = iter(my_typle)
print(next(myit))
print(next(myit))
print(next(myit))

# Строки также являются итерируемыми объектами, содержащими последовательность символов:
mystr = "banana class"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))



# Чтобы создать объект/класс как итератор, вам необходимо реализовать методы __iter__()и __next__()для вашего объекта.
# Как вы узнали из главы «Классы/объекты Python» , у всех классов есть функция с именем __init__(), которая позволяет выполнять инициализацию при создании объекта.
# Метод __iter__()действует аналогично, вы можете выполнять операции (инициализацию и т. д.), но всегда должны возвращать сам объект итератора.
# Метод __next__()также позволяет выполнять операции и должен возвращать следующий элемент в последовательности.
class Myclass:
    def  __iter__(self):
        self.a = 1
        return self 
    def __next__(self):
        x  = self.a 
        self.a+=1
        return x 
    
myNumbers = Myclass()
myiter = iter(myNumbers)
while(False):
    print(next(myiter))
    
# Чтобы предотвратить бесконечное повторение, мы можем использовать #StopIteration# оператор.
# В __next__()методе мы можем добавить условие завершения, чтобы вызвать ошибку, если итерация будет выполнена указанное количество раз:
# Остановка после 20 итераций:
class Rusik():
    def __iter__(self):
        self.a = 1 
        return self
    def __next__(self):
        if self.a<=99:
            x = self.a
            self.a+=1
            return x 
        else:
            raise StopIteration
        
asik = Rusik()
myiter = iter(asik)    

for x in myiter:
  print(x)