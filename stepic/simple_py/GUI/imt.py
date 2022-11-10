from tkinter import *

root = Tk()
root.title('Индекс массы тела')
root.geometry('640x480')
root.resizable(width=False, height=False)

#Wigets
labl_for_height = Label(
    text='Введите ваш рост,(м)',
    font=('Consolas','18')
)

entry_for_height = Entry(
    width=10,
    font=('Consolas','30'),
    justify=CENTER
)

labl_for_weight = Label(
    text='Введите ваш вес,(кг)',
    font=('Consolas','18')
)

entry_for_weight = Entry(
    width=10,
    font=('Consolas','30'),
    justify=CENTER
)

def calculate() -> str:
    height = float(entry_for_height.get().replace(',','.').strip())
    weigth = float(entry_for_weight.get().replace(',','.').strip())

    # bmi = weigth / (height ** 2)

    bmi = round(weigth / (height ** 2), 2)

    if bmi < 15.99:
        status = 'выраженный дефицит массы тела'
    elif bmi > 16 and bmi < 18.49:
        status = 'недостаточная масса тела'
    elif bmi > 18.5 and bmi < 24.99:
        status = 'норма'
    elif bmi > 25 and bmi < 29.99:
        status = 'предожирение'
    elif bmi > 30 and bmi < 34.99:
        status = '1 степень ожирения'
    elif bmi > 35 and bmi < 39.99:
        status = '2 степень ожирения'
    else:
        status = '3 степень ожирения'

    result_label = Label(
        text=f'''
    Ваш ИМТ: {bmi} кг/м2\n
    Это {status}
        ''',
        font=('Consolas', '18')
    )
    result_label.pack()


submit_button = Button(
    text='Рассчитать',
    font=('Consolas', '16'),
    command=calculate
)

#Placing Wigets

labl_for_height.pack()
entry_for_height.pack()
labl_for_weight.pack()
entry_for_weight.pack()
submit_button.pack()

if __name__ == '__main__':
    root.mainloop()