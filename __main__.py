import Puzzle as puz

def main():
    tab = []
    for i in range(3):
        tab.append([0] * 3)
    for i in range(3):
        for j in range(3):
            tab[i][j] = i * 3 + j
    print tab
    #tab[0][1] = 1
    #puz.Puzzle()


if __name__ == "__main__":
    main()
