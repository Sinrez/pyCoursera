# - Сделайте программу которая вычисляет ваш идеальный вес, в зависимости от роста и возраста.
# Найдите формулу для вычисления идеального веса в гугле, и реализуйте условие для расчёта идеального веса.

# используем формулу Брока в упрощенном вар
# https://cf.ppt-online.org/files1/slide/o/OjE74cxYQuAa1UygITRJoqKmWLtePn0lB2rN9F/slide-38.jpg

def check_q(d):
    if d.lower() == 'q':
        exit(f'Работа завершена')
    elif not d.isdigit():
        exit(f'Рост и возраст должны быть целыми положительными числами!')

def brok():
    ideal_weight = 0
    print(20 * '*')
    print('Программа считает идеальный вес по формуле Брока, для выхода нажмите q')
    print(20 * '*')

    #границы роста и веса аппроксимированы по крайним случаям примеров из человеческой истории, источник вики и др.
    height = input('Введите рост: ')
    check_q(height)
    height = int(height)
    height = height if 50 <= height <= 300 else exit('Нестандартынй рост! Вы точно человек:) ? - обратитесь в поддержку')

    age = input('Введите ваш возраст: ')
    check_q(age)
    age = int(age)
    age = int(age) if 0 < age <= 1000 else exit('Нестандартынй возраст! Вы точно человек:) ? - обратитесь в поддержку')

    coef_height = {
        164: 100,
        165: 105,
        176: 110
    }

    if 20 <= age <= 30:
        if height < 165:
            ideal_weight = (height - coef_height[164]) * 0.89
        elif 165 <= height <= 175:
            ideal_weight = (height - coef_height[165]) * 0.89
        else:
            ideal_weight = (height - coef_height[176]) * 0.89
    elif age >= 50:
        if height < 165:
            ideal_weight = (height - coef_height[164]) * 1.06
        elif 165 <= height <= 175:
            ideal_weight = (height - coef_height[165]) * 1.06
        else:
            ideal_weight = (height - coef_height[176]) * 1.06
    else:
        if height < 165:
            ideal_weight = height - coef_height[164]
        elif 165 <= height <= 175:
            ideal_weight = height - coef_height[165]
        else:
            ideal_weight = height - coef_height[176]
    print(f'Идеальный вес: {ideal_weight}')

if __name__ == '__main__':
    brok()