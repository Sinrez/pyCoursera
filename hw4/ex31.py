print("ты находишься в комнате с 2 дверями, какую выбираешь 1 или 2?")
#запускать из ком строки
door = input("> ")

if door == "1":
    print("В этой комнате гигантский медведь поедает сырок  'Дружба'.")
    print("Твои действия?")
    print("1 Отберу сырок")
    print("2. Заору медведю на ухо")

    bear  =input("> ")

    if bear == "1":
        print("Медведь вцепился тебе в лицо, Отлично-отлично")
    elif bear == "2":
        print("Медведь укусил за ногу, Отлично-отлично")
    else:
        print(f"Прекрасно, действие {bear} было единственным верным")
        print("Медведь убежал прочь")

elif door == "2":
    print("Ты смотришь в бесконечную пропасть глаз Ктулху, твои действия:")
    print("1 Расскажу Ктулху про бесконечные топи в Сибири")
    print("2 Потреплю пуговицы на своей куртке")
    print("3 Петь песню черный ворон")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Ты спасся, потому что Ктулху превратился в желе")
        print("Отлично-отлично, например")
    else:
        print("Безумие охватило тебя, и ты упал в байссейн с гнилью")
        print("Отлично")
else:
    print("Безумие охватило тебя")

