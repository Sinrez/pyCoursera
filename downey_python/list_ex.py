def nested_sum(t):
    s = 0
    for l1 in t:
        # print(l1)
        s += sum(l1)
    print(s)

def cumsum(z):
    total = 0
    res = []
    for x in z:
        total += x
        res.append(total)
    return res

def middle(lst):
    return lst[1:len(lst)-1]

def chop(lst):
    t = middle(lst)
    return t

def is_sorted(lst):
    return lst == sorted(lst)

def is_anagram(lst1, lst2):
    return sorted(lst1) == sorted(lst2)

def has_diplicates(s):

   lst = list(s)
   lst.sort()

   for i in range(1,len(lst)):
       if lst[i] == lst[i+1]:
           return True
       return False


if __name__ == '__main__':
    # t = [[1, 2], [3], [4, 5, 6]]
    # nested_sum(t)
    z = [1, 2, 3, 4, 5]
    l = 'роза'
    l2 = 'азор'
    lst1 = 'hggg5t'
    # print(chop(z))
    # print(is_anagram(l,l2))
    print(has_diplicates(lst1))


