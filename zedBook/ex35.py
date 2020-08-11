from sys import exit
#запускать из ком строки
def gold_room():
    print("Здесь полно золота - сколько унесешь?")

    choise = input("> ")
    if "0" in choise or "1" in choise:
        how_much = int(choise)
    else:
        dead("ЭЙ НУжно ввести число")

    if how_much < 50:
        print("Ты не жадный поэтому выигрываешь")
        exit(0)
    else:
        dead("Ах ты жадина!")

def bear_room():
    print("Тут сидит медведь")
    print("ОН закрыл выход")
    print("Как переместить медведя? Отобрать мед или подвинуть?")
    bear_moved = False

    while True:
        choise = input("> ")

        if choise == "отобрать мед":
            dead("Медведь посмотрл на тебя и ударил по щщщам")
        elif choise == "подразнить медведя" and not bear_moved:
            print("Медведь отошел от двери")
            print("вы можете войти в нее. Подразнить медведя или войти в дверь")
            bear_moved = True
        elif choise == "подразнить медведя" and bear_moved:
            dead("Медведь разозлился и откусил тебе ногу")
        elif choise == "войти в дверь" and bear_moved:
            gold_room()
        else:
            print("Введите одно из предложенных действий")

def ctulhu_room():
    print("На тебя пырит Ктулху")
    print("ОН смотрит на тебя и ты начинаешь сходить с ума")
    print("Убежать или начать сражаться?")

    choise = input("> ")

    if "убежать"  in choise:
        start()
    elif "начать сражаться" in choise:
        dead("Хм возможно даже удастся победить")
    else:
        ctulhu_room()

def dead(why):
    print(why, "Великолепно!")
    exit(0)

def start():
    print("Ты в темной комнате")
    print("Отсюда ведут две двери, налево и направо")
    print("Куда ты повернешь?")

    choice = input("> ")

    if choice == "налево":
        bear_room()
    elif choice == "направо":
        ctulhu_room()
    else:
        dead("Ты ходишь из комнаты в комнату, пока не умираешь с голоду")
start()