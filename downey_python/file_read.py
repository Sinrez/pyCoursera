def file_read():
    fin = open('words.txt', 'r')
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

if __name__ == "__main__":
    file_read()
