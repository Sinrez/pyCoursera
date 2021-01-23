# Открываем файл и объявляем переменную для хранения матирцы
matrix_file = open("matrix.txt", "r")
matrix = []

# Заполняем матрицу данными.
for line in matrix_file.readlines():
    matrix.append(line.strip().split(" "))

# Создаем пустую развернутую матрицу.
transpose_matrix = []
for k in range(matrix[0].__len__()):
    transpose_matrix.append([None] * matrix.__len__())

# Транспонируем (заполняем значениями)
i = 0
for line in matrix:
    j = 0
    for col in line:
        transpose_matrix[j][i] = matrix[i][j]
        j += 1
    i += 1