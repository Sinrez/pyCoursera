n = int(input())
counter = 1
last = 0
while counter <= n:
    last += 1 / (counter ** 2)
    counter += 1
print(last)
