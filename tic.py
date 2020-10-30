import random
play = "x"
computer = "o"

board = [1,2,3,4,5,6,7,8,9]

game_over = False
while game_over == False:
    player_play = input("please choose the location of your next play: ")
    player_play = int(player_play)
    computer_play = random.choice([x for x in board if x != "x" or x != "o"])

    while computer == 'x':
        computer_play = random.choice(board)

    for i in board:
        
        if i == player_play:
            turkey = board.index(player_play)
            if board[turkey] == "x" or board[turkey] == "o":
                player_play = input("please choose another location of your next play: ")
                player_play = int(player_play)
            
            board[turkey]= play

    for i in board:
        
        if i == computer_play:
            turkey = board.index(computer_play)
            board[turkey]= computer
    
           
    print(f""" 
        {board[0]} | {board[1]} | {board[2]}
        --+---+--
        {board[3]} | {board[4]} | {board[5]}
        --+---+--
        {board[6]} | {board[7]} | {board[8]}
    """)

    if "'x','x','x'" in board:
        game_over = True
    elif board == "'x',2,3,'x',5,6,'x',8,9":
        game_over = True
    elif board == "1,'x',3,4,'x',6,7,'x',9":
        game_over = True
    elif board == "1,2,'x',4,5,'x',7,8,'x'":
        game_over = True
    elif board == "'x',2,3,4,'x',6,7,8,'x'":
        game_over = True
    elif board == "1,2,'x',4,'x',6,'x',8,9":
        game_over = True
    if "'o','o','o'" in board:
        game_over = True
    elif board == "'o',2,3,'o',5,6,'o',8,9":
        game_over = True
    elif board == "1,'o',3,4,'o',6,7,'o',9":
        game_over = True
    elif board == "1,2,'o',4,5,'o',7,8,'o'":
        game_over = True
    elif board == "'o',2,3,4,'o',6,7,8,'o'":
        game_over = True
    elif board == "1,2,'o',4,'o',6,'o',8,9":
        game_over = True
    