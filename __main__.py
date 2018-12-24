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

def visited(open_set, closed_set, state, size):
    for state1 in open_set:
        print("testing")
        state1.print_puzzle()
        if tabcmp(state1.tab, state.tab, size) == False:
            return True
    for state1 in closed_set:
        if tabcmp(state1.tab, state.tab, size) == False:
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
        print ("returning this puzzle")
        choose.print_puzzle
	return choose
    choose = list_state[0]
    score = list_state[0].manhattan(final.tab)
    for state in list_state:
    	scorecmp = state.manhattan(final.tab)
        if scorecmp <= score:
    	    score = scorecmp
	    choose = state
    print ("returning this puzzle")
    choose.print_puzzle
    return choose

def solve(actual, final):
    open_set = []
    closed_set = []
    size = actual.size
    while tabcmp(actual.tab, final.tab, size) == False:
        actual.print_puzzle()
        time.sleep(1)
        closed_set.append(actual)
        #find another way to clean the list
        list_state = []
        state1 = actual.make_right()
        if visited(open_set, closed_set, state1, size) == False:
            list_state.append(state1)
        state2 = actual.make_left()
        if visited(open_set, closed_set, state2, size) == False:
            list_state.append(state2)
        state3 = actual.make_up()
        if visited(open_set, closed_set, state3, size) == False:
            list_state.append(state3)
        state4 = actual.make_down()
        if visited(open_set, closed_set, state4, size) == False:
            list_state.append(state4)
        if not list_state:
            print("empty list, must go back 1 state")
        score = actual.manhattan(final.tab)
        actual = best_state(score, list_state, final)


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
