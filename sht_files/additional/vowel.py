import sys
word = sys.argv[1].strip()
vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Y', 'y']
res = []
for let in word:
    if let in vowels:
        res.append(let)
print(''.join(res))