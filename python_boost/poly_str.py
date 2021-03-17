def poly(strr):
    rev = strr[::-1]
    res=''
    if strr == rev:
        res = 'палиндромом'
    else:
        res= 'нет'
    return res
print(poly('азаг'))