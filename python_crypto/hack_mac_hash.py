from time import time

def verify_mac(x, y, n):
    for i in range(n):
        if x[i] != y[i]:
            return False
    return True

MAC1 = '0123456789abcdef'
MAC2 = '01X3456789abcdef'
TRIALS = 100000

# при каждом обращении к verify_mac() просматриваются все восемь байт
start = time()
for i in range(TRIALS):
    verify_mac(MAC1, MAC1, len(MAC1))
end = time()
print('%0.5f' % (end-start))

# при каждом обращении к verify_mac() просматриваются только три байта
start = time()
for i in range(TRIALS):
    verify_mac(MAC1, MAC2, len(MAC1))
end = time()
print('%0.5f' % (end-start))