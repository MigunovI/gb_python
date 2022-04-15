"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
   реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
   создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
   Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b} * i'

    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError(f"'{other.__class__.__name__}' Несоответствие типов")
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError(f"'{other.__class__.__name__}' Несоответствие типов")
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


z1 = ComplexNumber(2, 1)
z2 = ComplexNumber(3, 4)
print(f'z1 = {z1}')
print(f'z2 = {z2}')
print(f'z1 + z2 = {z1 + z2}')
print(f'z1 * z2 = {z1 * z2}')
