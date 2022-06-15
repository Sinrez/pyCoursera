import pickle

class Tiny():
    def __str__(self):
        return 'tiny'

obj1 = Tiny()
print(obj1)
print(str(obj1))

pickled = pickle.dumps(obj1)
print(pickled)

obj2 = pickle.loads(pickled)
print(obj2)

