phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
#on tap

nlist = []
nlist.extend(plist[1:3])
nlist.extend(plist[5])
nlist.extend(plist[4])
nlist.extend(plist[-7:-4][::-1])

new_phrase = ''.join(nlist)
print(plist)
print(new_phrase)