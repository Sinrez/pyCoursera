num_st = int(input('сколько у вас студентов?'))

num_test_score = int(input('сколько оценок в расчете на каждого студента?'))

for student in range(num_st):
    total = 0.0
    print('Номер студента', student + 1)
    print('-----------------')
    for test_num in range(num_test_score):
        print('Номер лабораторки', test_num + 1, end = '')
        score = float(input('введите оценку: '))
        total += score

    average = total / num_test_score

    print('Средний балл студента номер', student + 1, 'составляет: ', average)
    print()