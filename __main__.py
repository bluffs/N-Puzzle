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
        return open_set[0]

def solve(actual, final, func):
    max_open = 0
    open_set = []
    closed_set = []
    path = []
    lowest = 10000
    size = actual.size
    open_set.append(actual)
    total = 1
    max_open = 0
    while actual != 0:
        #time.sleep(1)
        #print ("\nopen size = {}".format(len(open_set)))
        #print ("closed size = {}".format(len(closed_set)))
        #print("actual best =")
        if actual.f < lowest:
            lowest = actual.f
            #actual.print_puzzle()
        #print("f = {}, lowest = {}".format(actual.f, lowest))
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
            print("path size = {}".format(len(path)))
            print("total = {}".format(total))
            print("max open_set = {}".format(max_open))
            print("closed_set length = {}".format(len(closed_set)))
            sys.exit()
        open_set.remove(actual)
        closed_set.append(actual)
        state1 = actual.make_right()
        if visited(open_set, closed_set, state1, size) == False:
            state1.f = func(state1, final.tab)
            i = 0
            added = False
            for state in open_set:
                if state1.f < state.f:
                    open_set.insert(i, state1)
                    added = True
                    break
                i = i + 1
            if not added:
                open_set.append(state1)
            total = total + 1
        state2 = actual.make_left()
        if visited(open_set, closed_set, state2, size) == False:
            state2.f = func(state2, final.tab)
            i = 0
            added = False
            for state in open_set:
                if state2.f < state.f:
                    open_set.insert(i, state2)
                    added = True
                    break
                i = i + 1
            if not added:
                open_set.append(state2)
            total = total + 1
        state3 = actual.make_up()
        if visited(open_set, closed_set, state3, size) == False:
            state3.f = func(state3, final.tab)
            i = 0
            added = False
            for state in open_set:
                if state3.f < state.f:
                    open_set.insert(i, state3)
                    added = True
                    break
                i = i + 1
            if not added:
                open_set.append(state3)
            total = total + 1
        state4 = actual.make_down()
        if visited(open_set, closed_set, state4, size) == False:
            state4.f = func(state4, final.tab)
            i = 0
            added = False
            for state in open_set:
                if state4.f < state.f:
                    open_set.insert(i, state4)
                    added = True
                    break
                i = i + 1
            if not added:
                open_set.append(state4)
            total = total + 1
        actual = best_open(open_set)
        len_open = len(open_set)
        if max_open < len_open:
            max_open = len_open
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

def create_snail_list(tab, size):
    nb_list = []
    n = 0
    i = 0
    j = 0
    way = 0
    while len(nb_list) < size * size:
        if way == 0:
            if j < size - n:
                nb_list.append(tab[i][j])
                j = j + 1
                continue
            else:
                way = (way + 1) % 4
                j = j - 1
                i = i + 1
                continue
        if way == 1:
            if i < size - n:
                nb_list.append(tab[i][j])
                i = i + 1
                continue
            else:
                way = (way + 1) % 4
                i = i - 1
                j = j - 1
                continue
        if way == 2:
            if j >= n:
                nb_list.append(tab[i][j])
                j = j - 1
                continue
            else:
                way = (way + 1) % 4
                j = j + 1
                i = i - 1
                n = n + 1
                continue
        if way == 3:
            if i >= n:
                nb_list.append(tab[i][j])
                i = i - 1
                continue
            else:
                way = (way + 1) % 4
                i = i + 1
                j = j + 1
                continue
    #print nb_list
    return nb_list

def count_inversions(tab, size):
    nb_list = []
    #nb_list = create_snail_list(tab, size)
    count = 0
    if (size & 1):
        nb_list = create_snail_list(tab, size)
    else:
        for i in range(size):
            for j in range(size):
                nb_list.append(tab[i][j])
    for i in range(size * size):
        for j in range(i, size * size):
            if nb_list[j] != 0 and nb_list[i] > nb_list[j]:
                count = count + 1
    return count

def is_solvable(puzzle, size):
    nb = count_inversions(puzzle.tab, size)
    #print nb
    if size & 1:
        if nb & 1 == 0:
            #print("N is odd and nb is even")
            return True
    else:
        #print("row of 0 = {}".format(size - puzzle.y))
        if nb & 1 and (size - puzzle.y) & 1 == 0:
            return True
        if nb & 1 == 0 and (size - puzzle.y) & 1:
            return True
    return False

def check_file(filename):
    #handle error on open
    tab = []
    file = open(filename, 'r')
    lines = file.readlines()
    for line in lines:
        data = (line[:-1].split('#'))
        if data[0] != '':
            tab.append(data[0])
    size = int(tab[0])
    if len(tab) != int(tab[0]) + 1:
    #check if tab[0] has no other characters than the number of lines (to make sure it's not a puzzle line)
        print("bad number of lines")
        exit()
    #print tab
    clean_data = []
    for line in tab[1:]:
        data = line.split(' ')
        line_data = []
        for d in data:
            if d != '':
                line_data.append(int(d))
        clean_data.append(line_data)
    #print clean_data
    x = 0
    y = 0
    for nb in range(size * size):
        found = False
        for i in range(size):
            for j in range(size):
                if clean_data[i][j] == nb:
                    found = True
        if not found:
            print("nb = {} not found".format(nb))
            exit()
    for i in range(size):
        for j in range(size):
            if clean_data[i][j] == 0:
                y = i
                x = j
            #print clean_data[i][j]
    file.close()
    start = puz.Puzzle(clean_data, x, y, size, 0)
    return start

def main():
    random.seed(datetime.now())
    start = 0
    size = 0
    heuristic_nb = 0
    #start = create_random(size)
    if len(sys.argv) == 2:
        #test the input file, start = create_from_file
        #print("argv = {}".format(sys.argv[1]))
        start = check_file(sys.argv[1])
    else:
        random.seed(datetime.now())
        while size not in range(1, 5):
            try:
                size = int(raw_input("What size ?\n"))
            except ValueError:
                print("Bad Input")
                pass
        start = create_random(size)
        while not is_solvable(start, size):
            print("unsolvable puzzle")
            start = create_random(size)
        print("SOLVABLE PUZZLE")
    final = create_final(size)
    heuristics = []
    heuristics.append([1, puz.Puzzle.manhattan])
    heuristics.append([2, puz.Puzzle.hamming])
    heuristics.append([3, puz.Puzzle.linear_conflict])
    print("1-Manhattan\n2-Hamming\n3-Linear Conflict/Manhattan")
    while heuristic_nb not in range(1, 4):
        try:
            heuristic_nb = int(raw_input("Which heuristic ?\n"))
        except ValueError:
            print("Bad Input")
            pass
    heuristic = heuristics[heuristic_nb - 1][1]
    start.f = heuristic(start, final.tab)
    '''if not is_solvable(start, size):
        print("unsolvable puzzle")
    else:
        print("SOLVABLE PUZZLE")'''
    print("random N-Puzzle :")
    start.print_puzzle()
    print ("\nfinal N-Puzzle :")
    final.print_puzzle()
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass
    solve(start, final, heuristic)

if __name__ == "__main__":
    main()
