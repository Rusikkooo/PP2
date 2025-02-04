def is_polindrom(arr):
    
   return arr == arr[::-1]

arr = list(input("Напишите что нибудь:").split())
if is_polindrom(arr):
    print("This is a Polindrom")
else:
    print("This is not a Polindrom")