import Puzzle as puz
import sys
import random
#import matplotlib.pyplot as plt
import time
import numpy as np
from datetime import datetime

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
    return puz.Puzzle(tab, j, i, size, 0)

def tabcmp(start, final, size):
    for i in range(size):
        for j in range(size):
            if start[i][j] != final[i][j]:
                #if arrays are different, return False
                return False
    return True

def visited(open_set, closed_set, state, size):
    for state1 in open_set:
        if tabcmp(state1.tab, state.tab, size) == True:
            return True
    for state1 in closed_set:
        if tabcmp(state1.tab, state.tab, size) == True:
            return True
    return False

def best_state(score, list_state, final):
    choose = 0
    for state in list_state:
	scorecmp = state.manhattan(final.tab)
        if scorecmp < score:
	    score = scorecmp
	    choose = state
    if choose != 0:
	return choose
    choose = list_state[0]
    score = list_state[0].manhattan(final.tab)
    for state in list_state:
    	scorecmp = state.manhattan(final.tab)
        if scorecmp <= score:
    	    score = scorecmp
	    choose = state
    return choose

def best_open(open_set):
    best = 0
    if not open_set:
        return 0
    else:
        best = open_set[0]
    for state in open_set:
        if state.f < best.f:
            best = state
    return best

def solve(actual, final):
    open_set = []
    closed_set = []
    path = []
    lowest = 10000
    size = actual.size
    open_set.append(actual)
    while actual != 0:
        #time.sleep(1)
        #print ("\nopen size = {}".format(len(open_set)))
        #print ("closed size = {}".format(len(closed_set)))
        #print("actual best =")
        if actual.f < lowest:
            lowest = actual.f
            actual.print_puzzle()
        print("f = {}, lowest = {}".format(actual.f, lowest))
        #actual.print_puzzle()
        if actual.f == 0:
            while actual.parent != 0:
                path.insert(0, actual)
                actual = actual.parent
            path.insert(0, actual)
            print("path size = {}".format(len(path)))
            for state in path:
                state.print_puzzle()
                print("")
            sys.exit()
        open_set.remove(actual)
        closed_set.append(actual)
        state1 = actual.make_right()
        if visited(open_set, closed_set, state1, size) == False:
            state1.f = state1.manhattan(final.tab)
            open_set.append(state1)
        state2 = actual.make_left()
        if visited(open_set, closed_set, state2, size) == False:
            state2.f = state2.manhattan(final.tab)
            open_set.append(state2)
        state3 = actual.make_up()
        if visited(open_set, closed_set, state3, size) == False:
            state3.f = state3.manhattan(final.tab)
            open_set.append(state3)
        state4 = actual.make_down()
        if visited(open_set, closed_set, state4, size) == False:
            state4.f = state4.manhattan(final.tab)
            open_set.append(state4)
        actual = best_open(open_set)
    print("Imposible to solve this N-Puzzle")

def create_random(size):
    tab = []
    ran = []
    x = 0
    y = 0
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
    return (puz.Puzzle(tab, y, x, size, 0))

def main():
    random.seed(datetime.now())
    size = 2
    final = create_final(size)
    start = create_random(size)
    start.f = start.manhattan(final.tab)
    print("random N-Puzzle :")
    start.print_puzzle()
    print ("\nfinal N-Puzzle :")
    final.print_puzzle()
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass
    solve(start, final)

if __name__ == "__main__":
    main()
