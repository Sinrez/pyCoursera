import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.my_button = tkinter.Button(self.main_window, text ='Нажми меня!', command = self.do_something)
        self.my_button.pack()

        tkinter.mainloop()
        #Запилим метод обратного вызова callback при нажатии кнопки

    def do_something(self):
        tkinter.messagebox.showinfo('Реакция','Спасибо за пинок по кнопке')

my_gui = MyGUI()