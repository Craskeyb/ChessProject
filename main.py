#Project created by Brett Craskey#

#Utilized python-chess library (listed in requirements.txt file)#

import chess
import chess.pgn
import chess.svg

print("Welcome to the Chess Recall Program!")
print("\n-------------------------------------")
filename = input("\nPlease enter the name of your PGN file (without the .pgn at the end): ")

readfile = True

filename = f"{filename}.pgn"

pgn = open(filename)

game = chess.pgn.read_game(pgn)

print(game.headers["White"]+ ' vs. ' + game.headers["Black"])

print(game)

board = game.board()

squares = chess.SquareSet(chess.BB_ALL)
chess.svg.board(board,squares=squares, size=400)









