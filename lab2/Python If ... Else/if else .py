a = 33
b = 200
if b > a:
  print("b is greater than a")
  
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal") #elif

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")# else 

# Если вам нужно выполнить только один оператор, вы можете поместить его в ту же строку, что и оператор if.
if a > b: print("a is greater than b")

# Если вам нужно выполнить только один оператор, один для if и один для else, вы можете поместить их все в одну строку:
a = 2
b = 330
print("A") if a > b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True") # and 

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True") #or
  
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b") # not
  
# ifоператоры не могут быть пустыми, но если по какой-то причине у вас есть ifоператор без содержания, введите его, passчтобы избежать ошибки.
a = 33
b = 200
if b > a:
  pass

