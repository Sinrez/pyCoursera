start, goal, days = map(int, input().split())
d = 1
while start <= goal:
    # if start == 0:
    #     continue
    start += 1.1
    d += 1
if start >= goal and d <= days:
    print("True")
elif (start >= goal and d > days) or start < goal:
    print('False')