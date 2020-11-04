from random import choice

board = [[1,2,3],[4,5,6],[7,8,9]]
choices = [1,2,3,4,5,6,7,8,9]



initiate = input("Would you like to play Tic Tac Toe ? y/n : ")

# player2 = input("What is player 2's name? : ")

instructions = '''
You will prompted to enter a number, 1 through 9.
Each number corresponds to a tile on the game board.
Player 1 will place an "X" on the board.
Player 2 will place an "O" on the board.
The first player to get 3 markers in a row is the Winner.
Good Luck!'''

class Players():
    def __init__(self):
        pass
    
    def Player(self, move):
        self.move = int(move)
        if self.move not in choices:
            move = input(f'''
    That number has already been played. 
    Available numbers are ; {choices}
    Enter a number fom the available choices : ''')
            return int(move)
        elif choices == []:
            move = "The game board is full. Match is a draw"
            return move
        else:
            pass
            return self.move

    def Computer(self):
        if choices != []:
            computer = choice(choices)
            return computer
        elif choices == []:
            stalemate = "The game board is full. Match is a draw"
            return stalemate

class Game():
    def __init__(self, move):
        self.move = move

    def play(self):
        for i in board:                    
            for j in i:                    
                j = (i.index(j))            
                if self.move == i[j]:       
                    i[j] = "X"          
                    choices.remove(self.move)
                    

    def comp(self):
        for i in board:                    
            for j in i:                    
                j = (i.index(j))            
                if self.move == i[j]:       
                    i[j] = "O"          
                    choices.remove(self.move)
                    

    def win_loss(self):
        game_on = 0
        for i in board:
            if i == ["X","X","X"]:
                game_on = 1
            elif board[0][0]  == board[1][0]  == board[2][0] == "X":
                game_on = 2
            elif board[0][1]  == board[1][1]  == board[2][1] == "X":
                game_on = 3
            elif board[0][2]  == board[1][2]  == board[2][2] == "X":
                game_on = 4
            elif board[0][0]  == board[1][1]  == board[2][2] == "X":
                game_on = 5
            elif board[0][2]  == board[1][1]  == board[2][0] == "X":
                game_on = 6    
            
        # for i in board:
            elif i == ["O","O","O"]:
                game_on = 7
            elif board[0][0]  == board[1][0]  == board[2][0] == "O":
                game_on = 8
            elif board[0][1]  == board[1][1]  == board[2][1] == "O":
                game_on = 9
            elif board[0][2]  == board[1][2]  == board[2][2] == "O":
                game_on = 11
            elif board[0][0]  == board[1][1]  == board[2][2] == "O":
                game_on = 12
            elif board[0][2]  == board[1][1]  == board[2][0] == "O":
                game_on = 13
            elif choices == []:
                game_on = 14
            else:
                pass  
            if game_on in range(1,7):
                print("Player1 has Won!")
            elif game_on in range(7,15):
                print("Player2 has Won!")   
            return game_on

def main():
    if initiate == "y":
        mode = input("Would you like to play 1 or 2 player mode? : ")
    if int(mode) == 1:
        player1 = input("What is Player 1's name? : ")
        while Game(0).win_loss() == 0:
            play1_move = input('''
    Enter a number btween 1 and 9 to place your marker''')
            move = Players().Player(play1_move)
            Game(move).play()
            Game(move).win_loss()
            computer = Players().Computer()
            Game(computer).comp()
            Game(move).win_loss()
            game_board = f''' 
            {board[0][0]} | {board[0][1]} | {board[0][2]}
            --+---+--
            {board[1][0]} | {board[1][1]} | {board[1][2]}
            --+---+--
            {board[2][0]} | {board[2][1]} | {board[2][2]}
'''
            print(game_board)

    elif int(mode) == 2:
        player1 = input("What is Player 1's name? : ")
        player2 = input("What is player 2's name? : ")
        while Game(0).win_loss() == 0:
            play1_move = input(f'''
    {player1} enter a number between 1 and 9 to place your marker : ''')
            move1 = Players().Player(play1_move)
            Game(move1).play()
            Game(move1).win_loss()
            play2_move = input(f'''
    {player2} enter a number between 1 and 9 to place your marker : ''')
            move2 = Players().Player(play2_move)
            Game(move2).comp()
            Game(move2).win_loss()
            game_board = f''' 
            {board[0][0]} | {board[0][1]} | {board[0][2]}
            --+---+--
            {board[1][0]} | {board[1][1]} | {board[1][2]}
            --+---+--
            {board[2][0]} | {board[2][1]} | {board[2][2]}
'''
            print(game_board)

        

main()

