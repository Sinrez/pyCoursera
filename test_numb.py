import sys
import string

alphabet = string.ascii_letters + string.digits
base = len(alphabet)


def main():
    m = 3521614606199
    a = 1521614606159
    c = 2521614606179

    for i in range(m):
        value = (a * i + c) % m
        v = value
        letters = []
        for j in range(7):
            letters += alphabet[v % base]
            v = int(v / base)
        code = "".join(letters)
        print(i, value, code)


if __name__ == "__main__":
    sys.exit(main())