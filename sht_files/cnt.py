import sys
list_1 = list(sys.argv[1].strip().split())
list_2 = [",", ".", "!", "?", ":", ";"]
for w_el in list_1:
    for p_el in list_2:
        if w_el == p_el:
            list_1.remove(w_el)
word_count = len(list_1)
print(word_count)