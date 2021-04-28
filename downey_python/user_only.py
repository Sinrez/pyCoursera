def user_only(word, chars):
    for w in word:
        if w in chars:
            return True
    return False

if __name__ == '__main__':
    print(user_only('тесты','ой'))