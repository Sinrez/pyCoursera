from tkinter import *

root = Tk()
root.title('Appl Test')
root.geometry('640x480')

cnt = 0
def clicked() ->int:
    global cnt
    cnt += 1
    print(f'Кол-во кликов {cnt}')


button = Button(
    text='кнопка',
    width=20,
    height=10,
    background='#550',
    #foreground='#ffa'
    font=('Verdana', '24'),
    command=clicked
)
# button.place(
#     width=200,
#     height=200,
#     x = 100,
#     y = 100
# )

lable = Label(
    text='надпись',
    font=('Verdana', '24'),
)

lable.pack()
# button.grid(
#     row = 0,
#     column = 0
# )

button2 = Button(
    text='кнопка2',
    width=20,
    height=10,
    background='#550',
    font=('Verdana', '24'),
    command=clicked
)

button.pack()
button2.pack()

# button2.grid(
#     row = 0,
#     column = 1
# )


if __name__ == '__main__':
    root.mainloop()

