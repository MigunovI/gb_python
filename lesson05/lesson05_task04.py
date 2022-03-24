"""
4. Создать (не программно) текстовый файл со следующим содержимым:
   One — 1
   Two — 2
   Three — 3
   Four — 4

   Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
   При этом английские числительные должны заменяться на русские.
   Новый блок строк должен записываться в новый текстовый файл.
"""

dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}


def translate(text):
    for key, val in dictionary.items():
        text = text.replace(key, val)
    return text


with open("task04.txt", "r", encoding="utf-8") as file_obj:
    lines = file_obj.readlines()
rus_lines = [translate(el) for el in lines]
with open("task04_rus.txt", "x", encoding="utf-8") as file_obj:
    file_obj.writelines(rus_lines)
