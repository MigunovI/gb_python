"""
3. Создать текстовый файл (не программно), построчно записать
   фамилии сотрудников и величину их окладов (не менее 10 строк).
   Определить, кто из сотрудников имеет оклад менее 20 тыс.,
   вывести фамилии этих сотрудников.
   Выполнить подсчет средней величины дохода сотрудников.

   Пример файла:

   Иванов 23543.12
   Петров 13749.32
"""


with open("task03.txt", "r", encoding="utf-8") as file_obj:
    lines = file_obj.readlines()


lines_dict = {k: float(v) for k, v in [line.split() for line in lines]}
filtered_lines = {k: v for k, v in lines_dict.items() if v < 20000}

if len(filtered_lines) > 0:
    print("Сотрудникик с окладом менее 20 тыс.:")
    for el in filtered_lines:
        print(el)

avg_salary = sum(lines_dict.values()) / len(lines_dict)
print(f"Средняя величина дохода сотрудников: {avg_salary:<0.2f}")
