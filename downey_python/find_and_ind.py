def count(strr, chr):
    i = 0
    for s in strr:
        if chr == s:
            i += 1
    return i


if __name__ == "__main__":
    print(count('стюардесса','с'))
