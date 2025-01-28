# Словарь может содержать словари, это называется вложенными словарями.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
# Чтобы получить доступ к элементам вложенного словаря, используйте имя словарей, начиная с внешнего словаря:
print(myfamily["child2"]["name"])

# Вы можете выполнить цикл по словарю, используя items()следующий метод:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])

