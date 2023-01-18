s1, s2 = input().lower(), input().lower()
str1 = [s for s in s1]
str2 = [s for s in s2 if s.isalpha()]

# in1 = 'Abracadabra'
# in2 = 'Fabric'

# in1 = 'abc'
# in2 = 'abA'

# str1 = list(in1.lower())
# str2 = list(in2.lower())

result2 = {s: '' for s in str2}

result = []
for letter_2 in str2:
    if letter_2 in str1 and letter_2.isalpha():
        result = [i + 1 for i, letter_1 in enumerate(str1) if letter_2 == letter_1]
        result2[letter_2] = result

for k in result2.keys():
    if result2[k] == '':
        result2[k] = None

for k, v in result2.items():
    if v is not None:
        print(f'{k} {" ".join(map(str, v))}')
    else:
        print(f'{k} {v}')
