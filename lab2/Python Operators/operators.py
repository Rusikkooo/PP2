print(10+5)

x = 2
x &= 3
print(x)

x = 9
x|=3
print(x) 

x = 112
x>>=1
print(x)

x = 223
x<<=2
print(x)

x=99
x^=33
print(x)

x = 0
print(x := 5)  # Айнымалы x = 5 болады, нәтижеде экранда 5 шығады

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is y)
print(x is z)
print(x == y)
print(x is not y)

x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list
