import sys


word = sys.argv[1]
word2 = sorted(word)
word_f = []
for letter in word2:
    if letter not in word_f:
        word_f.append(letter)



print(''.join(word_f))

