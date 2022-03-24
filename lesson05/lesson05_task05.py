"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
   разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
   выводить ее на экран.
"""

line = input('Введите числа, разделенные пробелом: ')
with open("task05.txt", "w", encoding="utf-8") as file_obj:
    file_obj.write(line)

with open("task05.txt", "r", encoding="utf-8") as file_obj:
    line = file_obj.readline()

result = 0
for el in line.split():
    try:
        result += int(el)
    except ValueError:
        continue
print(f'Сумма всех чисел: {result}')
