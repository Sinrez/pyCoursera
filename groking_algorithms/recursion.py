def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        return countdown(i-1)

countdown(5)