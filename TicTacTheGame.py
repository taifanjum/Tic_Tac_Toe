
def printBoard(board):
    ''' print the board '''
    n = len(board)
    pattern1 = " ---" * n
    for i in range(n):
        print (pattern1)

        ## creating each line of board
        pattern2 = "| "
        for j in range(n):
            content = board[i][j]
            if content == 0:
                pattern2 += " "
            elif content == 1:
                pattern2 += "X"
            elif content == 2:
                pattern2 += "O"

            ##Sanity check: anything except 0, 1 or 2 is invalid! (although it is not possible in this code!)
            else:
                print 
                print "Error!! Exit the game"
                exit()

            pattern2 += " | "

        print pattern2

    print pattern1

def isBoardFull(board):
    '''returns True if the board is already full'''

    for row in board:
        if 0 in row:
            return False

    return True

def takePlayerChoice(board, playerID):
    ''' This function takes the playerID and board
    asks the user to enter the info of column and row
    to put the mark and update the board based on that.
    If the correspinding cell is empty and it is a valid cell
    in this board (correct indexes), it updates the board
    and return True. Otherwise it returns False (invalid row
    or column or trying to insert in already occupied cell)
    '''

    row = int(raw_input("Which row? "))
    col = int(raw_input("Which column? "))
    if row > 3 or row < 1:
        print "out of board"
        return False
    if col > 3 or col < 1:
        print "out of board"
        return False

    row -= 1
    col -= 1
    if board[row][col] != 0:
        print "cell is already full"
        return False
    board[row][col] = playerID
    return True

def column(board, i):
    return [row[i] for row in board]

def verifyWinner(board):
    # check row
    for row in board:
        if len(set(row)) == 1 and row[0] != 0:
            return row[0]
    
    # check column
    for i in range(len(board)):
        col = column(board, i)
        if len(set(col)) == 1 and col[0] != 0:
            return col[0]
    
    # check diagonal
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (board[2][0] == board[1][1] and board[1][1] == board[0][2]):
        return board[1][1]
    
    return 0

def createEmptyBoard(n):
    '''Create an empty board of size nxn '''
    
    board = []
    for i in range(n):
        tmp = []
        for i in range(n):
            tmp.append(0)
        board.append(tmp)
      
    return board

## Game starts here:
mainBoard = createEmptyBoard(3)

player = 0
while not isBoardFull(mainBoard):
    printBoard(mainBoard)
    print "Player%d: " %(player+1)
    while not takePlayerChoice(mainBoard, player+1):
        print "Player%d: Try again!" %(player+1)
        continue

    player = (player+1)%2 #the value of player alternates (0 or 1)

    printBoard(mainBoard)
    winner = verifyWinner(mainBoard)
    if winner != 0:
        print "Congratulation player" + str(winner) + ". You won!"
        break
        
print "Game over!!"
