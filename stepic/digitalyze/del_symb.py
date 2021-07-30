# print("".join((list(input().strip()))))
# print("".join(set(input())))
new_list = []
old_list = list(input().strip())
[new_list.append(item) for item in old_list if item not in new_list]
print(''.join(new_list))
