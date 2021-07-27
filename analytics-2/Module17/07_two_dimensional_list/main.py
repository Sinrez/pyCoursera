def list_gen():
    cols = 3;
    rows = 4
    res = [list(range(x, x + rows * (cols - 1) + 1, rows)) for x in range(1, rows + 1)]
    print(res)


if __name__ == '__main__':
    list_gen()
