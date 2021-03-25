import tkinter
import tkinter.messagebox

#ковертирует км в мили
class KiloComvertGUI:
    def __init__(self):

        self.main_wind = tkinter.Tk()

        #рамки для интерфейса
        self.top_frame = tkinter.Frame(self.main_wind)
        self.button_frme = tkinter.Frame(self.main_wind)

        #элементы для верхней рамки
        self.prompt_label = tkinter.Label(self.top_frame, text ='Введите расстояние в км:')
        self.kilo_entry = tkinter.Entry(self.top_frame, width = 50)

        #Упаковать элементы верхней рамки
        self.prompt_label.pack(side ='left')
        self.kilo_entry.pack(side = 'left')

        #Создаем элементы интерфейса Баттона для нижней рамки
        self.cals_button = tkinter.Button(self.button_frme, text = 'Конвертировать', command = self.convert)
        self.quit_button = tkinter.Button(self.button_frme, text = 'Выйти', command = self.main_wind.destroy)

        #пакуем кнопки
        self.cals_button.pack(side ='left')
        self.quit_button.pack(side='left')

        #пакуем рамки
        self.top_frame.pack()
        self.button_frme.pack()

        #войти в главный цикл tkinter
        tkinter.mainloop()

        #метод конвертации
    def convert(self):
        kilo = float(self.kilo_entry.get())
        miles = round(kilo * 0.6214,2)

        #показать результаты в диалоговом окне
        tkinter.messagebox.showinfo('Результаты', str(kilo) + ' км эквивалентно '+ str(miles) +' милям')

#создать экземпляр класса
kilo_conv = KiloComvertGUI()
