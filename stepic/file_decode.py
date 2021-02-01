a = input()
b = []
for i in range(len(a)):
    if a[i].lower() in 'qwertyuiopasdfghjklzxcvbnm':
        b+=a[i]
        a=a[:i]+"!"+a[i+1:]
c=a.split('!')[1:]
for i in range(len(b)):
    print(b[i]*int(c[i]), end="")