import sys

wrd = sys.argv[1].strip().lower()

rwd = wrd[::-1]
if( wrd == rwd):
    print("1")
else:
    print("0")

