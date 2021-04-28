def has_no_e():
    fin = open('words.txt', 'r')
    e_in = 0
    e_out = 0
    for line in fin:
        word = line.strip()
        if 'e' not in word:
            print(word +' True')
            e_in += 1
        else:
            print(word +' False')
            e_out +=1
    proc_e = round(e_in/(e_in + e_out) *100,1)
    print(f'Процент слов, содержащих "e" в файле: {proc_e}%')

if __name__ == "__main__":
    has_no_e()






