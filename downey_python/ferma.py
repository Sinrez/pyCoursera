def check_fermat():
    a = int(input('Введите число а: '))
    b = int(input('Введите число b: '))
    c = int(input('Введите число с: '))
    n = int(input('Введите показатель степени n: '))
    if n > 2 and a**n + b**n == c**n:
        return 'Не может быть -Ферма ошибся'
    else:
        return 'Нет, это не работает'

if __name__ == "__main__":
    print(check_fermat())

