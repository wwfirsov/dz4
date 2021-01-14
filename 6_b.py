from itertools import cycle

start = input("Введите значение: ")

c = 0
for el in cycle(start):
    if c >= len(start):
        break
    print(el)
    c += 1
