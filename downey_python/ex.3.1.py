def right_justify(s):
    z = str(s)
    l = len(z)
    l_space = 70 - l
    space = ' ' * l_space
    return space + z

if __name__ == "__main__":
    print(right_justify('monty'))


