"""
2. Для списка реализовать обмен значений соседних элементов,
   т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
   При нечетном количестве элементов последний сохранить на своем месте.
   Для заполнения списка элементов необходимо использовать функцию input().
"""
qty = input("Введите кол-во элементов списка:")
if not qty.isdigit():
    print('это не число')
    exit()
qty = int(qty)
my_list = []
i = 0
while i < qty:
    i += 1
    my_list.append(input(f"Введите значение элемента {i}: "))

i = 0
while i < qty//2:
    my_list[i + i], my_list[i + i + 1] = my_list[i + i + 1], my_list[i + i]
    i += 1
print(my_list)
