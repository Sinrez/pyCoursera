s= [ 127,624,235,235,77,288]
res = total= []
res.append(str(s[0]))
for i in range(1,len(s)):
    res.append(str(int(s[i])-int(s[i-1])))
total = " ".join(res)
print(total)
