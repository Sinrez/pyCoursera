def distance(x,y):
    l1 = list(x)
    l2 = list(y)
    all = list(zip(l1,l2))
    dist = 0
    for i,j in all:
        dist += (i-j)**2
        dst1 = dist**(1/2)
    return dst1
    # print(l2)
    # return dist

# print(distance((-1, 3), (6, 2)))
# # 7.0710678118654755
# print(distance((-1, 3, 3), (6, 2, -2)))
# # 8.660254037844387