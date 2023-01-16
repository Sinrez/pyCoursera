import sys

inp = int(sys.argv[1])

# inp = int(input())
# inp = 3
# inp = 5

for i in range(1, inp+1):
    print(' '* (inp-i)+'#' * i)