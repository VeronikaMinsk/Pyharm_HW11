# 3.Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def fill(self, values):
        for i in range(self.rows):
            for j in range(self.columns):
                self.data[i][j] = values[i][j]

    def print(self):
        for row in self.data:
            print(row)

    def __eq__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            return False
        for i in range(self.rows):
            for j in range(self.columns):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Матрицы разных размеров нельзя сложить.")
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        if self.columns != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы.")
        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                sum = 0
                for k in range(self.columns):
                    sum += self.data[i][k] * other.data[k][j]
                result.data[i][j] = sum
        return result


matrix1 = Matrix(3, 3)
matrix1.fill([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

matrix2 = Matrix(3, 3)
matrix2.fill([[7, 8, 9], [10, 11, 12], [10, 3, 7]])

matrix3 = Matrix(3, 3)
matrix3.fill([[1, 2, 5], [3, 7, 4], [5, 9, 6]])

print("Матрица 1:")
matrix1.print()

print("Матрица 2:")
matrix2.print()

print("Матрица 3:")
matrix3.print()

print("Сравнение матриц 1 и 2:", matrix1 == matrix2)
print("Сравнение матриц 1 и 1:", matrix1 == matrix1)

print("Сумма матриц 1 и 2:")
(matrix1 + matrix2).print()

print("Умножение матриц 1 и 3:")
(matrix1 * matrix3).print()
