import sys

strr = sys.argv[1].strip()
#islower() str.isupper()
lw = []
up = []
for st in strr:
    if(st.islower()):
        lw.append(st)
    elif(st.isupper()):
        up.append(st)
res = lw + up
print(''.join(res))
