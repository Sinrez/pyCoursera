phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
#on tap

for i in range(4):
    plist.pop()

plist.remove('D')
plist.remove("'")
plist.remove(" ")

plist.insert(3, plist.pop(4))
plist.insert(2, " ")

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)