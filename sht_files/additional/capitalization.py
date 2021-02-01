def capitalization (summ, proc, period):
    if period == 1:
        summ = summ + summ * proc / (12 * 100)
    else:
        for i in range(period):
            summ = summ + summ * proc / (12 * 100)
            i += 1
    return int(summ)

# print(capitalization(10000, 10, 12))