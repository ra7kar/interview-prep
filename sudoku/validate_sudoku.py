# validate sudoku
# input is a board
# Return True if board is correct
# Return False if board is incorrect


def validate(board):

    board_len = len(board)

    # # check row numbers for duplicates
    seen = {}
    dups = []
    for row in range(board_len):
        #print( bo[i])
        for col in board[row]:
            
            if col not in seen:
                seen[col] = 1
            else:
                dups.append(col)
            
        seen={}
        if len(dups) > 0:
            return False
    
    # check columns for duplicates
    seen = {}
    dups = []
    for col in range(board_len):
        for row in board:
            print(row[col])
            if row[col] not in seen:
                seen[row[col]] = 1
            else:
                dups.append(row[col])
        seen = {}
        if len(dups) > 0:
            return False
        print("--------")
    

    # check the box for duplicates
    for row in range(len(board)):
        first_box = {}
        second_box = {}
        third_box = {}
        if row % 3 == 0 and row !=0:
            print("-"*30)
        for col in range(len(board[0])):
            val = board[row][col]
            square = col // 3

            if square == 0 :
                if val in first_box:
                    print("Duplcate in one")
                    return False
                else:
                    first_box[val]=1

            if square == 1 :
                if val in second_box:
                    print("Duplcate in second")
                    return False
                else:
                    second_box[val]=1

            if square == 2 :
                if val in third_box:
                    print("Duplcate in third")
                    return False
                else:
                    third_box[val]=1

            if col % 3 == 0 and col != 0:
                print("| ", end="") 
                     
            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end=" ")
            


    return True
        
def print_board(board):
    board_len = len(board)

    for row in range(board_len):
        
        if row % 3 == 0 and row != 0:
            print( "-"*32) 
        
        # for col in range(len(board[0])):
            
        #     if col%3 == 0 and col != 0:
        #         print((board[row][col]))
        #     else:
        #         print(board[row][col], end=" ")


board = [[  7,  8,  5, 4,  3,  9, 1,  2,  6],
         [  6,  1,  2, 8,  7,  5, 3,  4,  9],
         [  4,  9,  3, 6,  2,  1, 5,  7,  8],
         [  8,  5,  7, 9,  4,  3, 2,  6,  1],
         [  2,  6,  1, 7,  5,  8, 9,  3,  4],
         [  9,  3,  4, 1,  6,  2, 7,  8,  5],
         [  5,  7,  8, 3,  9,  4, 6,  1,  2],
         [  1,  2,  6, 5,  8,  7, 4,  9,  3],
         [  3,  4,  9, 2,  1,  6, 8,  5,  7]]


result = validate(board)
print(result)
#print_board(board)



