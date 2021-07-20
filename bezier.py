#!python3
# bezier_fun.py - bezier plotting

import pandas as pd
from matplotlib import pyplot as plt

def get_coord(t, t_start, t_stop, start_val, stop_val, ease_out, ease_in):
    # single parameter bezier
    # time on x axis
    p1 = t_start
    p4 = t_stop

def get_coord2(t, p1, p2):
    x = ((1-t) * p1[0]) + (t * p2[0])
    y = ((1-t) * p1[1]) + (t * p2[1])

    return int(x), int(y)

def get_coord4(t, p1, p2, p3, p4):
    x = ((1-t)**3 * p1[0]) + (3 * (1-t)**2 * t * p2[0]) + (3 * (1-t) * t**2 * p3[0]) + (t**3 * p4[0])
    y = ((1-t)**3 * p1[1]) + (3 * (1-t)**2 * t * p2[1]) + (3 * (1-t) * t**2 * p3[1]) + (t**3 * p4[1])

    return round(x,2), round(y,2)
    
def easeCustom(t, t_start, t_stop, p1, p4, ease_out, ease_in):
    # 1/duration * (distance from animation start)
    t_trans = 1 / (t_stop-t_start) * (t - t_start)
    p2 = 

if __name__ == '__main__':
    print('\noutput: \n')
    positions = 30
    x_positions = []
    y_positions = []

    # animation starts at 2s and goes to 7s
    times = [2, 3, 4, 5, 6, 7]
    for t in times:
        x, y = easeCustom(t, 2, 7, (0,0), (10,10), .33, 1)
    # for i in range(positions+1):
    #     t = i / positions
    #     # x, y = get_coord4(t, (3,10), (10,0), (0,0), (7,10))
    #     # x, y = get_coord4(t, (0,0), (3,0), (0,10), (10,10))
    #     x, y = get_coord2(t, (0,0), (10,10))
    #     x_positions.append(x)
    #     y_positions.append(y)

    plt.plot(x_positions, y_positions)
    plt.title('Bezier')
    plt.show()

    print('\ndone.')