import canvas

def my_click(x, y):
    colors = ["Pink", 'Lime', 'Red', "Blue", 'Crimson', 'Gold', 'RosyBrown']
    a = enumerate(colors)
    for i in a:
        canvas.set_color(str(i[1]))
        b = range(15)
        canvas.circle(x, y, b[i[0]])
        # canvas.fill_circle(x, y, 15)
    canvas.draw()

canvas.set_onclick(my_click)

canvas.listen()