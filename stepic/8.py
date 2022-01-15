# number = 1234567890
# count = 0
# while number > 0:
#     last_digit = number % 10
#     if last_digit < 3:
#         count = count + 1
#     number = number // 10
# print(count)

# number = 73408
# m = 0
# s = 0
# while number > 0:
#     last_digit = number % 10
#     s = s + last_digit
#     if last_digit > m:
#         m = last_digit
#     number = number // 10
# print(s + m)

for i in 1, 2, 3, 'one', 'two', 'three':
    print(i)