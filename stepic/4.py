numbers = [22, 9, 37, 44, 46, 69, 24, 100, 97, 57, 1, 6, 27, 96, 16, 82, 10, 95, 99, 78, 62, 50, 77, 86, 56, 40, 49, 32, 53, 76, 63, 67, 52, 0, 93, 84, 28, 8, 41, 79, 25, 21, 71, 43, 81, 72, 20, 90, 39, 75, 85, 14, 15, 60, 64, 5, 66, 4, 36, 98, 80, 12, 47, 91, 73, 45, 31, 65, 87, 74, 11, 34, 33, 18, 58, 23, 68, 94, 92, 17, 26, 88, 35, 13, 7, 42, 38, 19, 48, 29, 3, 59, 55, 51, 89, 2, 70, 83, 61, 54, 30]

i = 1
count = 0
while i < len(numbers):
    if numbers[i-1]<numbers[i]>numbers[i + 1]:
        count += 1
    i += 1
print(count)