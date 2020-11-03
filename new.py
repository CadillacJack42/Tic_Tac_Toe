from random import choice

class Player:
    def __init__(self):
        pass
        
    def player_moves(self):
        player_move = input("Select a position to mark : ")

        if choices == []:
            initiate = input("Looks like a stalemate. Would you like to play again?")
        elif int(player_move) not in choices:
            print(f"That position has been played already. The available moves are {choices}.")
            player_move = input("Please make another selection : ")
        return int(player_move)

    def computer_moves(self):        
        if choices != []:
            computer_move = choice(choices)
            print(computer_move)
            return computer_move
        else:
            initiate = input("Looks like a stalemate. Would you like to play again?")
            return initiate
    

class Game(Player):
    def __init__(self):
        pass

    def player_choice(self):
        
        self.player_move = Player().player_moves()
        for i in board:                    
            for j in i:                    
                j = (i.index(j))            
                if self.player_move == i[j]:       
                    i[j] = "X"            
                    choices.remove(self.player_move)
                    print(choices)

    def computer_choice(self):
            
        self.computer_move = Player().computer_moves()
        for i in board:                    
            for j in i:                     
                j = (i.index(j))            
                if self.computer_move == i[j]:
                    i[j] = "O" 
                    choices.remove(self.computer_move)
        if self.computer_move == "y":
            board = [[1,2,3],[4,5,6],[7,8,9]]
            choices = [1,2,3,4,5,6,7,8,9]
            

        print(choices)
        

def main():
    initiate = input("Would you like to play Tic Tac Toe? : ")

    while initiate == "y":
        Game().player_choice()
        Game().computer_choice()
        game_board = f""" 
            {board[0][0]} | {board[0][1]} | {board[0][2]}
            --+---+--
            {board[1][0]} | {board[1][1]} | {board[1][2]}
            --+---+--
            {board[2][0]} | {board[2][1]} | {board[2][2]}
        """
        print(game_board)

board = [[1,2,3],[4,5,6],[7,8,9]]
choices = [1,2,3,4,5,6,7,8,9]

main()