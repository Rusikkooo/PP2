def convert_to_C(F):
    C = (5 / 9) * (F - 32)
    return C 
F = float(input("Enter the Fahrenheit temperature:"))
result = convert_to_C(F)
print(result)