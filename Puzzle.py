class Puzzle:
    def __init__(self, tab, x, y, size):
        self.tab = tab
        self.x = x
        self.y = y
        self.size = size

    def make_right(self):
        if (self.x > 0):
            tab = self.tab
            tab[self.y][self.x] = tab[self.y][self.x - 1]
            tab[self.y][self.x - 1] = -1
            return Puzzle(tab, self.x - 1, self.y, self.size)
        else:
            return 0

    def make_left(self):
        if (self.x < self.size - 1):
            tab = self.tab
            tab[self.y][self.x] = tab[self.y][self.x + 1]
            tab[self.y][self.x + 1] = -1
            return Puzzle(tab, self.x + 1, self.y, self.size)
        else:
            return 0

    def make_down(self):
        if (self.y > 0):
            tab = self.tab
            tab[self.y][self.x] = tab[self.y - 1][self.x]
            tab[self.y - 1][self.x] = -1
            return Puzzle(tab, self.x, self.y - 1, self.size)
        else:
            return 0

    def make_up(self):
        if (self.y < self.size - 1):
            tab = self.tab
            tab[self.y][self.x] = tab[self.y + 1][self.x]
            tab[self.y + 1][self.x] = -1
            return Puzzle(tab, self.x, self.y + 1, self.size)
        else:
            return 0
