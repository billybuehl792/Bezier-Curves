#!python3
# curves.py - curve plotting

from bezier import get_coord
from matplotlib import pyplot as plt

def get_point(t, p1, p2, ease_in, ease_out):
    influence = t * ease_out

    point = 0

    return (t, point)

def x_at_y(y0, y1, y2, y3, x):
    return (1-x)**3 * y0 + 3*(1-x)**2 * x * y1 + 3*(1-x) * x**2 * y2 + x**3 * y3

if __name__ == '__main__':
    print('\noutput: \n')

    x_positions = []
    y_positions = []
    p = 30
    for i in range(p+1):
        t = round(((1/p) * i), 1) 
        coord = x_at_y(0, 0, 1, 1, t)
        x_positions.append(coord)
        y_positions.append(t)
        # print(f't: {t}, X: {round(coord[0], 2)} | Y: {round(coord[1], 2)}')

    plt.plot(x_positions, y_positions)
    plt.title("stupid curve")
    plt.xlabel = "X"
    plt.ylabel = "Y"
    plt.show()

    print('\ndone.')
