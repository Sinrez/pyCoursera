import requests
result = requests.get('https://letpy.com/simple-html-example/')
strr = result.text
i = strr.find(': <strong>')
strr = strr[i:]
res_l = []
for s in strr:
    if s.isdigit():
        res_l.append(s)
res = ''.join(res_l)

print(res)