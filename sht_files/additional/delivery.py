def delivery(price, region=False, big=False, time=False, today=False):
    if today:
        # Стоимость доставки при доставке с доп. критерием "день в день":
        return 990

    if price < 5000:
        # Стоимость доставки заказа при общей сумме заказа меньше 5 000 р.:
        delivery_cost = 290
    else:
        delivery_cost = 0

    if big:
        # Стоимость доставки габаритного груза:
        delivery_cost = 490

    if region:
        # Стоимость заказа при расположении пункта назначения груза в Московской обл., но за пределами г. Москвы:
        delivery_cost = 290

    if time:
        # Размер наценки за доставку в определённое время:
        delivery_cost += 190

    return delivery_cost
