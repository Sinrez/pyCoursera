import sys

input_string = sys.stdin.readlines()

string = ""
for i in range(0, len(input_string)):
    string = string + input_string[i]

string = string.lower().replace("\n", " ")
list_with_no_symbols = []
for i in string:
    if i.isalpha() == True or i == " ":
        list_with_no_symbols.append(i)

list_with_no_symbols = "".join(list_with_no_symbols).split(" ")

list_len_more_than_3 = []

for i in list_with_no_symbols:
    if len(i) >= 3:
        list_len_more_than_3.append(i)

vac_words_counter = {}

for i in list_len_more_than_3:
    vac_words_counter[i] = list_len_more_than_3.count(i)

list_vac = []
list_vac = list(vac_words_counter.items())

sorted_list_vac = sorted(list_vac, key=lambda i: i[0])
sorted_list_vac = sorted(sorted_list_vac, key=lambda i: i[1], reverse=True)

print("10 самых часто встречающихся слов в этом тексте:\n", )
for i in range(0, 10):
    print(sorted_list_vac[i][0], ": ", sorted_list_vac[i][1], sep="")
