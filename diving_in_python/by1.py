# from mymodule import multiply

import dis

def multiply(a, b):
    return a * b

dis.dis(multiply)

import opcode
print(opcode.opmap)