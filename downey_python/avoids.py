def avoids(word, chars):
    for w in word:
        if w in chars:
            return False
    return True

if __name__ == '__main__':
    print(avoids('тесты','ой'))
