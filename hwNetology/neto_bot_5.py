HELP = """Доступные команды: 
help - Напечатать справку
add - добавить задачу в список, выберите когда планиурете сдеалать задачу. Введите "Сегодня" для текщих задач, "Завтра" - для завтрашних задач, если в любое другое время - введите проищвольное слово
print - напечатать все задачи из списка
exit - выход из программы"""

# tasks = ['Убраться дома']
tomorrow = []
other = []
today = []

print(HELP)

while True:  # True == True верно всегда
    # Будет выполняться всегда (бесконечно)
    command = input('Введите команду: ')
    command = command.strip().lower()
    if command == 'help':
        print(HELP)
    elif command == 'add':
        date = input('Введите когда планиурете задачу Сегодня, Завтра или Иное: ')
        task = input('Введите задачу: ')

        if date == "Сегодня":
            today.append(task)
        elif date == "Завтра":
            tomorrow.append(task)
        else:
            other.append(task)
        # tasks.append(task)
    elif command == 'print':
        for t in today:
            print('Сегодня')
            print(t, end='\n')
            print('###############')
        for tm in tomorrow:
            print('Завтра')
            print(tm, end='\n')
            print('###############')
        for o in other:
            print('Когда-то')
            print(o, end='\n')

    elif command == 'exit':
        print("Спасибо за использование! До свидания!")
        break
    else:
        # Пока не встретится ключевое слово break
        print('Неизвестная команда')
        break