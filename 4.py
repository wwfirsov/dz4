list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
listdbl = list
print(f"Исходный список: {list}")
new_list = []
new_list = [el for el in list for i in listdbl if el != i] # ???

print(f"Новый список: {new_list}")