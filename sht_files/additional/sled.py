arr = open("matrix.txt").read().strip().split("\n")
#arr.remove('')
new_arr = []
sum = 0


for item in arr:
    new_arr.append(item.split(" "))

for i in range(len(new_arr)):
    sum += int(new_arr[i][i])

print(new_arr)
print(sum)
