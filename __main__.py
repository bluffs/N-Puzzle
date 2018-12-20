import Puzzle as puz
import random
#import matplotlib.pyplot as plt
import time

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
    for i in range(size):
        for j in range(size):
            if start[i][j] != final[i][j]:
                print("{} != {}".format(start[i][j], final[i][j]))
                return False
    return True

def solve(start, final):
    start.print_puzzle()
    while tabcmp(start.tab, final.tab, start.size) == False:
        time.sleep(1)
        score = start.manhattan(final.tab)
        state1 = start.make_right()
        if state1.manhattan(final.tab) < score:
            print ("right move")
            solve(state1, final)
        state2 = start.make_left()
        elif state2.manhattan(final.tab) < score:
            print ("left move")
            solve(state2, final)
        state3 = start.make_up()
        elif state3.manhattan(final.tab) < score:
            print ("up move")
            solve(state3, final)
        state4 = start.make_down()
        #if state4.manhattan(final.tab) < score:
        else:
            print ("down move")
            solve(state4, final)

def main():
    tab = []
    ran = []
    x = 0
    y = 0
    size = 2
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
