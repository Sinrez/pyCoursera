lst = ["Mike", "", "Emma", "Kellly", "", "Brad"]
# lst.remove("")
# lst.remove("")
res = []
for l in lst:
    if l != "":
        res.append(l)
print(res)