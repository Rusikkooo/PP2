# To remove an item in a set, use the remove(), or the discard() method.
set1 = {"qwerty","lambda","arman"}
set1.remove("qwerty")
print(set1) #Примечание: если удаляемый элемент не существует, remove()возникнет ошибка.

# Удалить «банан» можно следующим способом discard() :
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) #если удаляемый элемент не существует, ошибка discard()НЕ​​возникнет .

# Метод clear() очищает набор:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# Ключевое delслово полностью удалит набор:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)