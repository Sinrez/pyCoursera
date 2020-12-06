import sys

i = sys.argv[1].strip()

quarters = {
    "quarter_1": [137, 565, 145],
    "quarter_2": [145, 738, 1145],
    "quarter_3": [1345, 1141, 879],
    "quarter_4": [784, 689, 543]
}
quarter = "quarter_" + str(i)
summ = quarters[quarter][0] + quarters[quarter][1] + quarters[quarter][2]

print(summ)