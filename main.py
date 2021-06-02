#Project created by Brett Craskey#

#Utilized python-chess library (listed in requirements.txt file)#

import chess
import chess.pgn
import chess.svg


print("Welcome to the Chess Recall Program!")
print("\n-------------------------------------")
filename = input("\nPlease enter the name of your PGN file (without the .pgn at the end): ")

filename = f"{filename}.pgn"

pgn = open(filename)

game = chess.pgn.read_game(pgn)

board = game.board()

image = chess.svg.piece(chess.Piece.from_symbol("R"))











