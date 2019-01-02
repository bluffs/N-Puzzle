import numpy as np

class Puzzle:
    def __init__(self, tab, x, y, size, parent):
        self.tab = tab
        self.x = x
        self.y = y
        self.size = size
        self.parent = parent
        if parent != 0:
            self.g = parent.g + 1
        else:
            self.g = 0

    def make_right(self):
        if (self.x > 0):
            tab = self.copy_tab()
            tab[self.y][self.x] = tab[self.y][self.x - 1]
            tab[self.y][self.x - 1] = 0
            return Puzzle(tab, self.x - 1, self.y, self.size, self)
        else:
            return self

    def make_left(self):
        if (self.x < self.size - 1):
            tab = self.copy_tab()
            tab[self.y][self.x] = tab[self.y][self.x + 1]
            tab[self.y][self.x + 1] = 0
            return Puzzle(tab, self.x + 1, self.y, self.size, self)
        else:
            return self

    def make_down(self):
        if (self.y > 0):
            tab = self.copy_tab()
            tab[self.y][self.x] = tab[self.y - 1][self.x]
            tab[self.y - 1][self.x] = 0
            return Puzzle(tab, self.x, self.y - 1, self.size, self)
        else:
            return self

    def make_up(self):
        if (self.y < self.size - 1):
            tab = self.copy_tab()
            tab[self.y][self.x] = tab[self.y + 1][self.x]
            tab[self.y + 1][self.x] = 0
            return Puzzle(tab, self.x, self.y + 1, self.size, self)
        else:
            return self

    def print_puzzle(self):
        print(np.matrix(self.tab))

    def copy_tab(self):
        tab = []
        for k in range(self.size):
            tab.append([0] * self.size)
        for i in range(self.size):
            for j in range(self.size):
                tab[i][j] = self.tab[i][j]
        return tab

    def find(self, final, nb):
        pt = []
        for i in range(self.size):
            for j in range(self.size):
                if final[i][j] == nb:
                    pt.append(i)
                    pt.append(j)
                    return pt

    def manhattan(self, final):
        total = 0
        for i in range(self.size):
            for j in range(self.size):
                nb = self.tab[i][j]
                if nb == 0:
                    continue
                pt = self.find(final, nb)
                total = total + abs(i - pt[0]) + abs(j - pt[1])
        return total
