#File containing loop that reads games until the minimum number has been reached#
import chess
import chess.pgn

def gameRead():
    print("***You must enter a minimum of 3 games to choose from (2 games would be too easy to guess from!)")
    
    #Create an empty list for loaded games
    gameList = []

    #While loop based on counter
    while(len(gameList) < 3):

        #make sure there is no file or the file is not already in the gamelist
        while(filename == '' or filename not in gameList):
        
        #grab files from user and check if there is an error
            try:
                filename = input("\nPlease enter the name of your PGN file (without the .pgn at the end): ")
            except FileNotFoundError:
                print("\nFile not found, try a different filename!")

        #read in game
        file = f"{filename}.pgn"
        pgn = open(file)
        game = chess.pgn.read_game(pgn)

        #check to make sure it is over the required move count (20)
        board = game.board()
        movect = 0
        for move in game.maineline_moves():
            board.push(move)
            movect = movect+1
        
        if(movect <= 20):
            print("\n Not enough moves in this game, miniatures (<=20 moves) are not allowed!")



        gameList.append(chess.pgn.read_game(pgn))
    
    print
    return gameList
    