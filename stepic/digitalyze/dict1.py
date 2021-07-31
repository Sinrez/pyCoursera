import json
my_dict = json.loads(input())
# {"key1": 123, "key2": 11, "key3": 110000, "key4": 50}

maxx = max(my_dict.values())
for k, v in my_dict.items():
    if v == maxx:
        print(k)