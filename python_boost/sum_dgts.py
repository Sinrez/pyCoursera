def sum_dgt(diget):
    res = []
    summ = 0
    for i in str(diget):
        res.append(int(i))
    for j in res:
        summ += j
    return summ

# alt
# def sum_digits(num):
#     digits = [int(d) for d in str(num)]
#     return sum(digits)
# print(sum_digits(5245))

print(sum_dgt(454646))

