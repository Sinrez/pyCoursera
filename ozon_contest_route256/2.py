if __name__ == '__main__':
    nums = int(input())
    for _ in range(1, nums + 1):
        items = int(input())
        prices = input().split()
        dt = {}
        for i in prices:
            if dt.get(i):
                dt[i] += 1
            else:
                dt[i] = 1

        sum_with_discount = 0
        for key, val in dt.items():
            s = val - val // 3
            sum_with_discount += int(key) * s

        print(sum_with_discount)