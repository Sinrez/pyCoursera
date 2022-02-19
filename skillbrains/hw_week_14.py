import random


def list_gen(n=10) -> list:
    return [random.randint(1, 100) for _ in range(n)]


def insert_sort(lst) -> list:
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and temp < lst[j]:
            lst[j + 1] = lst[j]
            j = j - 1
        lst[j + 1] = temp
    return lst


def lists_prepare(lst_in):
    print(f'Список до сортировки: {lst_in}')
    print(f'Список после сортировки: {insert_sort(lst_in)}')
    print('*' * 70)

def list_print():
    for i in range(10):
        print(f'Список {i+1}')
        lists_prepare(list_gen())

if __name__ == '__main__':
    list_print()

