def palindrome():
    word = input('Введите слово: ').strip().lower()

    if word == word[::-1]:
        print('\nСлово является палиндромом')
    else:
        print('\nСлово не является палиндромом')

if __name__ == '__main__':
    palindrome()

