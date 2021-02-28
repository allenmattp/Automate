# Conway's "Game of Life"

import random, time, copy
WIDTH = 60
HEIGHT = 20

# create a list of lists for the cells:
nextCells = []
for x in range(WIDTH):
    column = [] # column contains living and dead cells
    for y in range(HEIGHT):
        if not random.randint(0, 1):
            column.append("#") # Add a living cell if 1
        else:
            column.append(" ") # Add a dead cell if 0
    nextCells.append(column) # nextCells is a list of the lists 'column'

while True: # main program loop
    print("\n\n\n\n\n")
    currentCells = copy.deepcopy(nextCells) # make a copy of nextCells and all its inner lists

    # print currentCells
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end="") # print out each cell
        print() # print a line break at end of each row

    # calculate next step
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # check neighbors
            # Use % to ensure within range
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == "#":
                numNeighbors += 1 # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom-right neighbor is alive.

            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == "#" and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = "#"
            elif currentCells[x][y] == " " and numNeighbors == 3:
                nextCells[x][y] = "#"
            else:
                nextCells[x][y] = " "
    time.sleep(1)