class Notebook:
    def __init__(self, lst):
        self._notes = lst

    @property
    def notes_list(self):
        for i in range(0, len(self._notes)):
            print(f'{i+1}.{self._notes[i]}')

note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list