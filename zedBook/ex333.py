#запуск из ком строки
numbers = []


def numbers_list(x, y):
    i = 0
    while i < x:
        print("At the top of i is %d" % i)
        numbers.append(i)
        i += y
        print("Numbers now: ", numbers)
        print("At the bottom of i is %d" % i)
    return numbers


numbers_list(6, 1)
print("the numbers: ")

for num in numbers:
    print(num)