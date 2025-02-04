# Напишите функцию, которая принимает строку от пользователя и распечатайте все перестановки этой строки.
from itertools import permutations
def print_all_perm(x):
    all_perm = permutations(x)
    for y in all_perm:
        print("".join(y))
x = str(input("Please enter  your string:"))
print_all_perm(x)