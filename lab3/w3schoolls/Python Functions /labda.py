# Лямбда-функция — это небольшая анонимная функция.

# Лямбда-функция может принимать любое количество аргументов, но может иметь только одно выражение.

x = lambda a: a + 10
print(x(5))

x = lambda a , b : a+b
print(x(1,0))

x = lambda a,b,c: a+c+b
print(x(1,2,3))

# Зачем использовать лямбда-функции?
# Мощь лямбда-выражений лучше всего проявляется при их использовании в качестве анонимной функции внутри другой функции.

# Допустим, у вас есть определение функции, которая принимает один аргумент, и этот аргумент будет умножен на неизвестное число:
# Используйте это определение функции, чтобы создать функцию, которая всегда удваивает отправленное вами число:
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(33))

# или используйте одно и то же определение функции, чтобы создать обе функции в одной программе:
def func(n):
    return lambda a:a*n
mydoubler =  func(3)  
mytriper = func(9)

print(mydoubler(9))#9*3
print(mytriper(8))#8*9

