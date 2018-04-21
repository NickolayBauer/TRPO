import random


def create_matrix():
    flag = flag_too = False
    while flag == False:
        try:
            while flag_too == False:
                n = int(input("Введите размерность матрицы: "))
                if n > 1:
                    flag_too = True
                else:
                   print( "Попробуйте скорректировать ввод")
            print("Введите элементы матрицы: ")


            matrix =[[int(j) for j in input().split()] for i in range(n)]



            flag = True
        except ValueError:
            print("Что-то не так с вводом матрицы, попробуйте ещё раз")
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
    lowd = uppd = maind = alld = 0
    n = len(matrix)

    for i in range(n):
        for j in range(i):
            if matrix[i][j] == 0:
                lowd += 1
            if matrix[n - i - 1][n - j - 1] == 0:
                uppd += 1
            alld += 1
    for i in range(n):
        if matrix[i][i] == 0:
            maind += 1


    print("\nКоличество нулевых элементов НИЖЕ главной диагонали: ", lowd)
    print("Количество нулевых элементов ВЫШЕ главной диагонали: ", uppd)
    print("Количество нулевых элементов в ГЛАВНОЙ диагонали: ", maind,"\n")
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


matrix = create_matrix()
show_matrix(matrix)
check(matrix)
