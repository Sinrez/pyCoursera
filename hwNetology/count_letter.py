def count_letter(lst, letter):
    count = 0
    for word in lst:
        if letter in word:
            count += 1
    return count

#test
# lst1 = ['python', 'c++', 'c', 'scala', 'java']
# ltr1 = 'c'
# print(count_letter(lst1, ltr1))
# ++++result_test+++
# /usr/local/bin/python3.8 /Volumes/D/pyCoursera/hwNetology/count_letter.py
# 3