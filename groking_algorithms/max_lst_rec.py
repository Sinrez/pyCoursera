def maxx(lst):
    if len(lst) == 2:
        return lst[0] if lst[0] > lst[1] else lst[1]
    sub_max = max(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max

print(maxx([2,34,5,0]))
print([1])