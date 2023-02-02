voted = {}

def voting(name):
    if voted.get(name):
        print('GO away!')
    else:
        voted[name] = True
        print(f'Please vote {name}!')

voting('John')
voting('Peter')
voting('John')