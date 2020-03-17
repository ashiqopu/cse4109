#-- Shift: TicTacToe game
import time

class GAME:
    def __init__(self):
        self.board = [ '-' for i in range(0,9) ]
        self.lastmoves = []
        self.winner = None

    def print_board(self):
        print "\nCurrent board:"
        
        print "-------------"
        for j in range(0,9,3):
            print "|",
            for i in range(3):
                if self.board[j+i] == '-':
                    print "%d |" %(j+i),
                else:
                    print "%s |" %self.board[j+i],
            
            print "\n",
            print "-------------"
    
    def shift_board(self, winner):
        self.shiftLeft = False
        self.shiftRight = False
        self.shiftUp = False
        '''Print the shifted game board'''
        print ""
        print "----------- Shifting Board ------------"
        print "\nShifted board:"
        time.sleep(2)
        
        self.cnt = 0
        self.pos = ""
        
        self.tmp = 0
        if self.board[0]==winner: self.tmp += 1
        if self.board[3]==winner: self.tmp += 1
        if self.board[6]==winner: self.tmp += 1
        if self.tmp > self.cnt:
            self.pos = "left"
            self.cnt = self.tmp
        
        self.tmp = 0
        if self.board[2]==winner: self.tmp += 1
        if self.board[5]==winner: self.tmp += 1
        if self.board[8]==winner: self.tmp += 1
        if self.tmp > self.cnt:
            self.pos = "right"
            self.cnt = self.tmp
        
        self.tmp = 0
        if self.board[0]==winner: self.tmp += 1
        if self.board[1]==winner: self.tmp += 1
        if self.board[2]==winner: self.tmp += 1
        if self.tmp > self.cnt:
            self.pos = "up"
            self.cnt = self.tmp

        self.tmp = 0
        if self.board[6]==winner: self.tmp += 1
        if self.board[7]==winner: self.tmp += 1
        if self.board[8]==winner: self.tmp += 1
        if self.tmp > self.cnt:
            self.pos = "down"
            self.cnt = self.tmp
            
        if self.pos=="left": self.shiftLeft = True
        elif self.pos=="right": self.shiftRight = True
        elif self.pos=="up": self.shiftUp = True
        
        if self.shiftLeft:
            self.board[0] = self.board[2]
            self.board[3] = self.board[5]
            self.board[6] = self.board[8]
            self.board[1] = self.board[4] = self.board[7] = self.board[2] = self.board[5] = self.board[8] = '-'
        elif self.shiftRight:
            self.board[2] = self.board[0]
            self.board[5] = self.board[3]
            self.board[8] = self.board[6]
            self.board[1] = self.board[4] = self.board[7] = self.board[0] = self.board[3] = self.board[6] = '-'
        elif self.shiftUp:
            self.board[0] = self.board[6]
            self.board[1] = self.board[7]
            self.board[2] = self.board[8]
            self.board[3] = self.board[4] = self.board[5] = self.board[6] = self.board[7] = self.board[8] = '-'
        else: #self.shiftDown
            self.board[6] = self.board[0]
            self.board[7] = self.board[1]
            self.board[8] = self.board[2]
            self.board[0] = self.board[1] = self.board[2] = self.board[3] = self.board[4] = self.board[5] = '-'

        for j in range(0,9,3):
            for i in range(3):
                if self.board[j+i] == winner:
                    self.board[j+i] = '-'

    def get_free_positions(self):
        '''Get the list of available positions'''
        moves = []
        for i,v in enumerate(self.board):
            if v=='-':
                moves.append(i)
        return moves

    def mark(self,marker,pos):
        '''Mark a position with marker X or O'''
        self.board[pos] = marker
        self.lastmoves.append(pos)

    def revert_last_move(self):
        '''Reset the last move'''

        self.board[self.lastmoves.pop()] = '-'
        self.winner = None

    def is_roundover(self):
        '''Test whether round has ended'''
        win_positions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6),(1,4,7),(2,5,8), (0,4,8), (2,4,6)]

        for i,j,k in win_positions:
            if self.board[i] == self.board[j] == self.board[k] and self.board[i] != '-':
                self.winner = self.board[i]
                return True

        if '-' not in self.board:
            self.winner = '-'
            return True

        return False

    def play(self,player1,player2,OneWins,TwoWins):
        self.p1 = player1
        self.p2 = player2
        self.pOneWins = 0
        self.pTwoWins = 0
        self.gameCount = 1
        
        i = 0
        while i < 10:
            print "Game: ",self.gameCount,":: X won: ",self.pOneWins,":: O won: ",self.pTwoWins
            print ""
            #i = -1
            self.print_board()
            
            if i%2==0:
                if self.p1.type == 'H':
                    print "\t\t[Human's Move]"
                else:
                    print "\t\t[Computer's Move]"

                self.p1.move(self)
            else:
                if self.p2.type == 'H':
                    print "\t\t[Human's Move]"
                else:
                    print "\t\t[Computer's Move]"

                self.p2.move(self)

            if self.is_roundover():
                self.print_board()
                if self.winner == '-':
                    print "\nRound over with Draw"
                else:
                    print "\nRound Winner : %s" %self.winner
                    if self.winner == "O":
                        self.pTwoWins += 1
                    else:
                        self.pOneWins += 1
                
                if abs(self.pOneWins-self.pTwoWins)==2:
                    if self.pOneWins > self.pTwoWins:
                        print "\nGame Winner : X"
                    else:
                        print "\nGame Winner : O"
                    return
                else:
                    self.shift_board(self.winner)
                    #self.tmp = self.p1
                    #self.p1 = self.p2
                    #self.p2 = self.tmp
                self.gameCount += 1
                if i%2==0: i=0
                else: i = -1
            
            i += 1


class Human:
    '''Class for Human player'''
    def __init__(self,marker):
        self.marker = marker
        self.type = 'H'
    
    def move(self, gameinstance):

        while True:
        
            m = raw_input("Input position: ")

            try:
                m = int(m)
            except:
                m = -1
        
            if m not in gameinstance.get_free_positions():
                print "Invalid move. Retry"
            else:
                break
    
        gameinstance.mark(self.marker,m)


class AI:
    '''Class for Computer Player'''
    def __init__(self, marker):
        self.marker = marker
        self.type = 'C'

        if self.marker == 'X':
            self.opponentmarker = 'O'
        else:
            self.opponentmarker = 'X'

    def move(self,gameinstance):
        move_position,score = self.maximized_move(gameinstance)
        gameinstance.mark(self.marker,move_position)

    def maximized_move(self,gameinstance):
        ''' Find maximized move'''    
        bestscore = None
        bestmove = None

        for m in gameinstance.get_free_positions():
            gameinstance.mark(self.marker,m)
        
            if gameinstance.is_roundover():
                score = self.get_score(gameinstance)
            else:
                move_position,score = self.minimized_move(gameinstance)
        
            gameinstance.revert_last_move()
            
            if bestscore == None or score > bestscore:
                bestscore = score
                bestmove = m

        return bestmove, bestscore

    def minimized_move(self,gameinstance):
        ''' Find the minimized move'''

        bestscore = None
        bestmove = None

        for m in gameinstance.get_free_positions():
            gameinstance.mark(self.opponentmarker,m)
        
            if gameinstance.is_roundover():
                score = self.get_score(gameinstance)
            else:
                move_position,score = self.maximized_move(gameinstance)
        
            gameinstance.revert_last_move()
            
            if bestscore == None or score < bestscore:
                bestscore = score
                bestmove = m

        return bestmove, bestscore

    def get_score(self,gameinstance):
        if gameinstance.is_roundover():
            if gameinstance.winner  == self.marker:
                return 1 # Won
            elif gameinstance.winner == self.opponentmarker:
                return -1 # Opponent won
        return 0 # Draw
        

if __name__ == '__main__':
    game=GAME()
    p1 = raw_input("Enter Player 1 Type (h or m) : ")
    p2 = raw_input("Enter Player 2 Type (h or m) : ")
    if p1 == "h":
        player1 = Human("X")
    else:
        player1 = AI("X")
    if p2 == "m":
        player2 = AI("O")
    else:
        player2 = Human("O")
    
    game.play( player1, player2, 0, 0)
