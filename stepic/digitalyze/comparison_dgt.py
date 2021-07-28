inp_d = input().strip().split(' ')
for d in inp_d:
    if d.isalpha():
        exit('Нужны числа')
dgt1, dgt2 = map(int, inp_d)
# если оба больше 100,
# то выводит на печать максимальное из них, в противном случае выводит на печать сумму второго числа и числа 112.
if dgt1 > 100 and dgt2 > 100:
    print(max(dgt1, dgt2))
else:
    print(dgt2 + 112)
