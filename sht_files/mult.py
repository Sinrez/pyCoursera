import sys

number = int(sys.argv[1].strip())
for i in range(1,10):
    print('%i x %i = %i' %(number, i, number*i ))
    i=+1