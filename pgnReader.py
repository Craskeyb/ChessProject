#File containing loop that reads games until the minimum number has been reached#
import chess


def gameRead():
    print("***You must enter a minimum of 3 games to choose from (2 games would be too easy to guess from!)")
    
    #Create a counter for games, and an empty list for loaded games
    filecount = 0
    gameList = []

    #While loop based on counter
    while(filecount < 3):
        
        #grab files from user and check if there is an error
        filename = input("\nPlease enter the name of your PGN file (without the .pgn at the end): ")
        
        if(not filename.exists()):
            print("That file doesn't Exist! Try another name")
        else:
            file = f"{filename}.pgn"
            pgn = open(file)
            gameList.append(chess.pgn.read_game(pgn))
            filecount = filecount+1
        

    