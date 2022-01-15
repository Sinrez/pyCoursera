# 1. В единственной строке записан текст.
# Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.

def count_word():
    count = {}
    txt = input('Введите текст: ').strip().split()
    for t in txt:
        count[t] = count.get(t, 0) + 1

    for word, count in count.items():
        print(f'Слово "{word}", кол-во: {count}')

# 2. Дан текст: в первой строке задано число строк, далее идут сами строки.
# Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то,
# которое меньше в лексикографическом порядке. Словом считается последовательность
# непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.

def check_dgt(d):
    if not d.isdigit():
       exit('Вы ввели не число, повторите ввод')

def frequency_word():
    counter = {}
    cnt = input('Введите кол-во строк: ').strip()
    check_dgt(cnt)
    cnt = int(cnt)
    for i in range(cnt):
        line = input().split(f'Введите {i}-ю строку: ')
        for word in line:
            counter[word] = counter.get(word, 0) + 1

    max_count = max(counter.values())
    most_frequent = [k for k, v in counter.items() if v == max_count]
    print(min(most_frequent))

# доп про дерево

def tree():
    n = input('Введите высоту дерева: ').strip()
    check_dgt(n)
    n = int(n)
    d = {}
    a = {}

    for i in range(n - 1):
        child, parrent = input('Введите ребенка, родителя: ').split()
        d[child] = parrent
        a[child] = 0
        a[parrent] = 0

    for i in d:
        s = i
        while s in d:
            s = d[s]
            a[i] += 1

    for i in sorted(a):
        print(i, a[i])

if __name__ == '__main__':
    # count_word()
    # frequency_word()
    tree()