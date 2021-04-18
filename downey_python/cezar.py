def cezar(word, delta):
    res = ''
    for w in word:
        res += chr(ord(w)+delta)
    return res

if __name__ == "__main__":
    print(cezar('пайтнон', 7))
