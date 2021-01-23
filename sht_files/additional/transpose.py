arr = open("matrix.txt").read().strip().split("\n")

old_arr = []
new_arr = []
i=j=0
n = len(arr)

for item in arr:
    old_arr.append(item.split(" "))

new_arr = [[0]*n for i in range(n-1)]

for i in range(n-1):
    for j in range(n):
        new_arr[i][j] = old_arr[j][i]


new_file=open('transpose_matrix.txt','w')
for index in new_arr:
    new_file.write(' '.join(int(index))+'\n')
new_file.close()

