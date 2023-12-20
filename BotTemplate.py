class Bot():
    def __init__(self):
        """
        prepare your variable etc before the start of the game
        load your weights etc

        you can save variables between turns your bot instance.
        """
        pass
    
    def make_move(self, board_position, list_of_possible_move, time_left:float,  you_are="upper"):
        """
        should return one of the possible moves

        board_position_exemple :  (UPPER_CASE is White)

        [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], 
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], 
        ['.', '.', '.', '.', '.', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.', '.', '.'], 
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], 
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]


        list of possible move is given in uci format:
        exemple : 
        e2e4 for a first move (pawn from e2 to e4)

        time_left:
        gives you the time left on your clock (in seconds)

        you_are:
        tell you if you are the "upper" caracter pieces (white) or "lower" (black)
        """
        return list_of_possible_move[0]