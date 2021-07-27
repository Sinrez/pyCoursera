def lots():
    memb = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
    for i in range(1, len(memb)):
        if i % 2 == 0:
            print(memb[i])


if __name__ == '__main__':
    lots()
