def rvrs_h(s):
    a = s[:s.find('h')]
    b = s[s.find('h'):s.rfind('h') + 1]
    c = s[s.rfind('h') + 1:]
    s = a + b[::-1] + c
    print(s)


if __name__ == '__main__':
    strr = input('Введите строку: ').strip().lower()
    rvrs_h(strr)
