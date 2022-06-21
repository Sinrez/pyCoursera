import urllib.request as ur

url = 'http://www.example.com/'
conn = ur.urlopen(url)
print(conn.status)

data = conn.read()
print(data[:50])


str_data = data.decode('utf8')
print(str_data[:50])

print()

for key, value in conn.getheaders():
    print(key, value)