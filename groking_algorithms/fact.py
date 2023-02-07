def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

def fact_non_rec(n):
    res = 1
    if n == 1:
        return res
    else:
        for i in range(2,n+1):
            res *= i
    return res

print(fact(5))
print(fact_non_rec(5))