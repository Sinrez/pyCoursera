# 2) Напишите программу, которая
#
# - в ней изначально есть список плохих слов badwords = ['дурак', 'идиот', итд]
# - просит у пользователя ввести строку s
#  -разбивает её на список отдельных слов mywords с помощью s.split()
#  - в цикле for проходит по списку mywords и c помощью
#  x = process.extractOne(word, badwords, scorer = fuzz.WRatio)[1]
# вычисляет насколько похоже очередное слово word на слова из списка badwords
# - если процент сопадения большой, с помощью s = s.replace(word, 'цензура')
# заменяет подозрительное слово в оригинальной строке и в конце выводит её на экран

from rapidfuzz import process, fuzz

def check_word():
  badwords = ['дурак', 'идиот', 'урод', 'хмырь','fuck', 'fack', 'фак']
  strr = input('Введите строку: ').strip()
  check_list = strr.split()
  # print(check_list)
  for word in check_list:
    s = process.extractOne(word, badwords, scorer = fuzz.WRatio)
    if s[1] > 50:
      strr = strr.replace(word, 'цензура')
  print(strr)

if __name__ == '__main__':
  check_word()
