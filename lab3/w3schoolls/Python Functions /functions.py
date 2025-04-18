# Функция — это блок кода, который выполняется только при вызове.

# Вы можете передавать данные, называемые параметрами, в функцию.

# Функция может возвращать данные в качестве результата.
def my_func():
    d = "hello"
    print(d)
my_func()
# Информация может передаваться в функции в качестве аргументов.

# Аргументы указываются после имени функции, внутри скобок. Вы можете добавить столько аргументов, сколько захотите, просто разделяя их запятой.

# В следующем примере есть функция с одним аргументом (fname). Когда функция вызывается, мы передаем имя, которое используется внутри функции для вывода полного имени:
def x(name):
    print(name + " Rus")
x("aslan")
x("clever")
x("big")

# Параметр — это переменная, указанная в скобках в определении функции.
# Аргумент — это значение, которое отправляется функции при ее вызове.

# Эта функция ожидает 2 аргумента и получает 2 аргумента:
def my_func(fname,sname):
    print(fname + " " + sname )
my_func("Myrzabayev","Ruslan")

# Если вы не знаете, сколько аргументов будет передано вашей функции, добавьте *перед именем параметра в определении функции.
# Таким образом, функция получит кортеж аргументов и сможет получить доступ к элементам соответствующим образом:
def r(*kids):
     print("The youngest child is " + kids[1])
r("e","h","ff")

# Вы также можете отправлять аргументы с помощью синтаксиса ключ = значение .
# В этом случае порядок аргументов не имеет значения.
def k(c1,c2,c3):
    print(int((c1/c2)+c3))
k(c2 = 3,c1 = 4,c3 = 5)

# Если вы не знаете, сколько ключевых аргументов будет передано в вашу функцию, добавьте две звездочки: **перед именем параметра в определении функции.
# Таким образом, функция получит словарь аргументов и сможет получить доступ к элементам соответствующим образом:
def myfunc(**kw):
    print("my university is "+ kw["tunik"])
myfunc(funik = "ATU",sunik="SDU",tunik="KBTU")

# В следующем примере показано, как использовать значение параметра по умолчанию.

# Если мы вызываем функцию без аргумента, она использует значение по умолчанию:

# Пример
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Вы можете отправить в функцию аргумент любого типа данных (строку, число, список, словарь и т. д.), и внутри функции он будет рассматриваться как тот же тип данных.
# Например, если вы отправляете список в качестве аргумента, он все равно будет списком, когда достигнет функции:
def m(food):
    for x in food :
        print(x)
fruits = ["alma","almurt","banana"]
m(fruits)

# Чтобы функция возвращала значение, используйте return оператор:
def n(m):
    return 9*m
print(n(5))
print(n(4))
print(n(3))

# functionОпределения не могут быть пустыми, но если по какой-то причине у вас есть functionопределение без содержания, вставьте passоператор, чтобы избежать возникновения ошибки.
def myfunction():
      pass

# Вы можете указать, что функция может иметь ТОЛЬКО позиционные аргументы или ТОЛЬКО ключевые аргументы.
# Чтобы указать, что функция может иметь только позиционные аргументы, добавьте , / после аргументов:
def myfunc(x,/):
    print(x)

# Вы можете объединить два типа аргументов в одной функции.

# Все аргументы до являются / ,только позиционными, а все аргументы после являются *, только ключевыми словами.
def my_function(a, b, /, *, c, d):
      print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)


    
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results:")
tri_recursion(6)