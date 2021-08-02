def is_prime_number(number: int) -> bool:
    """Returns True, if `number` is prime, otherwise returns False
    Функция is_prime_number -
    проверка переданного числа на простоту
    """
    check = 0
    if number == 1 or number == 2:
        check = True
        return check

    for i in range(2, number):
        if number % i == 0:
            return (False)
            break
        else:
            check = "True"
    return check


def get_next_prime_number(number: int) -> int:
    """Returns next primer number after `number`
    get_next_prime_number - получает целое число и везвращает следующее простое число, большее, чем введённое
    (независимо простое оно или нет)
    """
    number += 1
    check = (is_prime_number(number))
    while (True):
        if (check == False):
            number += 1
            check = (is_prime_number(number))
        else:
            break
    return number