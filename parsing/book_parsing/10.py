import requests
params = {'email_addr': '123@gmail.com'}
r= requests.post('http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi',data=params)
print(r.text)