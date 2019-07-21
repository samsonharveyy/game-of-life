""" Simple Conway's Game of Life simulator """

def displayGrid(grid):
    """ Displays current contents of the grid """
    for lines in grid:
        print(lines)

def initialGrid(grid, file):
    """ Sets the initial grid state """
    x = file.readline()
    lines_in_file = [single_line.strip('\n') for single_line in file.readlines()]
    
    #filters given iterable
    #element for element in iterable in this case
    filtered = list(filter(None, lines_in_file))
    for single_line in filtered:
        plot_values = [single_line.split(",")]
        for single_row, single_column in plot_values:
            grid[int(single_row)][int(single_column)] = 1

def checkNeighbor(grid):
    """ Determines the correct number of neighbors of a coordinate in the grid """
    rows = len(grid)
    columns = len(grid[0])
    neighbors = [[0,]*columns for x in range(rows)]
    for single_column in range(columns):
        for single_row in range(rows):
            # Checks and counts for neighbors in corner cases
            if single_row==0 and single_column==0:
                neighbors[single_row][single_column] = grid[single_row+1][single_column+1] +\
                                                       grid[single_row][single_column+1] +\
                                                       grid[single_row+1][single_column]
            elif single_row==0 and single_column==20:
                neighbors[single_row][single_column] = grid[single_row+1][single_column-1] +\
                                                       grid[single_row][single_column-1] +\
                                                       grid[single_row+1][single_column]
            elif single_row==20 and single_column==0:
                neighbors[single_row][single_column] = grid[single_row-1][single_column+1] +\
                                                       grid[single_row][single_column+1] +\
                                                       grid[single_row-1][single_column]
            elif single_row==20 and single_column==20:
                neighbors[single_row][single_column] = grid[single_row-1][single_column-1] +\
                                                       grid[single_row][single_column-1] +\
                                                       grid[single_row-1][single_column]
            # for edge cases
            elif single_row == 0 and 0 < single_column < 20:
                neighbors[single_row][single_column] = grid[single_row][single_column - 1] + grid[single_row][single_column + 1] + \
                                                       grid[single_row + 1][single_column] + grid[single_row + 1][single_column - 1] + grid[single_row + 1][single_column + 1]
            elif single_row == 20 and 0 < single_column < 20:
                neighbors[single_row][single_column] = grid[single_row][single_column - 1] + grid[single_row][single_column + 1] + \
                                                       grid[single_row - 1][single_column - 1] + grid[single_row - 1][single_column] + grid[single_row - 1][single_column + 1]
            elif single_column == 0 and 0 < single_row < 20:
                neighbors[single_row][single_column] = grid[single_row + 1][single_column] + grid[single_row - 1][single_column] + \
                                                       grid[single_row][single_column + 1] + grid[single_row - 1][single_column + 1] + grid[single_row + 1][single_column + 1]
            elif single_column == 20 and 0 < single_row < 20:
                neighbors[single_row][single_column] = grid[single_row + 1][single_column] + grid[single_row - 1][single_column] + \
                                                       grid[single_row][single_column - 1] + grid[single_row - 1][single_column - 1] + grid[single_row + 1][single_column - 1]
            # Checks and counts for neighbors in normal cases
            else:
                neighbors[single_row][single_column] = grid[single_row][single_column + 1] + grid[single_row][single_column - 1] + \
                                                       grid[single_row + 1][single_column] + grid[single_row - 1][single_column] + \
                                                       grid[single_row + 1][single_column + 1] + grid[single_row + 1][single_column - 1] + \
                                                       grid[single_row - 1][single_column + 1] + grid[single_row - 1][single_column - 1]
    return neighbors

def implementGame(grid):
    """ Implements the Game of Life rules:
    For a space that is 'populated':
        Each cell with one or no neighbors dies, as if by solitude.
        Each cell with four or more neighbors dies, as if by overpopulation.
        Each cell with two or three neighbors survives.
    For a space that is 'empty' or 'unpopulated'
        Each cell with three neighbors becomes populated. """
    
    rows = len(grid)
    columns = len(grid[0])
    neighbors = checkNeighbor(grid)
    for single_column in range(columns):
        for single_row in range(rows):
            if grid[single_row][single_column] == 1:
                if neighbors[single_row][single_column] >=4:
                    grid[single_row][single_column] = 0
                elif neighbors[single_row][single_column] <=1:
                    grid[single_row][single_column] = 0
            elif grid[single_row][single_column] == 0:
                if neighbors[single_row][single_column] == 3:
                    grid[single_row][single_column] = 1
    return grid

def main():
    
    # Declare and initialize a 21x21 grid filled with zeros
    grid = [[0 for column in range(21)] for row in range(21)]
    
    # Asks the user to input a grid file into the program
    print("Welcome! This is a simple Conway's Game of Life simulator.")
    txt_file = str(input("Please input a .txt file for the program to start, INCLUDING the file extension:"))
    print(" ")

    # Displays the initial grid state and runs the simulated execution each for 10 iterations
    with open(txt_file, 'r') as file:
        initialGrid(grid, file)
        print("This is the starting grid:")
        displayGrid(grid)
        print(" ")
        
        for i in range(10):
            implementGame(grid)
            print("Cycle:", i+1)
            displayGrid(grid)
            print(" ")



if __name__ == "__main__":
    main()
