"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
   вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""


print("Введите текст. Для окончания введите пустую строку")
data = []

while True:
    new_str = input()
    if new_str == '':
        break
    data.append(new_str + '\n')

with open("task01.txt", "w") as file_obj:
        file_obj.writelines(data)
