number = int(input())
count = 0
for i in range(1, number+1):
    if number % i == 0:
        count += 1
print(True if count <= 2 else False)