# Author: Michael Le
# Date: 11/18/2019
# Description:  TicTacToe class for game and 3x3 list board


class TicTacToe:

    def __init__(self):
        """
        board is initialized as a 3x3 list form
        current state is default for "Unfinished"
        current num is equivalent to count of turns, which is 0 starting
        """
        self._board = [["","",""],["","",""],["","",""]]
        self._current_state = "UNFINISHED"
        self._num=0

    def get_current_state(self):
        """
        :return: returns current state of game
        """
        return self._current_state

    def make_move(self, row, col, player):
        """
        :param row: row count for insert of symbol 0-2
        :param col: col count for insert of symbol 0-2
        :param player: the player making the move
        :return: true or false depending on if move is possible
        """
        if row >= 0 and row <= 2 and col >= 0 and col <= 2:
            if self._current_state == "UNFINISHED":
                if not self._board[row][col]:
                    self._board[row][col] = player
                    self._num = self._num + 1
                else:
                    return False
            if self._num > 4:
                if (self._board[row][0] == player and self._board[row][1] == player and self._board[row][2] == player):
                    self._current_state = str(player) + "WON"
                elif (self._board[0][col] == player and self._board[1][col] == player and self._board[2][col] == player):
                   self._current_state = str(player) + "WON"
                elif (self._board[0][0] == player and self._board[1][1] == player and self._board[2][2] == player):
                        self._current_state = str(player) + "WON"
                elif (self._board[0][2] == player and self._board[1][1] == player and self._board[2][0] == player):
                        self._current_state = str(player) + "WON"
            else:
                if (self._num==9 and self._current_state=="UNFINISHED"):
                    self._current_state = "DRAW"
                    return False
                else:
                    return True
        else:
            return False

    def print_Table(self):
        """
        :return: print out table with current location of where symbols are on board (x,o)
        """
        print("\nPresent Status of TicTacToe board is : \n")
        l = "Col-->[0, 1, 2]"
        count = 0
        print(l)
        for i in self._board:
            print(str(count) + "-->" + str(i))
            count = count + 1
        print()

