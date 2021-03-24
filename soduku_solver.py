board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

solution = [[]]

def print_board(board):

    for row in board:
        row_print = ""
        for value in row:
            row_print += str(value) + " "
        print(row_print)
""" 
def find_zero(board):  
    for row in board:
        for value in row:
            if value == 0:
                return[row, value]
    return None """
def find_zero(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return [i, j]
    return None


#check's is the value in the grid, return false if it is, true if its not
""" def grid_call(row, col, value, max_row, max_col):
       
    if row <= max_row:
        if col <=max_col:
            
            
            while True:
                for row in range(row, max_row):
                    col = max_col - 3
                    for col in range(col, max_col):
                        board_val = board[row][col]
                        if value == board_val:
                            print("Returning false")
                            return False
                        col +=1
                    row +=1 
                row =  max_row -3   
                return True       """  

def is_valid(board, row, col, value):
    board_row =  board[row]
    #Row check 
    if value in board_row:
        print("Returning False")
        return False
    #col check 
    i = 0
    while i < len(board):
        col_value = board[i][col] 
        
        if col_value == value:
            print("Returning False")
            return False
        i +=1
#this part works out which 3X3 part of the sodku board where in. So it knows where to check, then it calls the grid_call method with the right paramaters. 
    if row < 3:
        #first col 
        if col <3:
            #first row, first col
            if grid_call(row,col, value, 3,3) == True:
               return True
           #first row second col
        if col < 6 and col > 2:
            if grid_call(row, col, value,3,6) == True:
                return True
            #first row, third col
        if col < 9 and col > 5:
            if grid_call(row, col, value,3,9) == True:
                return True
    #second row 
    if row < 6 and row > 2:
        #second row, first col
        if col <3:
            if grid_call(row,col, value, 6,3) == True:
                return True
        #second row, second row 
        if col <6 and col > 2:
            if grid_call(row,col, value, 6,6) == True:
                return True
        #second row, third row 
        if col <9 and col > 5:
            if grid_call(row,col, value, 6,9) == True:
                return True
    #third row 
    if row < 9 and row > 5:
        #third row, first col
        if col < 3:       
            if grid_call(row,col, value, 9,3) == True:
                return True
        #third row, second col
        if col < 6 and col > 2:       
            if grid_call(row,col, value, 9,6) == True:
                return True
        #third row, third col
        if col < 9 and col > 5:       
            if grid_call(row,col, value, 9,9) == True:
                return True
    return False 


def is_valid(board, row, col, value):
  # check if the input value already exited in row
  if value in board[row]:
    return False
  # if not, check if the input value already exited in column
  for r in range(len(board)):
    if value == board[r][col]:
      return False
  # if not, check if the input value already exites in 3x3 grid
  for r in range(0,len(board),3):
    for c in range(0, len(board),3):
      grid = []
      for r_ in range(0,3):
        grid += board[r:r+3][r_][c:c+3]
      if row in range(r,r+3) and col in range(c,c+3):
        if value in grid:
          return False
 
  return True


def solve(board, value_avoid=None):
    #base case 
    if find_zero(board) == None:
        print("Puzzle Solved!")
        print_board(board) #print solved board 
        return True
    else:
        #calls find_zero function which looks for a 0 on the board.
        empty_space = find_zero(board)
        #x, y = empty_space
        x = empty_space[0]
        y = empty_space[1]
        print("PRINTING BOARD BEFORE TRYING TO HIT VALUES")
        #recursive case Trys to fill in a value starting at 1, calls the is_valid 
        for value in range(1,10):
            if is_valid(board,x, y, value) == True:
                board[x][y] = value #assign the new value to the board 
                sol = solve(board)                                                                         
                if sol:
                    return True 
                else:
                    board[x][y] = 0
            else:
                continue
    return print("No Solution")

solution = solve(board)
print(solution)

