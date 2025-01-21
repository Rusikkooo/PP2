print(10>9)
print(10==9)
print(10<9)

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
    
print(bool("hello"))
print(bool(15))

x = "hello"
y = 15 
print(bool(x))
print(bool(y))

print(bool("abs"))
print(bool(123))
print(bool(["apple","cherry","banana"]))

print(bool(False)) #вернет значение false 
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

def my_func(x) :
    return True 
print(my_func(False))

def b():
    return False
if b():
    print("hello")
else:
    print("world")
    
x = 200
print(isinstance(x, bool))