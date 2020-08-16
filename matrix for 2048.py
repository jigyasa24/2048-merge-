#board = [[0, 0, 2, 2], [2, 2, 2 , 0], [4, 0, 0, 4], [0, 2, 0, 0]]      """temporary board"""
"""to create a matrix with at least 2 random values"""
import random                         
import copy

boardsize = 5
print("Welcome to 2048! Your goal is to combine similar values by moving the board in different directions. You can use the 'w' key to go up, 'a' key to go left, 's' key to go down and 'd' to go right. ")
display()

"""picks a new value for the board"""
def picknewvalue():                    
    if random.randint(1,8) == 1:
        return 4
    else:
        return 2
    
def addnewvalue():
    rownum = random.randint(0, boardsize - 1)
    colnum = random.randint(0, boardsize - 1) 
    
    while not board[rownum][colnum] == 0:
        rownum = random.randint(0, boardsize - 1)
        colnum = random.randint(0, boardsize - 1)
        
    board[rownum][colnum] = picknewvalue()
    
"""create a blanck board"""
board = []                              
for i in range(boardsize):
    row = []
    for j in range(boardsize):
        row.append(0)
    board.append(row)
    
numneeded = 2
while numneeded > 0:
    rownum = random.randint(0, boardsize - 1)
    colnum = random.randint(0, boardsize - 1)
    
    if board[rownum][colnum] == 0:
        board[rownum][colnum] = picknewvalue()
        numneeded -= 1
        
def display():
    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element
                
                
    numspaces = len(str(largest))
                
    for row in board:
        currRow = "|"
        for element in row:
            if element == 0:
                currRow += " " * numspaces + "|"
            else:
                currRow += (" " * (numspaces - len(str(element)))) + str(element) + "|"
        print(currRow)
    print()
    
display()

"""move evrything as far left as possible"""
def mergeonerowl(row):                        
    for j in range(boardsize - 1):
        for i in range(boardsize - 1, 0, -1):
          if row [i - 1] == 0:
            row [i - 1] = row[i]
            row[i] = 0
            
    for i in range(boardsize - 1):           
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1]=0
            
    for i in range(boardsize - 1, 0, -1):
        if row[i - 1]== 0:
            row[i - 1] = row[i]
            row[i]   = 0
    return row

"""merge the whole board to the left"""
def merge_left(currentboard):                
    for i in range(boardsize):
        currentboard[i] = mergeonerowl(currentboard[i])
    
    return currentboard

def reverse(row):
    new = []
    for i in range(boardsize - 1, -1, -1):
        new.append(row[i])
    return new

def merge_right(currentboard):
    for i in range(boardsize):
        currentboard[i] = reverse(currentboard[i])
        currentboard[i] = mergeonerowl(currentboard[i])
        currentboard[i] = reverse(currentboard[i])
    return currentboard

def transpose(currentboard):
    for j in range(boardsize):
        for i in range(j, boardsize):
            if not i == j:
                temp = currentboard[j][i]
                currentboard[j][i] = currentboard[i][j]
                currentboard[i][j] = temp
    return currentboard

def merge_up(currentboard):
    currentboard = transpose(currentboard)
    currentboard = merge_left(currentboard)
    currentboard = transpose(currentboard)
    
    return currentboard

def merge_down(currentboard):
    currentboard = transpose(currentboard)
    currentboard = merge_right(currentboard)
    currentboard = transpose(currentboard)
    
    return currentboard

#merge_down(board)
#display()

#merge_up(board)
#display()
#
#merge_right(board)
#display()
#        
#merge_left(board)
#display()

gameover = False

while not gameover:
    move = input("which way do you want to merge? ")
    
    validinput = True
    
    tempboard = copy.deepcopy(board)
    
    if move == "d":
        board = merge_right(board)
    elif move == "w":
        board = merge_up(board)
    elif move == "a":
        board = merge_left(board)
    elif move == "s":
        board = merge_down(board)
    else:
        validinput = False
        
    if not validinput:
        print("try again")
    else:
        if board == tempboard:
            print("try a diff direction")
        else:
            addnewvalue()
            display()
        
    
         
     