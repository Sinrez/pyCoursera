import webbrowser
import requests

print("Let's find an old website")
site = input("Type a website URL: ")
era = input("Type a year, mounth, and day, like 20150613: ")

url = "http://archive.org/wayback/available?url=%s&timestapm=%s" % (site, era)
response = requests.get(url)
data = response.json()
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Found this copy  ", old_site)
    print("It should appear in your brouser now")
    webbrowser.open(old_site)
except:
    print("Сорян, не найдено")