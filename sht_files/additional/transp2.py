file=open('matrix.txt')
matrix1=[list(line.strip().split(' ')) for line in file]
empty_matrix=[[0]*len(matrix1) for i in range(len(matrix1[0]))]
i=0
j=0
while i!=len(matrix1):
     j=0
     while j!=len(matrix1[i]):
         empty_matrix[j][i]=matrix1[i][j]
         j+=1
     i+=1
new_file=open('transpose_matrix.txt','w')
for index in empty_matrix:
    new_file.write(' '.join(index)+'\n')
new_file.close()
file.close()