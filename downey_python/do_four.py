def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

def do_four(f):
    do_twice(f)
    do_twice(f)

if __name__ == "__main__":
    do_four(print_spam)