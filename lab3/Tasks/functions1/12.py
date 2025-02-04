def histogram(a):
    for i in range(len(a)):
        print(a[i] * "*")
a = list(map(int,input("Please enter your int number : ").split()))
histogram(a)
        