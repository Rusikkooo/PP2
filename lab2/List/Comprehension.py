fruits = ['apple',"banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits :
    if "a" in x:
        newlist.append(x)
        
print(newlist)
    
# С помощью понимания списков вы можете сделать все это с помощью всего одной строки кода:
City = ['ast','alm','akx','petr','moskva']
newlist = [x for x in City if 'a' in  x]
print(newlist)

# Синтаксис
# newlist = [expression for item in iterable if condition == True]

NovyList = []
if x != "apple":
    NovyList.append(x)    
    print(NovyList)
    
    
    
# Выражение является текущим элементом в итерации, но это также и результат, которым вы можете манипулировать , прежде чем он станет элементом списка в новом списке:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)


fruits = ['aplle','kiwi','orange','mango','cgerry','banana',]
newlist = ['hello'for x in fruits]
print(newlist)


# Return the item if it is not banana, if it is banana return orange".


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x!="banana"else "orange" for x in fruits]
print(newlist)