def is_palindrome(lst):
    str1 = ''.join(map(str, lst))
    if str1 == str1[::-1]:
        return True
    else:
        return False


def list_creator(lst):
    count = check_dgt('Кол-во чисел или q для выхода: ')
    for _ in range(count):
        lst.append(check_dgt('Число: '))


def main_palindrome():
    nums = []
    new_nums = []
    answer = []
    list_creator(nums)
    for i_nums in range(0, len(nums)):
        for j_elem in range(i_nums, len(nums)):
            new_nums.append(nums[j_elem])
        if is_palindrome(new_nums):
            for i_answer in range(0, i_nums):
                answer.append(nums[i_answer])
            answer.reverse()
            break
        new_nums = []

    print(f"\nПоследовательность: {' '.join(map(str, nums))}")
    print(f"Нужно приписать чисел: {len(answer)}")
    print(f"Сами числа: {' '.join(map(str, answer))}")


def check_dgt(in_msg):
    while True:
        count_debtor = input(in_msg).strip()
        if count_debtor.lower() == 'q':
            exit('Работа завершена.')
        elif count_debtor.isdigit() == False:
            print('Нужно ввести число!')
        else:
            return int(count_debtor)


if __name__ == '__main__':
    main_palindrome()
