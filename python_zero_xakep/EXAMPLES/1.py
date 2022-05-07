# Откроем 6.txt для чтения из него строк
f1=open('myfiles/emails1.txt', 'r', encoding='UTF-8')
# Откроем файл result/gmailcom.txt для дозаписи строк в конец файла
# Если файла нет то он будет создан
f2=open('result/gmailcom.txt', 'a', encoding='UTF-8')
# Откроем файл result/mailru.txt для дозаписи строк в конец файла
# Если файла нет то он будет создан
f3=open('result/mailru.txt', 'a', encoding='UTF-8')

# Пробежим в цикле по строкам 6.txt
for x in f1:
    # Если у нас есть пробел между почтой и паролем
    # и строка длиннее 4 символов
    if(' ' in x.strip() and len(x.strip())>4):
        # Разделим строку по пробелу на список из двух элементов
        xmas = x.split()
        # В переменную email запишем первую часть 
        email= xmas[0]
        # В переменную password вторую часть
        password = xmas[1]
        # Напечатаем текущие email и пароль
        print('Найден e-mail: '+email+' и пароль: '+password)
        # Если email содержит подстроку 'gmail.com'
        # Добавим строчку с ним в файл result/gmailcom.txt
        if 'gmail.com' in email:
            f2.write(x)
        # Если email содержит подстроку 'mail.ru'
        # Добавим строчку с ним в файл result/mailru.txt    
        if 'mail.ru' in x:
            f3.write(x)

# Закроем все три файла
f1.close()
f2.close()
f3.close()

print('Готово! Результаты записаны в папку result')
           
