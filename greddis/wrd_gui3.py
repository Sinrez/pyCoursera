import tkinter

class MyGUI:
    def __init__(self):
        self.main_win = tkinter.Tk()
        self.label1 = tkinter.Label(self.main_win, text ='Привет мирЪ')
        self.label2 = tkinter.Label(self.main_win, text='Прога с GUI')
        self.label1.pack(side = 'left')
        self.label2.pack(side='left')
        tkinter.mainloop()

my_gui = MyGUI()