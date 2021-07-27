


def lists_gen():
    list1 = []
    list2 = []
    for i in range(160, 177, 2):
        list1.append(i)
    for j in range(162, 181, 3):
        list2.append(j)
    list1.extend(list2)
    list1.sort()
    return list1

if __name__ == '__main__':
  print(lists_gen())
