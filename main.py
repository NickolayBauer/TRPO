class NewMatrix:
    def __init__(self):
        matrix = []
        self.matrix = matrix


    def create_matrix(self,matrix):
        flag = False

        while flag == False:
            flag = True
            flag2 = False
            try:
                while flag2 == False:
                    flag2 = True
                    n = int(input("Введите размерность матрицы: "))
                    self.matrix = []
                    if n < 1:
                        flag = flag2 = False
                        print("Введите корректное количество элементов матрицы (больше 0)")
                    else:
                        print("Введите элементы матрицы: ")
                        for i in range(n):
                            flag3 = False
                            while flag3 == False:
                                row = input().split()
                                row = [int(elem) for elem in row]
                                if len(row) != n:
                                    print("ошибка в количестве элементов в строке\nПовторите ввод")
                                    flag3 = False
                                else:
                                    self.matrix.append(row)
                                    flag3 = True
            except ValueError:
                print("Пожалуйста, не вводите буквы в матрицу ")
                flag = False


        return self.matrix

    def show_matrix(self,matrix):
        maxx = 0

        for row in self.matrix:
            for elem in row:
                if abs(elem) > maxx:
                    maxx = elem

        for row in self.matrix:
            print('|' + '|'.join([str(elem).rjust(len(str(maxx)) + 2) for elem in row]) + '|')


    def check(self,matrix):

        i = j = lowd = uppd = maind = alld = 0
        n = len(self.matrix)

        for i in range(n):
            for j in range(i):
                if self.matrix[i][j] == 0:
                    lowd += 1
                if self.matrix[n - i - 1][n - j - 1] == 0:
                    uppd += 1
                alld += 1

            if self.matrix[i][i] == 0:
                maind += 1

        print("\nКоличество нулевых элементов НИЖЕ главной диагонали: ", lowd)
        print("Количество нулевых элементов ВЫШЕ главной диагонали: ", uppd)
        print("Количество нулевых элементов в ГЛАВНОЙ диагонали: ", maind, "\n")
        if (lowd == alld) and (uppd == alld) and (maind == n):
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


