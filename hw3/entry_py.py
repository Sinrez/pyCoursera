string = input()
revers = string[::-1]
a = revers.find('f')
b = len(string) - 1
lastnumber = b - a
firstnumber = string.find('f')
if firstnumber == lastnumber:
    print(firstnumber)
elif firstnumber == -1:
    print('')
else:
    print(firstnumber, lastnumber)
