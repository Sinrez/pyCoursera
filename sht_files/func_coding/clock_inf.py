from datetime import datetime as dt
from datetime import time
from datetime import timedelta

class Clock():
    def __init__(self,h = 0,  m = 0, s = 0, max_h = 86400):
        self.n = 0

        self.time1 = dt(1,1,1,h,m,s)
        self.max_h = max_h
    def __next__(self):

        self.n+=1
        # if self.max_h == self.n:
        #     raise StopIteration
        self.result = self.time1
        self.time1 = self.result + timedelta(seconds = 1)
        return self.result.strftime("%H:%M:%S")
    def __iter__(self):
        self.h = 0
        self.m = 0
        self.s = 0
        self.n = 0
        return self
