import requests

r = requests.get('https://www.google.com/')
print(r.reason)
print(r.cookies)
print(r.text)
print(r.content)

# import requests
# res = requests.get('https://www.google.com/',  verify=False)
# print("Response text of https://google.com/:")
# print(res.text)
# print("Content of the said url:")
# print(res.content)