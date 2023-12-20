"""
requirement:
pip install chess

"""
import time
import chess
import argparse
import importlib
import os
import BotTemplate
import inspect
import tokenize


TOKEN_NOT_COUNTED_IN_CODE_SIZE = [tokenize.COMMENT]

parser = argparse.ArgumentParser("Script for running a battle between 2 AI")
parser.add_argument("file_ai_1")
parser.add_argument("file_ai_2")
parser.add_argument("--max_length", type=int, default=1000, help="maximum length of the code in number of tokens")
parser.add_argument("--time_per_bot", type=float, default=60.0)
parser.add_argument("--nb_games", type=int, default=1)
parser.add_argument("-v","--verbose", action="store_true")


def count_tokens(file_path):
    """
    count the nomber of token in the code
    """
    with tokenize.open(file_path) as f:
        tokens = tokenize.generate_tokens(f.readline)
        nb_tokens = len([token for token in tokens if token.type not in [TOKEN_NOT_COUNTED_IN_CODE_SIZE]])
    return nb_tokens
        


def load_ai(file_path, max_length=1000) :
    """
    This check if the length of the code is inferior to max_length and load the AI
    """
    assert (count_tokens(file_path) < max_length) , f"ERROR: code from {file_path} have more than {max_length} tokens"
    
    BotModule = importlib.import_module(file_path[:-3])
    for attr_name in dir(BotModule):
        if(inspect.isclass(getattr(BotModule, attr_name)) and issubclass(getattr(BotModule, attr_name), BotTemplate.Bot)):
            return attr_name, getattr(BotModule, attr_name)()
    print(f"found no class based on BotTemplate.Bot in {file_path}")
            

def board_position_as_upper_and_lower_cases_letters(board):
    """ from stack overflow :) """
    pgn = board.epd()
    foo = []
    pieces = pgn.split(" ", 1)[0]
    rows = pieces.split("/")
    for row in rows:
        foo2 = [] 
        for thing in row:
            if thing.isdigit():
                for i in range(0, int(thing)):
                    foo2.append('.')
            else:
                foo2.append(thing)
        foo.append(foo2)
    return foo


def run_battle(args):
    """
    """
    if(args.verbose):   
            print("load bots ...")
    name_bot_1, bot1 = load_ai(args.file_ai_1, max_length=args.max_length)
    name_bot_2, bot2 = load_ai(args.file_ai_2, max_length=args.max_length)
    bots = [bot1, bot2]
    names = [name_bot_1, name_bot_2]

    timers = [args.time_per_bot, args.time_per_bot]
    
    if(args.verbose):   
            print("prepare board ...")
    board = chess.Board()
    current_player = -1 # the first player to play is 0 then 1 then 0 then 1 ....
    while not board.is_game_over():
        if(args.verbose):
            print(board)
            print("===========================")
        current_player = (current_player + 1) % 2
        board_position = board_position_as_upper_and_lower_cases_letters(board)
        legal_move_uci = [m.uci() for m in board.legal_moves]

        if(args.verbose):   
            print(f"Bot {names[current_player]} is thinking ...")
        t_start = time.time()
        move = bots[current_player].make_move(board_position,legal_move_uci, time_left=timers[current_player], you_are=["upper", "lower"][current_player])
        t_end = time.time()
        
        #update the time
        timers[current_player] -= t_end-t_start
        if(timers[current_player] <= 0):
            if(args.verbose):   
                print(f"player {names[current_player]} lose on time :'(")
            print(f"resultat entre {names[0]} et {names[1]} : {1*(current_player==0)}-{1*(current_player==1)}")
        else:
            if(args.verbose):   
                print(f"player {names[current_player]} time left : {timers[current_player]}")
        
        # add the move to the board
        move_c = chess.Move.from_uci(move)
        assert move_c in board.legal_moves, f"{names[current_player]} did not return a legal move !"
        board.push(move_c) # add the move
        
        
    if(args.verbose):   
        print(board)
    print(f"resultat entre {names[0]} et {names[1]} : {board.result()}")



if __name__ == "__main__":
    args = parser.parse_args()
    for _ in range(args.nb_games):
        run_battle(args)