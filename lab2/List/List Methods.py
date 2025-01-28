# append()	Adds an element at the end of the list:
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("append :" , fruits)

# clear()	Removes all the elements from the list:
list1 = ["a","s"]
list1.clear()
print("clear:",list1)

# copy()	Returns a copy of the list:
list1 = ["ast","alm","akt","shym"]
list2 = list1.copy()
print("copy :",list2)

# count()	Returns the number of elements with the specified value:
list1 = ["adde","wdeef","efwerverv","wvewrvrew"]
cnt = list1.count("wdeef")
print("cnt :",cnt)

# extend()	Add the elements of a list (or any iterable), to the end of the current list:
list1 = ["adde","wdeef","efwerverv","wvewrvrew"]
fruits = ["apple", "banana", "cherry"]
list1.extend(fruits)
print("extend:",list1)

# index()	Returns the index of the first element with the specified value
fruits = ["apple", "banana", "cherry"]
i = fruits.index("banana")
print("index:",i)

# insert()	Adds an element at the specified position:
fruits = ["apple", "banana", "cherry"]
fruits.insert(2,"mandarin")
print("insert: ",fruits)

# pop()	Removes the element at the specified position:
list1 = ["ast","alm","akt","shym"]
list1.pop(2)
print("pop: ", list1)