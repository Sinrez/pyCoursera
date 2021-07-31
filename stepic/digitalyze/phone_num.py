
def format_numbers(phone_number: str) -> str:
    return '8 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}'.format(*[i for i in phone_number if i.isdigit()][1:])
#
# print(format_numbers(numbers))

numbers = input().strip().replace('(','').replace(')','').replace(' ','').replace('-','')
if numbers[0] == '9':
    numbers = '8 (9' + numbers[1:]
    print(format_numbers(numbers))
elif numbers[:2] == '79':
    numbers = '8 (9' + numbers[2:]
    print(format_numbers(numbers))
elif numbers[:3] == '+79':
    numbers = '8 (9' + numbers[3:]
    print(format_numbers(numbers))
elif '8' in numbers[:3] or '7' in numbers[:3] or '9' in numbers[:3]:
    print(format_numbers(numbers))
else:
    print(numbers)