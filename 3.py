generator = (param for param in range(20, 240) if param % 20 == 0 or param % 21 == 0)

for el in generator:
    print(el)