
with open("stepic/py_oop/tests/test.txt") as f, open("stepic/py_oop/tests/test2.txt", "w") as w:
    for line in f:
        w.write(line)