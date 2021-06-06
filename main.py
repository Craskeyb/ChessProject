#Project created by Brett Craskey#

#Utilizes python-chess library (listed in requirements.txt file)#
import chess
import chess.pgn
from pgnReader import gameRead
from randPos import posPic

print("Welcome to the Chess Recall Program!")
print("\n-------------------------------------")

gameList = gameRead()

posPic(gameList)

















