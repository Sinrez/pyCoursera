import struct
num_tv=8
tovs=["свинина","майонез","морковь","свекла", "сыр", "чеснок", "масло", "картофель"]
tovs.sort()
with open("products.data",'wb') as fl:
    count=struct.pack("H",num_tv)
    fl.write(count)
    for tov in tovs:
        tovr=struct.pack("60s",tov.encode())
        fl.write(tovr)