import requests
params = {'username': 'Ryan', 'password': 'password'}
r= requests.post('http://pythonscraping.com/pages/cookies/welcome.php', params)
print('Cookie is set to:')
print(r.cookies.get_dict())
print('Going to profile page...')