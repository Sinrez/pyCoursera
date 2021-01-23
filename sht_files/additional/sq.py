# strr = '1 2 3 4 5'
# strr = '1 2 3 4 4 5 4 6 7 8'
strr = '1 3 4 5 6 7 9 15'
# import sys
# strr = sys.argv[1].strip()
lst = strr.split()
n = len(lst)

def ascending():
    i = 0
    try:
        while lst[i] < lst[i+1]:
            i += 1
        return "NO"
    except IndexError:
        return "YES"
print(ascending())