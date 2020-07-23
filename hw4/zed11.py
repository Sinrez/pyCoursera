def print_two(*args):
    #запуск из ком строки
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("А я ничего не получаю")

print_two("Мих","Райтм")
print_two_again("Мих", "Райт")
print_one("первый")
print_none()
