import sys
from mywindow import *
from PyQt5 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Вешаем на кнопку функцию PoemCheck
        self.ui.pushButton.clicked.connect(self.PoemCheck)

    # Описываем функцию 
    def PoemCheck(self):
        # Очищаем второе текстовое поле
        self.ui.textEdit_2.setText("")
        # В переменную stroki получаем текст из левого поля ввода
        stroki=self.ui.textEdit.toPlainText()
        # Получаем массив строк разделив текст по знаку переноса строки
        mas=stroki.split('\n')
        # Обнуляем переменную где будут копиться проверенные строки
        rezultat=''
        # Массив гласных букв для подсчёта колиества слогов
        glasnye=['а','е','ё','и','о','у','э','ю','я','ы']
        # Перебираем каждую строку стиха
        for stroka in mas:
            kol=0 # Переменная с количеством гласных в строке
            # Перебираем все буквы в строке
            for w in stroka.lower():
                # По очереди сравниваем буквы с гласными
                for bukva in glasnye:
                    # Если буква гласная увеличиваем счетчик
                    if(w==bukva): kol=kol+1
            if(kol>0):
                # Добавляем в конце строки количество слогов
                rezultat=rezultat+stroka+' - '+str(kol)+' слогов'+'\n'
            else:
                rezultat=rezultat+'\n'
        # Выводим в правое поле переменную результат с количеством слогов в строке
        self.ui.textEdit_2.setText(rezultat)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
