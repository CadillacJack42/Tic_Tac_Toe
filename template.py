from random import choice as select
board = [[1,2,3],[4,5,6],[7,8,9]]
choices = [1,2,3,4,5,6,7,8,9]

game_on = "x"
while game_on:
    play = input("Enter a number between 1 and 9 : ")

    if int(play) not in choices:
        play = input(f'''
That number has already been played. 
Available numbers are ; {choices}
Enter a number fom the available choices : ''')

    for i in board:                     
        for j in i:                     
            j = (i.index(j))            
            if int(play) == i[j]:       
                i[j] = "x"              
                choices.remove(int(play))

    comp = select(choices)
    
    for i in board:                     
        for j in i:                     
            j = (i.index(j))            
            if comp == i[j]:
                i[j] = "o" 
                choices.remove(comp)

    game = f""" 
            {board[0][0]} | {board[0][1]} | {board[0][2]}
            --+---+--
            {board[1][0]} | {board[1][1]} | {board[1][2]}
            --+---+--
            {board[2][0]} | {board[2][1]} | {board[2][2]}
        """
    print(game)

    for i in board:
        if i == ["x","x","x"]:
            game_on = ''
            print("You Win")
    if board[0][0] == board[1][0] == board[2][0] == "x":
        game_on = ''
        print("you Win")
    elif board[0][1] == board[1][1] == board[2][1] == "x":
        game_on = ''
        print("you Win")
    elif board[0][2] == board[1][2] == board[2][2] == "x":
        game_on = ''
        print("you Win")
    elif board[0][0] == board[1][1] == board[2][2] == "x":
        game_on = ''
        print("you Win")
    elif board[0][2] == board[1][1] == board[2][0] == "x":
        game_on = ''
        print("you Win")

    for i in board:
        if i == ["o","o","o"]:
            game_on = ''
            print("You Lose")
    if board[0][0] == board[1][0] == board[2][0] == "o":
        game_on = ''
        print("you Lose")
    elif board[0][1] == board[1][1] == board[2][1] == "o":
        game_on = ''
        print("you Lose")
    elif board[0][2] == board[1][2] == board[2][2] == "o":
        game_on = ''
        print("you Lose")
    elif board[0][0] == board[1][1] == board[2][2] == "o":
        game_on = ''
        print("you Lose")
    elif board[0][2] == board[1][1] == board[2][0] == "o":
        game_on = ''
        print("you Lose")
    
