def myfunc(n):
    for i in range(n,-1,-1):
        yield i 
n = int(input("n:"))
for x in myfunc(n):
    print(x)    
        