import requests as re
params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
r= re.post("http://pythonscraping.com/pages/files/processing.php", data=params)
print(r.text)