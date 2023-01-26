import os.path, tempfile


class File:
    """Интерфейс для работы с файлами"""

    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, data):
        with open(self.file_path, 'w') as f:
            f.write(data)

    def read(self):
        with open(self.file_path) as f:
            return f.read()

    def __add__(self, obj):
        file_name = '-'.join([self.file_path, obj.file_path])
        new_file_path = os.path.join(tempfile.gettempdir(), str(hash(file_name)))
        new_obj = File(new_file_path)
        new_obj.write(self.read() + obj.read())

        return new_obj

    def __str__(self):
        return self.file_path

    def __iter__(self):
        return open(self.file_path, 'r')