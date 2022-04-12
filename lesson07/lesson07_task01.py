"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
   который должен принимать данные (список списков) для формирования матрицы.
   Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
   Примеры матриц: см. в методичке.

   Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
   Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов
   класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
   Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
   первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    __matrix: list
    __matrix_size = [0,0]

    def __init__(self, matrix):
        self.__matrix_size = [0, len(matrix[0])]
        for self.__matrix_size[0] in range(len(matrix)):
            if len(matrix[self.__matrix_size[0]]) != self.__matrix_size[1]:
                raise ValueError("Матрица неправильного размера")
        self.__matrix = matrix

    def __add__(self, other: "Matrix"):
        if not isinstance(other, Matrix):
            raise TypeError(f"'{other.__class__.__name__}' Несоответствие типов")
        if self.__matrix_size != other.__matrix_size:
            raise ValueError("Матрицы разного размера")
        result = []
        for i in range(len(self.__matrix)):
            result.append([self.__matrix[i][j] + other.__matrix[i][j] for j in range(len(self.__matrix[i]))])
        return Matrix(result)

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.__matrix]))


first_matrix = Matrix([[5, 18, 11], [6, 17, 23], [41, 50, 9]])
second_matrix = Matrix([[88, 75, 15], [55, 67, 45], [8, 28, 96]])

print("Первая матрица:")
print(first_matrix)
print("Вторая матрица:")
print(second_matrix)
print("Результат сложения матриц:")
print(first_matrix + second_matrix)
