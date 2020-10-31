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
        player2 = select(choices)
        return player2

class Game(Player):
    def __init__(self):
        # super().__init__ (self)
        player1 = self.player1()
        play = int(player1)
        for i in board:                    
            for j in i:                    
                j = (i.index(j))            
                if int(play) == i[j]:       
                    i[j] = "x"            
                    choices.remove(int(play))
                    # print(game)
        
                
        player2 = self.player2()
        for i in board:                    
            for j in i:                     
                j = (i.index(j))            
                if player2 == i[j]:
                    i[j] = "o" 
                    choices.remove(player2)
        game = f""" 
            {board[0][0]} | {board[0][1]} | {board[0][2]}
            --+---+--
            {board[1][0]} | {board[1][1]} | {board[1][2]}
            --+---+--
            {board[2][0]} | {board[2][1]} | {board[2][2]}
        """
        print(game)

Game()



