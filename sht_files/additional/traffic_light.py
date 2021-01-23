import sys
N = int(sys.argv[1])
M = int(sys.argv[2])
T = int(sys.argv[3])
T1 = T % (N+M)
if T1 < N:
	print('green')
else:
	print('red')