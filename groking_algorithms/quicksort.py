def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        less = [l for l in lst if l < pivot]
        greater = [l for l in lst if l > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10,5,2,3]))