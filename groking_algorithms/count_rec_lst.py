def cnt(lst):
    if not lst:
        return 0
    else:
        return 1 + cnt(lst[1:])


print(cnt([1, 2, 3]))