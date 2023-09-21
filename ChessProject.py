a = 0
b = 1
c = 2
d = 3
e = 4
f = 5
g = 6
h = 7

CHESS_DICTIONARY = {
    #index of columns
    'a' : 0,
    'b' : 1,
    'c' : 2,
    'd' : 3,
    'e' : 4,
    'f' : 5,
    'g' : 6,
    'h' : 7,
    #index of rows
    '1' : 0,
    '2' : 1,
    '3' : 2,
    '4' : 3,
    '5' : 4,
    '6' : 5,
    '7' : 6,
    '8' : 7
}

def string_to_integers(string): #converts "a1" to a pair of integers (0,0) for example king
    """Method to grab the first letter of a string and converts it to an index value and
        does the same for the second number since players will be entering their moves
        like a1 or e7, etc."""

    first_letter = string[0]  # converts any string to indexes(integers)
    second_letter = string[1]

    column_letter = CHESS_DICTIONARY[first_letter]  # convert first letter 'c' to a number
    row_letter = CHESS_DICTIONARY[second_letter]

    return [column_letter, row_letter] # tuple

class ChessPieces:
    """Represents a chess piece to play on a chess board with attributes such as location
        and color of a piece."""
    def __init__(self, location, color):
        """Creates a ChessPieces object with location and color."""
        self._location = location
        self._color = color

    def get_location(self):
        """Returns the location of a chess piece."""
        return self._location

    def set_location(self, new_location):
        """Updates the location of a chess piece."""
        self._location = new_location

    def get_color(self):
        """Returns the color of a chess piece."""
        return self._color

    def is_valid_move(self, move_to_column, move_to_row):
        """Each child chess piece class have an is_valid_move method to check for illegal moves."""
        pass

    def is_king_in_check(self, king, board):
        """Each child chess piece class has an is_king_in_check method to check if a piece is
        checking the opponent's king."""
        pass

class King(ChessPieces):
    """Represents a king piece from chess using attributes from the parent class ChessPieces."""
    def __init__(self, location, color):
        """Creates a King object under parent ChessPieces object with a location and color attribute."""
        super().__init__(location, color)

    def __str__(self):  # method with __ is special
        """Creates a method using str to return an object in string format. In this case it is a K
        to represent the King and is displayed to the two people playing this Chess game."""
        return "K"      # will return K

    def is_valid_move(self, move_to_column, move_to_row):   #parameters are the goal index number
        """This method checks if the King piece itself can move the steps in rows and columns
        legally as desired by the user."""
        # if king piece moves more than 2 squares from current position then move is illegal
        integer_position = string_to_integers(self.get_location()) # current location is now a tuple ex. (0,0)

        column_steps = move_to_column - integer_position[0]
        row_steps = move_to_row - integer_position[1]

        #print("Columns steps", column_steps)
        #print("Row steps", row_steps)

        # if king piece is off the board from current position, illegal.
        if move_to_row < 0 or move_to_column < 0:
            #print("king is off the board")
            return False
        elif abs(row_steps) >= 2 or abs(column_steps) >= 2:
            #print("kings movement is more than 1 step")
            return False
        else:
            return True

    def is_king_in_check(self, king, board):
        """This method checks if the opponent's king (in the parameter) is being checked
        by an opponent's piece. The board parameter is the board itself."""
        own_location = string_to_integers(self.get_location())
        column_steps = string_to_integers(king.get_location())[0] - own_location[0]
        row_steps = string_to_integers(king.get_location())[1] - own_location[1]

        if abs(column_steps) == 1 and abs(row_steps) == 1:
            return True    # meaning king is not in check! answer your own method question like is_king_in_check
        else:
            return False

class Rook(ChessPieces):
    """Represents a Rook piece from chess using attributes from the parent class ChessPieces."""
    def __init__(self, location, color):
        """Creates a Rook object under parent ChessPieces object with a location and color attribute."""
        super().__init__(location, color)

    def __str__(self):  # method with __ is special
        """Creates a method using str to return an object in string format. In this case it is a R
            to represent the Rook and is displayed to the two people playing this Chess game."""
        return "R"

    def is_valid_move(self, move_to_column, move_to_row):   #parameters are the goal index number
        """This method checks if the Rook piece itself can move the steps in rows and columns
            legally as desired by the user."""
        integer_position = string_to_integers(self.get_location()) #current location is now a tuple ex. (0,0)

        column_steps = move_to_column - integer_position[0]
        row_steps = move_to_row - integer_position[1]

        if column_steps != 0:
            if row_steps == 0:
                return True
            elif row_steps != 0:
                return False

        if row_steps != 0:
            if column_steps == 0:
                return True
            elif row_steps != 0:
                return False

    def is_king_in_check(self, king, board):
        """This method checks if the opponent's king (in the parameter) is being checked
            by an opponent's piece. The board parameter is the board itself."""
        upwards_position = string_to_integers(self.get_location())
        for _ in range(len(board)):
            # adding 1 to current position to upwards path
            upwards_position[0] = upwards_position[0] + 1

            try:
                if type(board[upwards_position[0]][upwards_position[1]]) is King and board[upwards_position[0]][upwards_position[1]].get_color() == king.get_color():  # if equal to target king's color
                    #print("King color", board[upwards_position[0]][upwards_position[1]].get_color())
                    #print("upwards")
                    return True

                elif board[upwards_position[0]][upwards_position[1]] != "_":
                    break
            except IndexError:  # if we don't hit anything, keep adding 1 and if off board stop adding one and get out
                break


        right_position = string_to_integers(self.get_location())
        for _ in range(len(board)):
            # adding 1 to current position to upwards path
            right_position[1] = right_position[1] + 1

            try:
                if type(board[right_position[0]][right_position[1]]) is King and board[right_position[0]][right_position[1]].get_color() == king.get_color():  # if equal to target king's color
                    #print("King color", board[right_position[0]][right_position[1]].get_color())
                    #print("right")
                    return True
                elif board[right_position[0]][right_position[1]] != "_":
                    break
            except IndexError:  # if we don't hit anything, keep adding 1 and if off board stop adding one and get out
                break

        down_position = string_to_integers(self.get_location())
        for _ in range(len(board)):
            # adding 1 to current position to upwards path
            down_position[0] = down_position[0] - 1
            #print("square", board[down_position[0]][down_position[1]])

            try:
                if type(board[down_position[0]][down_position[1]]) is King and board[down_position[0]][down_position[1]].get_color() == king.get_color(): #if equal to target king's color
                    #print("King color", board[down_position[0]][down_position[1]].get_color())
                    #print("down")
                    return True

                elif board[down_position[0]][down_position[1]] != "_":
                    break
            except IndexError:  # if we don't hit anything, keep adding 1 and if off board stop adding one and get out
                break

        left_position = string_to_integers(self.get_location())
        for _ in range(len(board)):
            # adding 1 to current position to upwards path
            left_position[1] = left_position[1] - 1

            try:
                if type(board[left_position[0]][left_position[1]]) is King and board[left_position[0]][left_position[1]].get_color() == king.get_color():  # if equal to target king's color
                    #print("King color", board[left_position[0]][left_position[1]].get_color())
                    #print("left")
                    return True
                elif board[left_position[0]][left_position[1]] != "_":
                    break
            except IndexError:  # if we don't hit anything, keep adding 1 and if off board stop adding one and get out
                break

        return False

class Bishop(ChessPieces):
    """Represents a Bishop piece from chess using attributes from the parent class ChessPieces."""
    def __init__(self, location, color):
        """Creates a Bishop object under parent ChessPieces object with a location and color attribute."""
        super().__init__(location, color)
        pass
    def __str__(self):  # method with __ is special
        """Creates a method using str to return an object in string format. In this case it is a B
            to represent the Bishop and is displayed to the two people playing this Chess game."""
        return "B"

    def is_valid_move(self, move_to_column, move_to_row):  # parameters are the goal index number
        """This method checks if the Rook piece itself can move the steps in rows and columns
            legally as desired by the user."""
        integer_position = string_to_integers(self.get_location())  # current location is now a tuple ex. (0,0)

        column_steps = move_to_column - integer_position[0]
        row_steps = move_to_row - integer_position[1]

        if abs(column_steps) == abs(row_steps):
            return True
        else:
            return False

    def is_king_in_check(self, king, board):
        """This method checks if the opponent's king (in the parameter) is being checked
            by an opponent's piece. The board parameter is the board itself."""
        upright_position = string_to_integers(self.get_location())
        for _ in range(len(board)):
            # adding 1 to current position to upwards path
            upright_position[0] = upright_position[0] + 1
            upright_position[1] = upright_position[1] + 1

            try:
                if type(board[upright_position[0]][upright_position[1]]) is King and board[upright_position[0]][upright_position[1]].get_color() == king.get_color():
                    return True
                elif board[upright_position[0]][upright_position[1]] != "_":
                    break
            except IndexError:  # if we don't hit anything, keep adding 1 and if off board stop adding one and get out
                break

        upleft_position = string_to_integers(self.get_location())
        for _ in range(len(board)):
            # adding 1 to current position to upwards path
            upleft_position[0] = upleft_position[0] + 1
            upleft_position[1] = upleft_position[1] - 1

            try:
                if type(board[upleft_position[0]][upleft_position[1]]) is King and board[upleft_position[0]][upleft_position[1]].get_color() == king.get_color() :
                    return True

                elif board[upleft_position[0]][upleft_position[1]] != "_":
                    break
            except IndexError:  # if we don't hit anything, keep adding 1 and if off board stop adding one and get out
                break

        downright_position = string_to_integers(self.get_location())
        for _ in range(len(board)):
            # adding 1 to current position to upwards path
            downright_position[0] = downright_position[0] - 1
            downright_position[1] = downright_position[1] + 1

            try:
                if type(board[downright_position[0]][downright_position[1]]) is King and board[downright_position[0]][downright_position[1]].get_color() == king.get_color() :
                    return True

                elif board[downright_position[0]][downright_position[1]] != "_":
                    break
            except IndexError:  # if we don't hit anything, keep adding 1 and if off board stop adding one and get out
                break

        downleft_position = string_to_integers(self.get_location())
        for _ in range(len(board)):
            # adding 1 to current position to upwards path
            downleft_position[0] = downleft_position[0] - 1
            downleft_position[1] = downleft_position[1] - 1

            try:
                if type(board[downleft_position[0]][downleft_position[1]]) is King and board[downleft_position[0]][downleft_position[1]].get_color() == king.get_color():
                    return True

                elif board[downleft_position[0]][downleft_position[1]] != "_":
                    break
            except IndexError:  # if we don't hit anything, keep adding 1 and if off board stop adding one and get out
                break

        return False

class Knight(ChessPieces):
    """Represents a knight piece from chess using attributes from the parent class ChessPieces."""
    def __init__(self, location, color):
        """Creates a Knight object under parent ChessPieces object with a location and color attribute."""
        super().__init__(location, color)
        pass
    def __str__(self):  # method with __ is special
        """Creates a method using str to return an object in string format. In this case it is a N
            to represent the Bishop and is displayed to the two people playing this Chess game."""
        return "N"

    def is_valid_move(self, move_to_column, move_to_row):  # parameters are the goal index number
        """This method checks if the Rook piece itself can move the steps in rows and columns
            legally as desired by the user."""
        integer_position = string_to_integers(self.get_location())  # current location is now a tuple ex. (0,0)

        column_steps = move_to_column - integer_position[0]
        row_steps = move_to_row - integer_position[1]

        if abs(row_steps) == 2 and abs(column_steps) == 1:
            return True
        elif abs(column_steps) == 2 and abs(row_steps) == 1:
            return True
        else:
            return False

    def is_king_in_check(self, king, board):
        """This method checks if the opponent's king (in the parameter) is being checked
            by an opponent's piece. The board parameter is the board itself."""
        threat_list = []
        integer_position = string_to_integers(self.get_location())
        king_location = string_to_integers(king.get_location())

        threat_list.append([integer_position[0] + 2, integer_position[1] + 1])
        threat_list.append([integer_position[0] + 2, integer_position[1] - 1])
        threat_list.append([integer_position[0] + 1, integer_position[1] + 2])
        threat_list.append([integer_position[0] + 1, integer_position[1] - 2])
        threat_list.append([integer_position[0] - 2, integer_position[1] + 1])
        threat_list.append([integer_position[0] - 2, integer_position[1] - 1])
        threat_list.append([integer_position[0] - 1, integer_position[1] + 2])
        threat_list.append([integer_position[0] - 2, integer_position[1] - 2])

        for element in threat_list:
            if king_location == element:
                #print("Knight is checking the king")
                return True

        return False

class ChessBoard:
    """Represents a chess board to place the pieces at starting position with attributes board and pieces."""
    def __init__(self):
        """Creates a board object with a board list and pieces attributes."""
        self._board = [] #for loop to append into list
        size = 8

        for amount in range(size): #append 8 empty lists into the bigger list
            self._board.append([])

        for each_list in self._board: #8x8 square
            for each_tile in range(size): #goes through each row vertically size 8
                each_list.append("_") #appends _ 8 times

        self.place_pieces()           # a method that is called when object is first created
    def display_board(self):
        """Method to display the board itself to the user by using an underscore to represent empty
        squares and the pieces will show up at the bottom of the board."""
        for i in reversed(range(len(self._board))): #7-0
            for lyst in self._board:        #gets individual lists in self._board
                print(lyst[i], end=' ')
            print()

    def get_board(self):
        """Returns the board."""
        return self._board

    def place_pieces(self):
        """This method sets up the board with pieces starting at specific locations for the game."""
        self._board[a][0] = King("a1", "white")
        self._board[a][1] = Rook("a2", "white")
        self._board[b][0] = Bishop("b1", "white")
        self._board[b][1] = Bishop("b2", "white")
        self._board[c][0] = Knight("c1", "white")
        self._board[c][1] = Knight("c2", "white")

        self._board[h][0] = King("h1", "black")
        self._board[h][1] = Rook("h2", "black")
        self._board[g][0] = Bishop("g1", "black")
        self._board[g][1] = Bishop("g2", "black")
        self._board[f][0] = Knight("f1", "black")
        self._board[f][1] = Knight("f2", "black")

class ChessVar:
    """Represents a round of chess play and rules are implemented as the game continues with
    attributes board, turn, game state, and move to check if a black piece has made their move yet."""
    def __init__(self):
        """Creates a ChessVar object to play the game with the chessboard object, whose turn it is
        the game state meaning status of the game, and a move attribute to check if a black piece
        has made their move yet."""
        self._board = ChessBoard()
        self._turn = "white"
        self._game_state = "UNFINISHED"
        self._move = False # black has not made a move yet

    def get_game_state(self):
        """This method displays unfinished, white won, black won, and tie game condition."""
        white_king = None
        black_king = None

        for row in self._board.get_board():
            for piece in row:
                if type(piece) == King:
                    if piece.get_color() == "white":
                        white_king = piece
                    elif piece.get_color() == "black":
                        black_king = piece

        #print("White location", white_king.get_location()[1])
        #print("Black location", black_king.get_location()[1])
        if white_king.get_location()[1] == "8" and black_king.get_location()[1] == "8":
            #print("Game is tie")
            return "TIE"

        if white_king.get_location()[1] == "8":   #.get_location()[1] only looking at first element meaning the row
            if self._move == False:
                self._move = True
                #print("White reached row 8, now black's turn to move")
                return "UNFINISHED"
            elif self._move == True:
                #print("White reached row 8, black's turn is nowhere close to 8.")
                return "WHITE_WON"

        if black_king.get_location()[1] == "8":
            #print("Black reached row 8 and white has ran out of moves")
            return "BLACK_WON"

        return "UNFINISHED"

    def change_turn(self):
        """This method displays to the opponent the turn it is to make the next moves."""
        if self._turn == "white":
            return "black"
        else:
            return "white"

    def make_move(self, move_from, move_to):    #parameters are strings
        """This method allows the chess game to be played by checking if a spot can be moved to and whose
        turn it is that can move. Also, this method will update the pieces of the board."""
        from_move = string_to_integers(move_from)
        to_move = string_to_integers(move_to)

        if self._game_state != "UNFINISHED":
            return False

        if self._board.get_board()[from_move[0]][from_move[1]] == "_":
            #print("No piece there.")
            return False    #empty square

        current_chess_piece = self._board.get_board()[from_move[0]][from_move[1]]
        # check to make sure turn is equal to the white or black piece movement
        if current_chess_piece.get_color() != self._turn:
            #print("Not your piece.")
            return False

        if self._board.get_board()[to_move[0]][to_move[1]] != "_":  #cannot eat your own pieces of the same color
            piece = self._board.get_board()[to_move[0]][to_move[1]]
            if current_chess_piece.get_color() == piece.get_color():
                #print("Cannot move to since your piece is there.")
                return False

        if current_chess_piece.is_valid_move(to_move[0], to_move[1]) == False:
            #print("Not legal piece steps.")
            return False

        if current_chess_piece.is_valid_move(to_move[0], to_move[1]) == True:
            # king threat checking
            # at every turn check if your own king is in check or check if opponent's king will be in check
            white_king = None
            black_king = None

            for row in self._board.get_board():
                for piece in row:
                    if type(piece) == King:
                        if piece.get_color() == "white":
                            white_king = piece
                        elif piece.get_color() == "black":
                            black_king = piece

            if self.king_check(white_king, move_from, move_to, current_chess_piece, self._board.get_board()) == True:     # checks if white king's move will put itself to check or opponent will put king into check
                #print("Checking of white king not allowed")
                return False

            if self.king_check(black_king, move_from, move_to, current_chess_piece, self._board.get_board()) == True:
                #print("Checking of black king not allowed")
                return False

            #if neither king are in check meaning False we can make a move

            # piece location
            current_chess_piece.set_location(move_to)

            # board location
            self._board.get_board()[to_move[0]][to_move[1]] = current_chess_piece   #ending location of the moved chess piece
            self._board.get_board()[from_move[0]][from_move[1]] = "_"


        self._turn = self.change_turn()

    def king_check(self, king, move_from, move_to, current_chess_piece, board): # board simulation looking if the king WILL be in check
        """This method simulates if a king will be in check by looking at the board in a future mode
        because the game needs to call out the player to make sure they are not going to threaten
        their opponent's king from trying to play the game correctly."""
        from_move = string_to_integers(move_from)
        to_move = string_to_integers(move_to)

        #board = copy.deepcopy(old_board)

        current_chess_piece.set_location(move_to)
        board[to_move[0]][to_move[1]] = current_chess_piece     #using board as a parameter to make a simulation of a board and not using the real board
        board[from_move[0]][from_move[1]] = "_"

        if self.check_threatening_paths(king, current_chess_piece.get_color(), board) == True:
            return True
        else:
            return False

    def check_threatening_paths(self, king, color, board):
        """This method uses the simulated board to imitate if an individual piece that is made by the
        player will make a threatening path to put their opponent's king in check."""
        threat_pieces = []
        for row in board:   #this double for loop gets every opponents piece first before checking if the king is in check
            for piece in row:
                if piece == "_":
                    continue      #king not in check
                if king.get_color() != piece.get_color():
                    threat_pieces.append(piece)

        for each_piece in threat_pieces:    # check each piece in list to see if the king is in check
            is_checked = each_piece.is_king_in_check(king, board)
            if is_checked == True:
                return True

        return False

    def get_turn(self):
        """Returns who turn it is to play the game."""
        return self._turn



game = ChessVar()
while True:
    game._board.display_board()
    print(game.get_turn())
    from_move = input("Please enter from: ")
    to = input("Please enter to: ")
    game.make_move(from_move, to)
    status = game.get_game_state()
    if status == "WHITE_WON" or status == "BLACK_WON" or status == "TIE":
        break

if status == "WHITE_WON":
    print("White won")

if status == "BLACK_WON":
    print("Black won")

if status == "TIE":
    print("Tie game")

game._board.display_board()


move_result = game.make_move('c2', 'e3')
game.make_move('g1', 'f1')
game.make_move("g2","f3")
game._board.display_board()

state = game.get_game_state()