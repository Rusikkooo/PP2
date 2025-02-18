# local scope 
def myfunc():
    x = 300
    print(x)

myfunc()

def rusik():
    x = 10
    def asik():
        print(x)
    asik()
rusik()


# у нас есть метод global:
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)

# Ключевое  nonlocal слово используется для работы с переменными внутри вложенных функций.

# Ключевое nonlocal слово делает переменную принадлежащей внешней функции.
def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal x
    x = "hello"
    myfunc2()
    return x

print(myfunc1())


import platform
x = dir(platform)
print(x)