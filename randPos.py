#File containing the function that will pick a random position and produce a PNG file of it#

import cairosvg
import chess
import chess.pgn
import chess.svg

def posPic(gameList):

    game = gameList[0]
    board = game.board()


  