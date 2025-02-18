def sqares(m,n):
    for i in range(m,n+1):
        yield i**2
m = int(input("m:"))
n = int(input("n:"))    
for x in sqares(m,n):
    print(x)
    
