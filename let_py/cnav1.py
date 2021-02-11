import canvas

def my_click(x, y):
    canvas.circle(x, y, 15)
    canvas.draw()

canvas.set_onclick(my_click)
canvas.listen()