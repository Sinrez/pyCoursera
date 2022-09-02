from math import gcd
n = 36567232109354321
e = 13771927877214701
d = 15417970063428857

kphi = d*e - 1
t = kphi

while t % 2 == 0:
        t = divmod(t, 2)[0]
a = 2
while a < 100:
    k = t
    while k < kphi:
        x = pow(a, k, n)
        if x!= 1 and x!= (n - 1) and pow(x, 2, n) == 1:
            p = gcd(x - 1, n)
            break
        k = k*2
    a=a+ 2
q = n//p
assert (p*q) == n

print('p = ', p)
print('q = ', q)