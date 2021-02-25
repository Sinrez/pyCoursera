numberOfParticipants = int(input())

participants = {}
points = 0

for i in range(numberOfParticipants):
    properties = list(input().split())
    secondName = properties[0]
    points = int(properties[1])
    participants[secondName] = points

sorted_dict = {}
sorted_participants = sorted(participants.values())  # Sort the values
for i in sorted_participants:
    for k in participants.keys():
        if participants[k] == i:
            sorted_dict[k] = participants[k]
            break
res = list(sorted_dict.keys())
print(', '.join(res))

# for p in participants:
#     print(p.secondName)
