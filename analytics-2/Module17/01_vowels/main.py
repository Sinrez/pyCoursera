def count_letters():
    vowel_letters_rus = ('а, и, е, ё, о, у, ы, э, ю, я').strip().split(', ')
    text = input('Введите текст на русском: ').strip().lower()
    vowel_letters_res = [let for let in text if let in vowel_letters_rus]

    print(f'\nСписок гласных букв: {vowel_letters_res}')
    print(f'Длина списка: {len(vowel_letters_res)}')


if __name__ == '__main__':
    count_letters()
