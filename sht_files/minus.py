file = open('numbers.txt').read().split()
sum = 0
for i in file:
    if int(i) <0:
        sum+=int(i)
print(sum)