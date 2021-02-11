def f(x):
    return x + 1

def g(function, x):
    return function(x) * function(x)

print(g(f, 5))