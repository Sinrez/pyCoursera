def speed_to_pace(speed):
    """
    Функция переводит скорость (speed) в км/ч в темп (км/мин).
    """
    temp = 60 / speed
    minutes = int(temp)
    seconds = (temp - minutes) * 60
    return "{}:{:02.0f}".format(minutes, seconds)