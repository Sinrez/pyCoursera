import requests
result = requests.get('https://letpy.com/simple-html-example/')
text = result.text.replace('</strong>', '<strong>')
parts = text.split('<strong>')
print(parts[-2])