import random

def gen_lst():
    res = []
    lst1 = [round(random.uniform(5, 10), 2) for i in range(1,21)]
    lst2 = [round(random.uniform(5, 10), 2) for i in range(1,21)]
    for i in range(0, 20):
        if lst1[i] > lst2[i]:
            res.append(lst1[i])
        else:
            res.append(lst2[i])

    print(f'Первая команда: {lst1}')
    print(f'Вторая команда: {lst2}')
    print(f'Победители тура: {res}')


if __name__ == '__main__':
    gen_lst()
