# Python — объектно-ориентированный язык программирования.

# Почти все в Python является объектом со своими свойствами и методами.

# A Class is like an object constructor, or a "blueprint" for creating objects.

# Создайте класс с именем MyClass и свойством с именем x:
class MyClass:
      x = 5#свойства
print(MyClass)

# Теперь мы можем использовать класс MyClass для создания объектов:]

# Создайте объект с именем p1 и выведите значение x:
p1 = MyClass()
print(p1.x)

# У всех классов есть функция __init__(), называемая , которая всегда выполняется при инициализации класса.
# Используйте __init__()функцию для присвоения значений свойствам объекта или других операций, которые необходимо выполнить при создании объекта:

class Person:
     def __init__(self,name,age):
        self.name =name 
        self.age = age 
p1 = Person("Rusik",18)
print(p1.name)
print(p1.age)

# Примечание: функция __init__()вызывается автоматически каждый раз, когда класс используется для создания нового объекта.


# Функция __str__()контролирует, что должно быть возвращено, когда объект класса представлен в виде строки.
# Если __str__()функция не задана, возвращается строковое представление объекта:

class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age 
    
    def __str__(self):
        return f"{self.name}({self.age})"
p1 = Person("John",36)
print(p1)

# Объекты также могут содержать методы. Методы в объектах — это функции, которые принадлежат объекту.
class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    def myfunc(self):
        print("Hello my name is " + self.name)
        
p1 = Person("John",36)
p1.myfunc()



# Параметр self
# Примечание: параметр selfявляется ссылкой на текущий экземпляр класса и используется для доступа к переменным, принадлежащим классу.

# Его не обязательно называть self, вы можете называть его как угодно, но он должен быть первым параметром любой функции в классе:
class Person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name = name
        mysillyobject.age = age 
    def myfunc(abc):
        print("Hello , my name is " + abc.name)
    p1 = Person("Rusik",18)
    p1.myfunc()
    
    
    
# Изменить свойства объекта
class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    def myF(self):
        print("Hello my name is " + self.name)
p1 = Person("john",34)
p1.age = 40 
print(p1.age)
p1.myF()

# classОпределения не могут быть пустыми, но если по какой-то причине у вас есть classопределение без содержания, вставьте passоператор, чтобы избежать возникновения ошибки.
class Person:
      pass

    