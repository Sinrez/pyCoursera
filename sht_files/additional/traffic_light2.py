import sys
n = int(sys.argv[1])  #зеленый сигнал светофора
m = int(sys.argv[2])  #желтый сигнал светофора
l = int(sys.argv[3])  #красный сигнал светофора
t = int(sys.argv[4])
cicle = n + l + m
light = t - cicle*(int(t/cicle))
if light < n:
  print('green')
elif light >= n and light < (n+m):
  print('yellow')
elif light >= n+m or light < (n+m+l):
  print('red')
else:
  print('green')