class AvgList(list):
    def mean(self):
        return(sum(self) / len(self))

    def median(self):
        if len(self) % 2 == 0:
            return (int(self[int(len(self) / 2 - 1)] +  self[int(len(self) / 2)]) / 2)
        else:
            return self[len(self) // 2]

    def median_low(self):
        if len(self) % 2 == 0:
            return self[(len(self) // 2) - 1]
        else:
            return self[len(self) // 2]

    def median_high(self):
            return self[(len(self) // 2)]