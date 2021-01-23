#strr = 'Мы с Андреем пошли на рыбалку , а затем вернулись домой ! '
#strr = ' Было здорово  на игре !' #4
#strr = 'Я ел   булочки  и  пил кофе' #6
#strr = 'Я     пошел  в ТЦ    Европа    в магазин Варежки .' #8
#strr = 'Мы с Андреем  пошли на рыбалку , а затем вернулись домой !' #10

import sys
strr = sys.argv[1]
strr = strr.replace(" ,", ",").replace(" .", ".").replace(" :", ":").replace(" :", ":").replace(" ;", ";")\
    .replace(" -","-").replace(" !","!").replace(" ?","?").replace("  "," ").strip()
strr = strr.split()
#print(type(strr))
strr2 = ' '.join(strr)
#print(strr2)
count = 1
for s in strr2:
    if s == " ":
        count += 1

print(count)