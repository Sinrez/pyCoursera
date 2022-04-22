# one_dollar = 2
# print(f"{one_dollar:05}")

class Date:
    def __init__(self,d,m,y):
        self.d = d
        self.m = m
        self.y = y

    @property
    def date(self):
        return f'{self.d:02}/{self.m:02}/{self.y:04}'

    @property
    def usa_date(self):
        return f'{self.m:02}-{self.d:02}-{self.y:04}'


d1 = Date(5, 10, 2001)
d2 = Date(15, 3, 999)

print(d1.date) # 05/10/2001
print(d1.usa_date) # 10-05-2001
print(d2.date) # 15/03/0999
print(d2.usa_date) # 03-15-0999