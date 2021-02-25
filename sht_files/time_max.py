from datetime import time

base_time = time(9, 0, 0)

with open('visits.txt') as file:
    lines = file.read().splitlines()

dic = {}
late = {}

for line in lines:
    key, value = line.split(',')
    dic[key] = value

for key, value in dic.items():
    hours, minutes, seconds = value.split(":")
    f_time = time(int(hours), int(minutes), int(seconds))
    if f_time > base_time:
        late[key] = value

max_time = time(0, 0, 0)
for key, value in late.items():
    hours, minutes, seconds = value.split(":")
    f_time = time(int(hours), int(minutes), int(seconds))

    if max_time is None or max_time < f_time:
        max_time = f_time

for k, v in late.items():
    # time_str = f_time.strftime("%H:%M:%S")
    if v == max_time.strftime("%H:%M:%S"):
        print(k, v, sep=',')