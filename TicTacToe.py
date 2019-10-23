class TicTacToe:

    def __init__(self):

        self._triple_list = [[[0, 0], [0, 1], [0, 2]],
                             [[1, 0], [1, 1], [1, 2]],
                             [[2, 0], [2, 1], [2, 2]],
                             [[0, 0], [1, 0], [2, 0]],
                             [[0, 1], [1, 1], [2, 1]],
                             [[0, 2], [1, 2], [2, 2]],
                             [[0, 0], [1, 1], [2, 2]],
                             [[2, 0], [1, 1], [0, 2]]]

        self._board = [[" ", " ", " "],
                       [" ", " ", " "],
                       [" ", " ", " "]]

        self._win = False
        self._player1_name = ""
        self._player2_name = ""

    def run(self):

        self._player1_name = input("Player 1 Name: ")
        self._player2_name = input("Player 2 Name: ")

        while not self._win:
            self.display_board()

            p1_input_row = int(input("Player 1 - ROW: "))
            p1_input_column = int(input("Player 1 - COLUMN: "))

            while self.is_invalid(p1_input_row, p1_input_column):
                print("Invalid input. Please choose another.")
                p1_input_row = int(input("Player 1 - ROW: "))
                p1_input_column = int(input("Player 1 - COLUMN: "))

            self.set_value(p1_input_row, p1_input_column, "X")

            self.display_board()

            if self.check_win("X"):
                self._win = True
                print("\nPlayer 1 wins")

            if not self._win:

                p2_input_row = int(input("Player 2 - ROW: "))
                p2_input_column = int(input("Player 2 - COLUMN: "))

                while self.is_invalid(p2_input_row, p2_input_column):
                    print("Invalid input. Please choose another.")
                    p2_input_row = int(input("Player 2 - ROW: "))
                    p2_input_column = int(input("Player 2 - COLUMN: "))

                self.set_value(p2_input_row, p2_input_column, "O")

                if self.check_win("O"):
                    self._win = True
                    print("\nPlayer 2 wins")

    def display_board(self):

        print()

        for row in range(0, len(self._board)):
            print("|", end="")
            for column in range(0, len(self._board[row])):
                print(self._board[row][column] + "|", end="")
            print()

        print()

    def is_invalid(self, row, column):
        # This method determines if the input from the user is valid

        invalid_input = False

        # Determine if the row and column values are out of the range of values for the board
        if (row > len(self._board)) or (row < 1) or (column > len(self._board[0])) or (column < 1):
            invalid_input = True

        # Determine if there is already a mark in the current square space
        elif (self._board[row-1][column-1] == "X") or (self._board[row-1][column-1] == "O"):
            invalid_input = True

        return invalid_input

    def set_value(self, row, column, value):
        # This method sets the mark value in the appropriate place in the board list object

        # Set the appropriate value in the list object (subtract 1 for element index)
        self._board[row-1][column-1] = value

    def check_win(self, value):

        win = False

        for a in range(0, len(self._triple_list)):

            if ((self._board[self._triple_list[a][0][0]][self._triple_list[a][0][1]] == value) and
                    (self._board[self._triple_list[a][1][0]][self._triple_list[a][1][1]] == value) and
                    (self._board[self._triple_list[a][2][0]][self._triple_list[a][2][1]] == value)):

                win = True

        return win









