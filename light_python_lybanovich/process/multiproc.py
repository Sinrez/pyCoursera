import multiprocessing
from datetime import datetime
from time import sleep

def now(seconds):
    sleep(seconds)
    print('wait', seconds, 'seconds, time is', datetime.utcnow())


if __name__ == '__main__':
    import random
    for n in range(3):
        seconds = random.random()
        proc = multiprocessing.Process(target=now, args=(seconds,))
        proc.start()