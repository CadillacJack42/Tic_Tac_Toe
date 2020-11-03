from random import choice as select
board = [[1,2,3],[4,5,6],[7,8,9]]
choices = [1,2,3,4,5,6,7,8,9]

class Player:
    def __init__(self):
        pass

    def player1(self):
        player1 = input("Enter a number between 1 and 9 : ")

        if int(player1) not in choices:
            player1 = input(f'''
    That number has already been played. 
    Available numbers are ; {choices}
    Enter a number fom the available choices : ''')
        return player1

    def player2(self):
        if choices != []:
            player2 = select(choices)
            return player2
        elif choices == []:
            return "Stalemate"
        

class Game(Player):
    def __init__(self, game_on):
        self.game_on = game_on
        player1 = self.player1()
        play = int(player1)
        for i in board:                    
            for j in i:                    
                j = (i.index(j))            
                if int(play) == i[j]:       
                    i[j] = "x"            
                    choices.remove(int(play))
        self.game_on = self.Win_loss()
        
                                   
        player2 = self.player2()
        for i in board:                    
            for j in i:                     
                j = (i.index(j))            
                if player2 == i[j]:
                    i[j] = "o" 
                    choices.remove(player2)
        self.game_on = self.Win_loss()

        game = f""" 
            {board[0][0]} | {board[0][1]} | {board[0][2]}
            --+---+--
            {board[1][0]} | {board[1][1]} | {board[1][2]}
            --+---+--
            {board[2][0]} | {board[2][1]} | {board[2][2]}
        """
        print(game)
    def Win_loss(self):
        for i in board:
            if i == ["x","x","x"]:
                self.game_on = 1
            elif board[0][0] == "x" and board[1][0] == "x" and board[2][0] == "x":
                self.game_on = 2
            elif board[0][1] == "x" and board[1][1] == "x" and board[2][1] == "x":
                self.game_on = 3
            elif board[0][2] == "x" and board[1][2] == "x" and board[2][2] == "x":
                self.game_on = 4
            elif board[0][0] == "x" and board[1][1] == "x" and board[2][2] == "x":
                self.game_on = 5
            elif board[0][2] == "x" and board[1][1] == "x" and board[2][0] == "x":
                self.game_on = 6
    
            elif i == ["o","o","o"]:
                self.game_on = 7

            elif board[0][0] == "o" and board[1][0] == "o" and board[2][0] == "o":
                self.game_on = 8

            elif board[0][1] == "o" and board[1][1] == "o" and board[2][1] == "o":
                self.game_on = 9

            elif board[0][2] == "o" and board[1][2] == "o" and board[2][2] == "o":
                self.game_on = 11

            elif board[0][0] == "o" and board[1][1] == "o" and board[2][2] == "o":
                self.game_on = 12

            elif board[0][2] == "o" and board[1][1] == "o" and board[2][0] == "o":
                self.game_on = 13

            elif choices == []:
                self.game_on = 14
                
        return self.game_on


class Tic():
    def __init__(self):
        game_on = 0
        while game_on == 0:
            Games = Game(game_on)
            game_on = Games.Win_loss()
            print(game_on)
            if game_on in range(1,7):
                print("You've Won")
            elif game_on in range(7,14):
                print("You've Lost")
            elif game_on == 14:
                print("Looks like there are no more available moves")
            if game_on != 0:
                break
            
            Game(game_on)
        
Tic()