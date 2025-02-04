# Наследование позволяет нам определить класс, который наследует все методы и свойства другого класса.
# Родительский класс — это класс, от которого наследуется, также называемый базовым классом.

# Дочерний класс — это класс, который наследует другой класс, также называемый производным классом.

# Создать родительский класс
# Создайте класс с именем Person, со firstnameс войствами lastname и printname методом

class Person :
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname,self.lastname)

x = Person("John","Doe")
x.printname()

# Cоздать Дочерный класс
# Чтобы создать класс, наследующий функциональность другого класса, отправьте родительский класс в качестве параметра при создании дочернего класса:
class Student(Person):
    pass

x = Student("Rusik","Myrzabayev")
x.printname()

class Student(Person):
    def __init__(self,fname,lname): 
        pass
# біз __init__ дегенді қосқан кезде , біз родительский класстан ажырап кеттік . новыйын создовать еттік.

# Чтобы создать класс, наследующий функциональность другого класса, отправьте родительский класс в качестве параметра при создании дочернего класса:
class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
        
# В Python также есть super()функция, которая позволяет дочернему классу унаследовать все методы и свойства от своего родителя:
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname,self.lastname)
        
class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
x = Student("Mike","Olsen")
x.printname()


# При использовании super()функции вам не обязательно использовать имя родительского элемента, он автоматически унаследует методы и свойства от своего родителя.
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)
