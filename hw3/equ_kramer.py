a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
# ax + by = e
# cx + dy = f
# решаем через формулу Крамера
determinant = a * d - b * c  # находим определитель системы
# если determinant != 0, то система имеет только одно решение
kramerX = (e * d - f * b) / determinant
kramerY = (a * f - c * e) / determinant
x = '{0:.6f}'.format(kramerX)
y = '{0:.6f}'.format(kramerY)
print(x, y)
