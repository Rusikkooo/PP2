my_list = list(map(int,input("Please enter your numbers:").split()))
def filter_prime(my_list):
    prime_list = []
    is_prime = True
    for x in my_list:
        if x<2:
            continue
        elif x>=2:
            for i in range(2,int(x**0.5)+1):
                if x%i==0:
                    is_prime = False 
                else :
                    is_prime = True
        if is_prime:
            prime_list.append(x)

    return prime_list

result = filter_prime(my_list)
print(result)