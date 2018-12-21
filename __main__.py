import Puzzle as puz
import random
#import matplotlib.pyplot as plt
import time
import numpy as np

def create_final(size):
    i = 0
    j = 0
    way = 0
    move = False
    tab = []
    for k in range(size):
        tab.append([0] * size)
    total = size * size - 1
    for nb in range(total):
        move = False
        tab[i][j] = nb + 1
        nb = nb + 1
        while move == False:
            if way == 0:
                if j >= size - 1 or tab[i][j + 1] != 0:
                    way = (way + 1) % 4
                    continue
                else:
                    j = j + 1
                    move = True
            if way == 1:
                if i >= size - 1 or tab[i + 1][j] != 0:
                    way = (way + 1) % 4
                    continue
                else:
                    i = i + 1
                    move = True
            if way == 2:
                if j <= 0 or tab[i][j - 1] != 0:
                    way = (way + 1) % 4
                    continue
                else:
                    j = j - 1
                    move = True
            if way == 3:
                if i <= 0 or tab[i - 1][j] != 0:
                    way = (way + 1) % 4
                    continue
                else:
                    i = i - 1
                    move = True
    #plt.plot(tab)
    #plt.ylabel('Label 1')
    #plt.show()
    return puz.Puzzle(tab, j, i, size)

def tabcmp(start, final, size):
    '''print ("puzzle :")
    print(np.matrix(start))
    print ("final :")
    print(np.matrix(final))
    print ("size = {}".format(size))'''
    for i in range(size):
        for j in range(size):
            if start[i][j] != final[i][j]:
                #print("{} != {} on i = {} j = {}".format(start[i][j], final[i][j], i, j))
                return False
    return True

def solve(start, final):
    open_set = []
    closed_set = []
    open_set.append(start)
    while tabcmp(start.tab, final.tab, start.size) == False:
        start.print_puzzle()
        time.sleep(1)
        score = start.manhattan(final.tab)
        state1 = start.make_right()
        for i in range(len(open_set)):
            if tabcmp(open_set[i].tab, state1) == False:
                if state1.manhattan(final.tab) < score:
                    print ("right move\n")
                    start = state1
                    open_set.append(state1)
                    continue
            state2 = start.make_left()
            if tabcmp(open_set[i].tab, state2) == False:
                if state2.manhattan(final.tab) < score:
                    print ("left move\n")
                    start = state2
                    open_set.append(state2)
                    continue
                state3 = start.make_up()
            if tabcmp(open_set[i].tab, state3) == False:
                if state3.manhattan(final.tab) < score:
                    print ("up move\n")
                    start = state3
                    open_set.append(state3)
                    continue
                state4 = start.make_down()
                #if state4.manhattan(final.tab) < score:
                print ("down move\n")
                start = state4
                open_set.append(state4)
        continue
    start.print_puzzle()
    print ("Open Set:")
    for i in range(len(open_set)):
        open_set[i].print_puzzle()

def main():
    tab = []
    ran = []
    x = 0
    y = 0
    size = 3
    for k in range(size):
        tab.append([0] * size)
    for l in range(size * size):
        ran.append(l)
    for i in range(size):
        for j in range(size):
            nb = random.choice(ran)
            if nb == 0:
                x = i
                y = j
            tab[i][j] = nb
            ran.remove(nb)
    start = puz.Puzzle(tab, y, x, size)
    print("random N-Puzzle :")
    start.print_puzzle()
    final = create_final(size)
    print ("\nfinal N-Puzzle :")
    final.print_puzzle()
    solve(start, final)
    '''state1 = start.make_down()
    total = start.manhattan(final.tab)
    print ("Manhattan value = {}".format(total))
    print ("\nState1 (move_down) :")
    state1.print_puzzle()
    total2 = state1.manhattan(final.tab)
    print ("Manhattan value = {}".format(total2))
    print ("\nfinal N-Puzzle :")
    final.print_puzzle()'''

if __name__ == "__main__":
    main()
