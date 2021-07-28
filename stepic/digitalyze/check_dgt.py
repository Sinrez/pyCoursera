inp_d = input().strip().replace(',', '.')
if inp_d.isalpha():
    exit('Нужно число')
elif float(inp_d) > 0:
    print('Это положительное число')
elif float(inp_d) == 0:
    print('Это ноль')
else:
    print('Это отрицательное число')