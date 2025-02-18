from datetime import datetime  
x = input("Введите первую дату: ")
y = input("Введите вторую дату: ")
date1 = datetime.strptime(x, "%Y.%m.%d")
date2 = datetime.strptime(y, "%Y.%m.%d")
result = abs((date2 - date1).total_seconds())
print(f"Разница между датами: {result} секунд")




