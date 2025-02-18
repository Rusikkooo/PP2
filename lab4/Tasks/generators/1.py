def s(n):
    for i in range(n+1):
        yield i ** 2
        
n = int(input("N:"))
for x in s(n):
    print(x)