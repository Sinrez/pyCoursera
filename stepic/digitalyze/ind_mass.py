ind = input().replace(',','.').split(" ")
# формате масса, затем пробел, затем высота
a = float(ind[0])
b = float(ind[1]) ** 2
print(format((a / b), '.1f'))