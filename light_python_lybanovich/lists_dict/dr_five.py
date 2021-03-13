years = []
dr = 1984
for year in range(1984,1989):
    # print(year)
    years.append(year)

print(years)
print(max(years))
num_birth_day = int(input())
print(years[num_birth_day-1])