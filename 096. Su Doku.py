import numpy as np

def read_file(file):
    with open(file) as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith("Grid")]

    data = np.array([[int(c) for c in line] for line in lines])

    n_grids = data.shape[0] // 9
    grids = np.split(data, n_grids)

    return grids

# Function to check if it is safe to place num at mat[row][col]
def isSafe(mat, row, col, num):
    
    # Check if num exists in the row
    for x in range(9):
        if mat[row][x] == num:
            return False

    # Check if num exists in the col
    for x in range(9):
        if mat[x][col] == num:
            return False

    # Check if num exists in the 3x3 sub-matrix
    startRow = row - (row % 3)
    startCol = col - (col % 3)

    for i in range(3):
        for j in range(3):
            if mat[i + startRow][j + startCol] == num:
                return False

    return True

# Function to solve the Sudoku problem
def solveSudokuRec(mat, row, col):
    # base case: Reached nth column of the last row
    if row == 8 and col == 9:
        return True

    # If last column of the row go to the next row
    if col == 9:
        row += 1
        col = 0

    # If cell is already occupied then move forward
    if mat[row][col] != 0:
        return solveSudokuRec(mat, row, col + 1)

    for num in range(1, 10):
        
        # If it is safe to place num at current position
        if isSafe(mat, row, col, num):
            mat[row][col] = num
            if solveSudokuRec(mat, row, col + 1):
                return True
            mat[row][col] = 0

    return False

def solveSudoku(mat):
    solveSudokuRec(mat, 0, 0)

if __name__ == "__main__":
    sum = 0
    c = 0
    grids = read_file("0096_sudoku.txt")
    for mat in grids:
        solveSudoku(mat)
        sum += mat[0][0]*100 + mat[0][1]*10 + mat[0][2]
        
    print(sum)
    
    
        