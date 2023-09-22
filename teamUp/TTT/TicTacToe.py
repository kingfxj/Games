#!/usr/bin/env python3

class TicTacToe:
    def __init__(self):
        # "board" is a list of 10 strings representing the board (ignore index 0)
        self.board = [" "]*10
        self.board[0] = "#"
        # self.board = ['#', 'x', 'x', 'o', 'x', 'x', 'o', 'o', 'o', 'x']

    def drawBoard(self):
        """
        Displays the current board next to a reference board with numbers.
        """
        for i in [7, 4, 1]:
            print('  ' + '   |   '.join(self.board[i:i+3]), end='  ')
            print(end='\t')
            j = [str(i), str(i+1), str(i+2)]
            print('  ' + '   |   '.join(j), end='  ')
            print()
            if i != 1:
                for i in range(2):
                    for i in range(11):
                        print(end='_ ')
                    print(end='\t')
                print()

    def assignMove(self, square, ch):
        """
        Assigns the player's character to the specified square of the board.
        
        Input: 
          square: reference number of square (int)
          ch: 'x' or 'o' (str)
        Returns: 
          True if move is valid; False otherwise
        """
        if type(square) == int and 1 <= square <= 9:
            if self.squareIsEmpty(square):
                self.board[square] = ch
                return True
            else:
                return False
        else:
            return False

    def squareIsEmpty(self, square):
        """
        Checks if an individual square contains a space character (i.e. is empty) or not.
        
        Input: 
          square: reference number of square to check (int)
        Returns: 
          True if square is valid and empty; False otherwise
        """
        if self.board[square] == ' ':
            return True
        else:
            return False

    def boardFull(self):
        """
        Checks if the board has any empty squares. 
        
        Returns: 
          True if no empty squares, False otherwise.
        """
        if ' ' in self.board:
            return False
        else:
            return True

    def whoWon(self):
        """
        Determines winner of the game.

        Returns:
          The symbol of the player who won if there is a winner;
          otherwise an empty string is returned.
        """
        if self.isWinner("x"):
            return "x"
        elif self.isWinner("o"):
            return "o"
        else:
            return ""

    def isWinner(self, ch):
        """
        Checks the rows, columns, and diagonals to determine whether the 
        specified player has won.
        
        Input: 
          ch: player 'x' or 'o' (str)
        Returns: 
          True if specified player has won; False otherwise
        """
        for i in [1, 4, 7]:
            if self.board[i] == self.board[i+1] == self.board[i+2] == ch:
                # print(i, i+1, i+2, ch)
                return True
        for i in [1, 2, 3]:
            if self.board[i] == self.board[i+3] == self.board[i+6] == ch:
                # print(i+1, i+3, i+6, ch)
                return True
        if self.board[1] == self.board[5] == self.board[9] == ch:
            # print(1, 5, 9, ch)
            return True
        if self.board[3] == self.board[5] == self.board[7] == ch:
            # print(3, 5, 7, ch)
            return True
        return False


# if __name__ == "__main__":
#     gameBoard = TicTacToe()
        
#     # Write code to fully test your methods here.
#     # Be sure to fully test your class before using in lab3_main.py (part 2 of this lab)!
#     gameBoard.drawBoard()
#     for i in range(1, 10):
#         print(i, gameBoard.board[i], gameBoard.squareIsEmpty(i))
#     print(gameBoard.assignMove(4, 'x'))
#     gameBoard.drawBoard()
#     print(gameBoard.assignMove(5, 'o'))
#     gameBoard.drawBoard()
#     print(gameBoard.boardFull())
#     print(gameBoard.whoWon())


# import lab3


def main():
    again = 'a'
    while again[0] != 'n':
        game = TicTacToe()
        print('Starting new Tic Tac Toe game')
        game.drawBoard()
        while game.whoWon() not in ['o', 'x'] and not game.boardFull():
            makeMove(game, 'x')
            if game.whoWon() in ['x', 'o'] or game.boardFull():
                break
            else:
                makeMove(game, 'o')
        if game.whoWon() in ['x', 'o']:
            print(game.whoWon(), 'wins. Congrats!')
        else:
            print("Board is full. Game ties")
        again = 'a'
        while again[0] not in 'yn':
            again = input('Do you want to play again? (no/yes) ')
    print("Thanks for playing! Goodbye.")


def makeMove(game, player):
    move = input('Player ' + player + ' please enter your move: ')
    while not game.assignMove(int(move), player):
        move = input('Invalid move. Player ' + player + ' please enter your move: ')
    game.drawBoard()


main()
