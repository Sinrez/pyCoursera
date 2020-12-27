import matplotlib.pyplot as plt

def main():
    x_coords = [0,1,2,3,4]
    y_coords = [0, 3, 1, 5,2]

    plt.plot(x_coords, y_coords)

    plt.title('Образец данных')

    plt.xlabel('Это ось Х')
    plt.xlabel('Это ось Y')

    #сетку
    plt.grid(True)

    plt.show()

main()
