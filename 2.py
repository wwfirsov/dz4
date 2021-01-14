list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f"Исходный список: {list}")
new_list = []
new_list = [el for el in list if el < list(el+1)] # как обратиться к следующему значению списка?

print(f"Новый список: {new_list}")