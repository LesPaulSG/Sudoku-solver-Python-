import copy
import sys

def output(a):
    sys.stdout.write(str(a))

def printGrid(Grid):
    for i in range(9):
        for j in range(9):
            output(Grid[i][j])
            if (j + 1) % 3 == 0 and j < 8:
                output(' |')
            if j != 8:
                output(' ')
        output('\n')
        if (i + 1) % 3 == 0 and i < 8:
            output("------|-------|------\n")

def Sudoku(solution):
    minPoss = None
    while True:
        minPoss = None
        for i in range(9):
            for j in range(9):
                if solution[i][j] != 0:
                    continue
                CanUse = canUse(i, j, solution)
                if len(CanUse) == 0:
                    return False
                if len(CanUse) == 1:
                    solution[i][j] = CanUse.pop()
                if not minPoss or \
                    len(CanUse) < len(minPoss[1]):
                    minPoss = ((i, j), CanUse)
        if not minPoss:
            return True
        elif 1 < len(minPoss[1]):
            break
    row, column = minPoss[0]
    for var in minPoss[1]:
        temp = copy.deepcopy(solution)
        temp[row][column] = var
        if Sudoku(temp):
            for row in range(9):
                for column in range(9):
                    solution[row][column] = temp[row][column]
            return True
    return False

def canUse(row, column, puzzle):
    arr = {var for var in range(1, 10)}
    arr -= set(puzzle[row][:])
    arr -= {puzzle[r][column] for r in range(9)}
    arr -= blocked(row, column, puzzle)
    return arr

def blocked(row, column, puzzle):
    rowStart = 3*(row // 3)
    columnStart = 3*(column // 3)
    return {
        puzzle[rowStart+r][columnStart+c]
            for r in range(3)
            for c in range(3)
    }

Grid = [[0,0,3,0,0,2,0,0,0],
        [5,0,0,0,6,0,1,2,0],
        [9,0,0,0,0,0,0,0,4],
        [0,0,8,0,7,0,0,0,0],
        [0,0,0,0,0,3,0,0,8],
        [0,3,6,0,0,0,7,0,0],
        [0,7,0,9,2,0,0,0,0],
        [0,0,0,0,0,5,0,9,6],
        [0,0,0,8,0,4,5,0,0]]

if Sudoku(Grid):
    print("Solution:")
    printGrid(Grid)
else:
    print("Solution not found")