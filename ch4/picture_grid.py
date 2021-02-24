#! python3

"""
https://automatetheboringstuff.com/2e/chapter4/
Automate the Boring Stuff Chapter 4 Practice Project:
Character Picture Grid
"""

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

grid_two = [list("..OO.OO.."),
            list(".OOOOOOO."),
            list(".OOOOOOO."),
            list("..OOOOO."),
            list("...OOO..."),
            list("....O...."),]

def make_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end="")
        print("")

make_grid(grid)
print("\n", "*" * 10, "BREAK", "*" * 10, "\n")
make_grid(grid_two)