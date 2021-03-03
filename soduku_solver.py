

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
    #check grid 
    counter = 0 
    if row <= 2:
        #first col 
        if col <=2:
            #first col, first row
            row_counter = 0
            col_counter = 0
            while True:
                for row_counter in range(3):
                    for col_counter in range(3):
                        board_val = board[row_counter][col_counter]
                        if value == board_val:
                            print("Returning false")
                            return False
                        col_counter +=1
                    row_counter +=1    
                return True      
            
                


    #     if col <= 5:
    #         #first col, second row
    #     else:
    #         #first col, third row
    # if row <= 5:
    #     #second grid
    #     if col <=2:
    #         #second col, first row
    #     if col <= 5:
    #         #second col, second row
    #     else:
    #         #second col, third row
    # else:
    #     #third grid
    #     if col <=2:
    #         #third col, first row
    #     if col <= 5:
    #         #third col, second row
    #     else:
    #         #third col, third row

def solve(board):

    return   

print_board(board)
print(find_zero(board))

is_valid(board,0,0,9)