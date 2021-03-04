

board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]



def print_board(board):

    for row in board:
        row_print = ""
        for value in row:
            row_print += str(value) + " "
        print(row_print)

def find_zero(board):
    row_count = 0
    col_count =  0  
    for row in board:
        for value in row:
            if value == 0:
                return[row_count, col_count]
            col_count += 1
        row_count += 1
    return None

#check's is the value in the grid, return false if it is, true if its not
def grid_call(row, col, value, max_row, max_col):
       
    if row <= max_row:
        if col <=max_col:
            row_counter = 0
            col_counter = 0
            while True:
                for row_counter in range(max_row):
                    for col_counter in range(max_col):
                        board_val = board[row_counter][col_counter]
                        if value == board_val:
                            print("Returning false")
                            return False
                        col_counter +=1
                    row_counter +=1    
                return True        


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


def solve(board):
    #base case 
    if find_zero(board) == None:
        print("Puzzle Solved!")
        return print_board(board) #print solved board 
    else:
        empty_space = find_zero(board)
        x = empty_space[0]
        y = empty_space[1]
        #recursive case 
        for value in range(1,9):
            if is_valid(board,x, y, value) == True:
                x = empty_space[0]
                y = empty_space[1]
                board[x][y] = value #assign the new value to the board 
                
                solve(board)
                print(print_board(board))
            else:
                # is_valid return's false, backtrack 
                board[x][y] = 0 #change value back to 0, value will increment next loop.
                print(print_board(board))
                #solve(board) #call the method again but with 
    return   

#print_board(board)
#print(find_zero(board))
#arugments board, row, col, value
#is_valid(board,0,2,4)

solution = solve(board)