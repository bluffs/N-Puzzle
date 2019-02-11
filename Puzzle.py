import numpy as np

class Puzzle:
    def __init__(self, tab, x, y, size, parent):
        self.tab = tab
        self.x = x
        self.y = y
        self.size = size
        self.parent = parent
        self.nb_list = []
        for i in range(self.size):
            for j in range(self.size):
                self.nb_list.append(tab[i][j])
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

    def hamming(self, final):
        total = 0
        for i in range(self.size):
            for j in range(self.size):
                nb = self.tab[i][j]
                if nb == 0:
                    continue
                pt = self.find(final, nb)
                if i != pt[0] or j != pt[1]:
                    total = total + 1
        return total

    def count_conflicts(self, tab1, tab2):
        total = 0
        nb_list = []
        nb_listf = []
        for j in range(self.size):
            if tab1[j] != 0 and tab1[j] in tab2:
                nb_list.append(tab1[j])
            if tab2[j] != 0 and tab2[j] in tab1:
                nb_listf.append(tab2[j])
        for j in range(len(nb_list) - 1):
            nb = nb_list[j]
            nb2 = nb_list[j + 1]
            place = -1
            place2 = -1
            for k in range(len(nb_listf)):
                if nb_listf[k] == nb:
                    place = k
                if nb_listf[k] == nb2:
                    place2 = k
            if place > place2:
                total = total + 1
        return total

    def linear_conflict(self, final):
        total = 0
        for i in range(self.size):
            hori = []
            horif = []
            verti = []
            vertif = []
            for j in range(self.size):
                hori.append(self.tab[i][j])
                horif.append(final[i][j])
                verti.append(self.tab[i][j])
                vertif.append(final[i][j])
            total = self.count_conflicts(hori, horif) + self.count_conflicts(verti, vertif)
        total = total + self.manhattan(final)
        return total
