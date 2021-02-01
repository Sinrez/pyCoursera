import tkinter

class MyGUI:
    def __init__(self):
        self.main_win = tkinter.Tk()
        self.label = tkinter.Label(self.main_win, text ='Привет мирЪ')
        self.label.pack()
        tkinter.mainloop()

my_gui = MyGUI()