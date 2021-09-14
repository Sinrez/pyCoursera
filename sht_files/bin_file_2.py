import struct


with open("bill.data", "rb") as file_open:
    file = file_open.read()
    # считываю вводные данные из файла "bill.data", тут мне нужно найти к-во товара чтобы понять какой длины делать цикл
    number, date, qv = struct.unpack("h10sh", file[:14])
    file_2 = file[14:]
    x = 0
    # цикл на основе кол-ва, код p = file_2[i * 108: i * 108 + 108] - был подсмотрен в уроке "МОДУЛЬ STRUCT, ЧАСТЬ 2"
    for i in range(qv):
        p = file_2[i * 108: i * 108 + 108]
        name, qv_2, price = struct.unpack("100shf", p)
        x += qv_2 * price
    # вывожу на экран конечную стоимость всех товаров и работ в счете
    print(f"{x:.2f}")