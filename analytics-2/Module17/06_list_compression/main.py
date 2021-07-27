from random import randint as ri

def compr_zero():
    l = [ri(-4, 4) for i in range(ri(10, 30))]
    print(l)
    l = [i for i in l if i]
    print(l)

if __name__ == '__main__':
    compr_zero()
