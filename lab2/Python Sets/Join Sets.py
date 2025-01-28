# В Python существует несколько способов объединения двух или более множеств.

# Методы union()и update()объединяют все элементы из обоих наборов.

# Метод intersection()сохраняет ТОЛЬКО дубликаты.

# Метод difference()сохраняет элементы из первого набора, которых нет в другом наборе(ах).

# Метод symmetric_difference()сохраняет все элементы, КРОМЕ дубликатов.


# method union:
set1 =  {'a','b','c','d'}
set2 = {1 , 2, 3, 4}
set3 = set1.union(set2)
print(set3)

# Вы можете использовать |оператор вместо union()метода и получите тот же результат.
set1 =  {'a','b','c','d'}
set2 = {1 , 2, 3, 4}
set3 = set1|set2
print(set3)

# Метод intersection()вернет новый набор, содержащий только те элементы, которые присутствуют в обоих наборах.
set1 =  {'a','b','c','d'}
set2 = {1 , 2, 3, 4,'a'}
set3 = set1.intersection(set2)
print(set3)

# Вы можете использовать &оператор вместо intersection()метода и получите тот же результат.
set1 =  {'a','b','c','d'}
set2 = {1 , 2, 3, 4,'b'}
set3 = set1&set2
print(set3)

# Метод intersection_update()также сохранит ТОЛЬКО дубликаты, но он изменит исходный набор вместо возврата нового набора.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

# Метод difference()вернет новый набор, который будет содержать только те элементы из первого набора, которых нет в другом наборе.
set1 = {1,2,3,4,5}
set2 ={'a','b','c','d',3}
set3 =set1.difference(set2)
print(set3)#Вы можете использовать -оператор вместо difference()метода и получите тот же результат.

# Метод symmetric_difference()сохранит только те элементы, которые НЕ присутствуют в обоих наборах.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)#Вы можете использовать ^оператор вместо symmetric_difference()метода и получите тот же результат

# Метод symmetric_difference_update()также сохранит все, кроме дубликатов, но он изменит исходный набор вместо возврата нового набора.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

