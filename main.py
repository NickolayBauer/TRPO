import random


def create_matrix():
    flag = False

    while flag == False:
        flag = True
        flag2 = False
        try:
            while flag2 == False:
                flag2 = True
                n = int(input("Введите размерность матрицы: "))
                matrix = []
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
                                matrix.append(row)
                                flag3 = True
        except ValueError:
            print("Пожалуйста, не вводите буквы в матрицу ")
            flag = False


    return matrix


def create_random_matrix(firstParam, secondParam):
    n = random.randint(firstParam, secondParam)
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randint(0, 1))
        matrix.append(row)
    return matrix


def show_matrix(matrix):
    maxx = 0
    for row in matrix:
        for elem in row:
            if abs(elem) > maxx:
                maxx = elem

    for row in matrix:
        print('|' + '|'.join([str(elem).rjust(len(str(maxx)) + 2) for elem in row]) + '|')


def check(matrix):
    i = j = lowd = uppd = maind = alld = 0
    n = len(matrix)

    for i in range(n):
        for j in range(i):
            if matrix[i][j] == 0:
                lowd += 1
            if matrix[n - i - 1][n - j - 1] == 0:
                uppd += 1
            alld += 1

        if matrix[i][i] == 0:
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
    matrix = create_matrix()
    show_matrix(matrix)
    check(matrix)
