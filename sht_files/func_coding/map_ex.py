def mymap(func, *seq):
    newseq = []

    # Ищем размер минимальной последовательности
    min_list_len = min([len(s) for s in seq])

    # Теперь идем по элементам последовательностей
    for i in range(min_list_len):
        # Формируем аргументы функции из элементов последовательностей
        func_args = []
        for s in seq:
            func_args.append(s[i])

        # Раскрываем fun_args и вставляем в функцию
        newseq.append(func(*func_args))

    return newseq