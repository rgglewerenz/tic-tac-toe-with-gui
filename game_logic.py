import random

#This is the board varriable that will be converted into a gui later
def resetboard():
    global board
    board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]
player1 = 1
player2 = 2
#Placing logic
def place(x,y,player):
    x_new = x - 1
    y_new = y - 1
    if board[x_new][y_new] == player:
        return "You are already here"
    elif board[x_new][y_new] != player and board[x_new][y_new] != 0:
        return "The opponant has already place an item here"
    elif board[x_new][y_new] == 0:
        board[x_new][y_new] = player
        return "You have done a succsess full move"
    else:
        return "Error, no coordinate pair found"
#Checking logic
def check(board_placement):
    score = 0
    for i in range(3):
        if board_placement[i][0] == board_placement[i][1] == board_placement[i][2] and  board_placement[i][2] != 0:
            return board_placement[i][0]
    for i in range(3):
        if board_placement[0][i] == board_placement[1][i] == board_placement[2][i] and  board_placement[0][i] != 0:
            return board_placement[1][i]
    if board_placement[0][0] == board_placement[1][1] == board_placement[2][2] or board_placement[0][2] == board_placement[1][1] == board_placement[2][0] and 0 != board_placement[2][2]:
        return board_placement[1][1]
    for i in board_placement:
        for b in i:
            if b != 0:
                score = score + 1
    if score == 9:
        return 3
    return 0
#AI moves
def ai(board_placement):
    #Horozontal Positions
    for i in range(3):
        if board_placement[i][0] == board_placement[i][1] and board_placement[i][0] != 0 and board_placement[i][1] != 0:
            if place(i+1,3,player2) == "You have done a succsess full move":
                return (i)*3 + 3
    for i in range(3):
        if board_placement[i][0] == board_placement[i][2] and board_placement[i][0] != 0 and board_placement[i][2] != 0:
            if (i+1,2,player2)  == "You have done a succsess full move":
                return (i)*3 + 2
    for i in range(3):
        if board_placement[i][2] == board_placement[i][1] and board_placement[i][1] != 0 and board_placement[i][2] != 0:
            if place(i+1,1,player2)  == "You have done a succsess full move":
                return (i)*3 + 1
    #Vertical Positions
    for i in range(3):
        if board_placement[1][i] == board_placement[0][i] and board_placement[0][i] != 0 and board_placement[1][i] != 0:
            if place(3,i+1,player2)  == "You have done a succsess full move":
                return (i+1) + 6
    for i in range(3):
        if board_placement[1][i] == board_placement[2][i] and board_placement[1][i] != 0 and board_placement[2][i] != 0:
            if place(2,i+1,player2) == "You have done a succsess full move":
                return (i+1) + 3
    for i in range(3):
        if board_placement[2][i] == board_placement[1][i] and board_placement[2][i] != 0 and board_placement[1][i] != 0: 
            if place(1,i+1,player2)  == "You have done a succsess full move":
                return (i+1)
    #Cross Board placement
    if board_placement[0][0] == board_placement[1][1] or board_placement[0][2] == board_placement[1][1] and 0 != board_placement[2][2]:
        if place(3,3,player2)  == "You have done a succsess full move":
            return 9
    elif board_placement[0][0] == board_placement[2][2] or board_placement[0][2] == board_placement[2][0] and 0 != board_placement[2][2]:
        if place(2,2,player2)  == "You have done a succsess full move":
            return 5
    elif board_placement[1][1] == board_placement[2][2] and 0 != board_placement[1][1]:
        if place(1,1,player2)  == "You have done a succsess full move":
            return 1
    elif board_placement[1][1] == board_placement[2][0] and 0 != board_placement[1][1]:
        if place(1,3,player2)  == "You have done a succsess full move":
            return 3
    elif board_placement[0][2] == board_placement[1][1] and 0 != board_placement[1][1]:
        if place(3,1,player2)  == "You have done a succsess full move":
            return 7
    
    #Random move if no other moves are made
    print("Random Time")
    x = 0
    y = 0
    while True:
        x = random.randint(1,3)
        y = random.randint(1,3)
        if check(board_placement) > 0:
            return 0
        if place(x,y,player2) == "You have done a succsess full move":
            return (x-1)*3 + y
def get_board():
    global board
    return board
#game loop
def game():
    while check(board) == 0:
        p1_move = []
        while True:
            try:
                p1_input = input("Please enter the coordinates for your desired location: ")
                p1_move = p1_input.split(",")
                if place(int(p1_move[0]),int(p1_move[1]),player1) == "You have done a succsess full move":
                    break
                else:
                    print(place(int(p1_move[0]),int(p1_move[1]),player1))
            except Exception:
                print("Please enter a valid number")
        ai(board)
        for i in board:
            print(i)
    if check(board) < 3:
        print(f"Player {check(board)} Won")
    else:
        print("Tie")
