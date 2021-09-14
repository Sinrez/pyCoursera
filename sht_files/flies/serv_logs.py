import datetime
from sys import argv


with open("server.log") as log:
    new_l = []
    new_d = []
    for i in log.readlines():
        d_start = i.find("[") + 1
        d_stop = i.find("]")
        date = datetime.datetime.strptime(i[d_start:d_stop], "%d/%b/%Y:%H:%M:%S")
        x = i.find("GET ") + 4
        z = i.find(" ", x)
        new_d.append({date.strftime("%d.%m.%Y"): i[x:z]})



    for i in range(len(new_d)):
        if argv[1] in new_d[i].keys():
            new_l.append(new_d[i].get(argv[1]))
        else:
            continue



    x = 0
    z = ""
    new_set_l = set(new_l)
    for i in new_set_l:
        if new_l.count(i) > x:
            x = new_l.count(i)
            z = i
print(z, x)