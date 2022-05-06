# 3) Напишите программу, которая считает в тексте количество символов без пробелов, и отдельно с пробелами

def count_symb():
    inp_text = input('Введите текст: ').strip()
    count_whitespace = len(inp_text.replace(' ', ''))
    count_all = len(inp_text)
    print(f'Кол-во символов без пробелов: {count_whitespace} с пробелами {count_all}')

# 4) Напишите программу, которая считает во введённой строке количество отдельных предложений (подумайте, как это можно сделать)

def count_sentence():
    inp_text = input('Введите текст: ')
    count_symb = inp_text.count('. ')
    count_symb += inp_text.count('! ')
    count_symb += inp_text.count('? ')
    count_symb += inp_text.count('?! ')
    count_symb += inp_text.count('!? ')
    count_symb += inp_text.count('!!! ')
    count_symb += inp_text.count('!! ')
    print(count_symb+1)

if __name__ == '__main__':
  # count_symb()
  count_sentence()
