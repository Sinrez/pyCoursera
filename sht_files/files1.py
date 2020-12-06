file1 = open('shopping_list_1.txt').readlines()
file2 = open('shopping_list_2.txt').readlines()
file3 = open('shopping_list_3.txt').readlines()
my_list = []
for i in file1:
    if i not in my_list:
        my_list.append(i)
for i in file2:
    if i not in my_list:
        my_list.append(i)
for i in file:
    if i not in my_list:
        my_list.append(i)
my_file = open('shopping_list.txt', w)
my_file.write(my_list)