from itertools import count

start = int(input("Введите начальное число: "))
stop = int(input("Когда остановиться?: "))

for el in count(start):
    if el > stop:
        break
    else:
        print(el)
