import struct

with open('order.data','rb') as order_file:
    orders = order_file.read()
    num, date, prod,count, sums = struct.unpack('i10s70sif',orders)

    price = str(count * sums)+'0'

    sdate = date.decode('UTF-8').replace('-','.')
    ndate = sdate[8:]+sdate[4:8]+sdate[:4]
    print(f'Заказ {num} от {ndate} на сумму {price}')