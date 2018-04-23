###################
#matrix - матрица
#row - строка матрицы
#elem - елемент матрицы
#n - размерность матрицы
#maxx - значение максимального по модулю элемента матрицы
class NewMatrix:
    def __init__(self):
        matrix = []
        self.matrix = matrix

    def create_matrix(self, matrix):
        def first_check():
            try:
                n = int(input("Введите размерность матрицы: "))
                if (n < 1) or (n > 1000000000):
                    print("Число значений не может быть равно ", n)
                    return False
                return n
            except ValueError:
                print("Количество элементов не может содержать буквы и специальные символы")
                return False

        def second_check(n):
            try:
                row = [float(elem) for elem in input().split()]
                if len(row) < n:
                    print("Неверное количество элементов в строке")
                    return False
                return row
            except ValueError:
                print("Ни один из элементов строки не может быть буквой или содержать специальные символы")
                return False

        n = False
        while not n:
            n = first_check()

        print("Введите элементы в строку")
        for i in range(n):
            row = False
            while not row:
                row = second_check(n)
            self.matrix.append(row)

        return self.matrix

    def show_matrix(self, matrix):
        maxx = 0

        for row in self.matrix:
            for elem in row:
                if abs(elem) > maxx:
                    maxx = elem

        for row in self.matrix:
            print('|' + '|'.join([str(elem).rjust(len(str(maxx)) + 2) for elem in row]) + '|')

    def check(self, matrix):

        i = j = lowd = uppd = maind = alld = 0

        for i in range(len(self.matrix)):
            for j in range(i):
                if self.matrix[i][j] == 0:
                    lowd += 1
                if self.matrix[len(self.matrix) - i - 1][len(self.matrix) - j - 1] == 0:
                    uppd += 1
                alld += 1

            if self.matrix[i][i] == 0:
                maind += 1

        print("\nКоличество нулевых элементов НИЖЕ главной диагонали: ", lowd)
        print("Количество нулевых элементов ВЫШЕ главной диагонали: ", uppd)
        print("Количество нулевых элементов в ГЛАВНОЙ диагонали: ", maind, "\n")
        if (lowd == alld) and (uppd == alld) and (maind == len(self.matrix)):
            print("Нулевая матрица")
        elif (lowd == alld) and (uppd == alld):
            print("Диагональная матрица")
        elif (lowd == alld):
            print("Треугольная нижнняя матрица")
        elif (uppd == alld):
            print("Треугольная вернхяя матрица")
        else:
            print("Матрица нетреугольная")


while True:
    A = []
    my_matrix = NewMatrix()
    my_matrix.create_matrix(A)
    my_matrix.show_matrix(A)
    my_matrix.check(A)
