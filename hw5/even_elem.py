myList = input().split()

for i in map(int, myList):
    if i % 2 == 0:
        print(i, end=' ')
