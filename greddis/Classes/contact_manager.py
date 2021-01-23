import contrat

import pickle

#const for menu

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

#global const for file name
FILENAME = 'contacts.dat'

#maim func
def main():
    mycontacts = load_contacts()

#переменная для выбора пользователя
choise = 0

while choise != QUIT:
    choise = get_menu_choise()

    if choise == LOOK_UP:
        look_up(mycontacts)
    elif choise == ADD:
        add(mycontacts
    elif choise == CHANGE:
        change(mycontacts)
    elif choise == DELETE:
        delete(mycontacts)

save_contacts(mycontacts)


