"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
   Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
   нуля в качестве делителя программа должна корректно обработать эту ситуацию и
   не завершиться с ошибкой.
"""


class DivisionOnZero(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    input_a = input("Введите делимое: ")
    try:
        input_a = int(input_a)
    except ValueError:
        print("Вы ввели не число")
    else:
        break


while True:
    input_b = input("Введите делитель: ")
    try:
        input_b = int(input_b)
        if input_b == 0:
            raise DivisionOnZero("Вы ввели 0. На 0 делить нельзя!")
    except ValueError:
        print("Вы ввели не число")
    except DivisionOnZero as err:
        print(err)
    else:
        break

print(f"Результат деления {input_a} / {input_b} = {input_a / input_b:.2f}")

