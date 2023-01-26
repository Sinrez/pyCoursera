from os.path import exists
from tempfile import gettempdir
from os.path import join


class File:
    add_helper = 0

    def __init__(self, path_to_file):
        if not exists(path_to_file):
            open(path_to_file, "w").close()
        self.path_to_file = path_to_file

    def __str__(self):
        return self.path_to_file

    def __iter__(self):
        self.current = 0
        with open(self.path_to_file, "r") as f:
            self.lines = f.readlines()
        return self

    def __next__(self):
        if len(self.lines) == self.current:
            raise StopIteration
        line = self.lines[self.current]
        self.current += 1
        return line

    def __add__(self, obj):
        File.add_helper += 1
        new_obj = File(join(gettempdir(), str(self.add_helper)))
        new_obj.write(self.read() + obj.read())
        return new_obj

    def read(self):
        with open(self.path_to_file, "r") as f:
            return f.read()

    def write(self, data):
        with open(self.path_to_file, "w") as f:
            f.write(data)
            print(len(data))


if __name__ == "__main__":
    pass