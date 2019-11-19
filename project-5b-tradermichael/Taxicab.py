# Author: Michael Le
# Date: 10/27/2019
# Description: Taxicab class that has methods to get coordinates for a taxicab, move the taxicab, and also get how much taxicab has traveled
class Taxicab:
    def __init__(self, corX = 0, corY = 0):
        """

        :type self: object that has coordinate X and Y as parameters
        """
        # setting total distance traveled to 0
        self._odometer = 0

        self._corX = corX
        # setting Y coordinate to user given value
        self._corY = corY

    # move the cab in X direction, negative input --> move left, positive input --> move right
    def move_x(self, move):
        self._corX = self._corX + move
        if move < 0:
            self._odometer -= (move)
        else:
            self._odometer += (move)
        return self._corX


    # move the cab in Y direction, negative input --> move down, positive input --> move up
    def move_y(self, move):
        self._corY = self._corY + move
        if move < 0:
            self._odometer -= (move)
        else:
            self._odometer += (move)
        return self._corY

    def get_odometer(self):
        return self._odometer

        # getter for coordinate X

    def get_x_coord(self):
        return self._corX

        # getter for coordinate Y

    def get_y_coord(self):
        return self._corY

