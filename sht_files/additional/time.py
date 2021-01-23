import sys
t = int(sys.argv[1].strip())
#t = 17
# sec = 79
# sec = 4589
ss = mm = hh = 0

hh = t // 3600
mm = t % 3600 // 60
ss = t - mm * 60 - hh * 3600
if hh == 0 and mm == 0:
    print('{:02}'.format(ss))
elif hh == 0 and mm != 0:
    print('{:02}:{:02}'.format(mm, ss))
else:
    print('{:02}:{:02}:{:02}'.format(hh, mm, ss))


