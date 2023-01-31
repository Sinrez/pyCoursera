def binary_searh(lst, inp):
    left = 0
    right = len(lst)-1

    while left <= right:
        med = (right + left) // 2
        midian = lst[med]
        if inp == midian:
            return med
        elif inp < midian:
            right = med - 1
        else:
            left = med + 1
    return None


if __name__ == '__main__':
    lst = [1,3,5,7,9]
    print(binary_searh(lst, 3))
    print(binary_searh(lst, -1))