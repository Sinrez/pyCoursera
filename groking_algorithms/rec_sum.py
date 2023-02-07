def rec_sum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + rec_sum(lst[1:])

print(rec_sum([1,2,3]))