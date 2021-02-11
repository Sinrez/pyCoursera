import canvas


def my_click(x, y):
    print("Только что был клик!")


canvas.set_onclick(my_click)

canvas.listen()
