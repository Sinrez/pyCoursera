from tkinter import *

root = Tk()
root.title('Appl Test')
root.geometry('640x480')

entry = Entry(
    width=20,
    font = ('Verdana','12'),
    justify=CENTER,
    show='*'
)

def cliked() ->str:
    s = entry.get()
    print(s)

def delete() ->None:
    entry.delete(0,END)


buttton = Button(
    text='cliked',
    command=cliked
)

buttton2 = Button(
    text='delete',
    command=delete
)

entry.pack()
buttton.pack()
buttton2.pack()

if __name__ == '__main__':
    root.mainloop()

