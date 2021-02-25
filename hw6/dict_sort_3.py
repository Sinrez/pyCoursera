import operator

dict1 = {1: 1, 2: 9}
get_item_with_key_2 = operator.itemgetter(2)

print(get_item_with_key_2(dict1))  # 9