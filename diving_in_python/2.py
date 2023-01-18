
inp = list(set('Beautiful is better than ugly.'.lower()))
inp_2 = sorted([i for i in inp if i.isalpha()])
print(''.join(inp_2))