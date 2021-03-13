import pickle
import struct

with open('bill.data', "rb") as f:
    data = f.read()
    bill, date, amount = struct.unpack('h10sh', data)
    print(amount)