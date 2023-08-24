from time import sleep
import os
import random
import sys
x = 1000000000
sys.setrecursionlimit(x)
#import maths
#loading the needed global variabels needed in functionm:
global rounds
global board
global player
print("Work in progress")
# make the board.
board = ["Ignore me!", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
rounds = 0
#boolean variable to continue playing
playing = True
choice = ""
ComputerLet = ""
depth = 0
global count
count = 0

#board creation
global format_0
format_0="+---" + "+--" + "-+" + "---+\n" 
def DisplayBoard(board):
    print(format_0+
          "| " + board[7] + " | " + board[8] + " | " + board[9] + " |\n" +
          format_0+
          "| " + board[4] + " | " + board[5] + " | " + board[6] + " |\n" +
          format_0+
          "| " + board[1] + " | " + board[2] + " | " + board[3] + " |\n" +
          format_0)
    
#welcome message funtion that leads to the player movement funtion.
def welcome0():
    print("Welcome to TicTacToe!\n \nLEVEL 0:")
    print(format_0+
          "| " + "7" + " | " + "8" + " | " + "9" + " |\n" +
          format_0+
          "| " + "4" + " | " + "5" + " | " + "6" + " |\n" +
          format_0+
          "| " + "1" + " | " + "2" + " | " + "3" + " |\n" +
          format_0)
    print("player one will start as x")
    global rounds
    global player
    rounds = rounds + 1
    player = "X"
    PlayerMove0()

def welcome1():
    global rounds
    global choice
    print("Welcome to TicTacToe!\n  \nLEVEL 1:")
    print("+---" + "+--" + "-+" + "---+\n" +
          "| " + "7" + " | " + "8" + " | " + "9" + " |\n" +
          "+---" + "+--" + "-+" + "---+\n" +
          "| " + "4" + " | " + "5" + " | " + "6" + " |\n" +
          "+---" + "+--" + "-+" + "---+\n" +
          "| " + "1" + " | " + "2" + " | " + "3" + " |\n" +
          "+---" + "+--" + "-+" + "---+\n")
    #ask the user which letter tehyw ant to play
    choice = input("enter which player you will be: (O or X):\n").upper()
    while choice != "X" and choice != "O":
        choice = input("invalid character enter either O or X\n").upper()
    rounds = rounds + 1
    FirstMove1(choice)

def welcome2():
    #makeing variables global so they can be used in function
    global rounds
    global choice
    #displays welcome message
    print("Welcome to TicTacToe!\n\nLEVEL 2:")
    print("+---" + "+--" + "-+" + "---+\n" +
          "| " + "7" + " | " + "8" + " | " + "9" + " |\n" +
          "+---" + "+--" + "-+" + "---+\n" +
          "| " + "4" + " | " + "5" + " | " + "6" + " |\n" +
          "+---" + "+--" + "-+" + "---+\n" +
          "| " + "1" + " | " + "2" + " | " + "3" + " |\n" +
          "+---" + "+--" + "-+" + "---+\n")
    choice = input("enter which player you will be: (O or X):\n").upper()
    while choice != "X" and choice != "O":
        choice = input("invalid character enter either O or X\n").upper()
    rounds = rounds + 1
    FirstMove2(choice)


def welcome3():
    #makeing variables global so they can be used in function
    global rounds
    global choice
    #displays welcome message
    print("Welcome to TicTacToe!\n\nLEAVEL 3:")
    print("+---" + "+--" + "-+" + "---+\n" +
          "| " + "7" + " | " + "8" + " | " + "9" + " |\n" +
          "+---" + "+--" + "-+" + "---+\n" +
          "| " + "4" + " | " + "5" + " | " + "6" + " |\n" +
          "+---" + "+--" + "-+" + "---+\n" +
          "| " + "1" + " | " + "2" + " | " + "3" + " |\n" +
          "+---" + "+--" + "-+" + "---+\n")
    choice = input("enter which player you will be: (O or X):\n").upper()
    while choice != "X" and choice != "O":
        choice = input("invalid character enter either O or X\n").upper()
    rounds = rounds + 1
    FirstMove3(choice)

#welcoming function
def welcome4():
    #makeing variables global so they can be used in function
    global rounds
    global choice
    #displays welcome message
    print("Welcome to TicTacToe!\n \nLEVEL 4:")
    print("+---" + "+--" + "-+" + "---+\n" +
          "| " + "7" + " | " + "8" + " | " + "9" + " |\n" +
          "+---" + "+--" + "-+" + "---+\n" +
          "| " + "4" + " | " + "5" + " | " + "6" + " |\n" +
          "+---" + "+--" + "-+" + "---+\n" +
          "| " + "1" + " | " + "2" + " | " + "3" + " |\n" +
          "+---" + "+--" + "-+" + "---+\n")
    choice = input("enter which player you will be: (O or X):\n").upper()
    while choice != "X" and choice != "O":
        choice = input("invalid character enter either O or X\n").upper()
    rounds = rounds + 1
    FirstMove4(choice)

#function to decide if computer will be makeing a move or if player will be making a move   
def FirstMove1(choice):
    global rounds
    XorO = rounds % 2
    if XorO == 1:
        if choice == "X":
            player = choice
            PlayerMove1()
        elif choice == "O":
            player = choice
            ComputerMove1()
    elif XorO == 0:
        if choice == "X":
            player = choice
            ComputerMove1()
        elif choice == "O":
            player = choice
            PlayerMove1()
            
def FirstMove2(choice):
    global rounds
    global ComputerLet
    XorO = rounds % 2
    if XorO == 1:
        if choice == "X":
            Player = choice
            PlayerMove2()
        elif choice == "O":
            ComputerMove2()
            check(board,ComputerLet)
            DisplayBoard(board)
    elif XorO == 0:
        if choice == "X":
            ComputerMove2()
            check(board,ComputerLet)
            DisplayBoard(board)
        elif choice == "O":
            player = choice
            PlayerMove2()


def FirstMove3(choice):
    global rounds
    global ComputerLet
    XorO = rounds % 2
    if XorO == 1:
        if choice == "X":
            player = choice
            PlayerMove3()
        elif choice == "O":
            ComputerMove3()
            check(board,ComputerLet)
            DisplayBoard(board)
    elif XorO == 0:
        if choice == "X":
            ComputerMove3()
            check(board,ComputerLet)
            DisplayBoard(board)
        elif choice == "O":
            player = choice
            PlayerMove3()

#function ot coordinate who is makeing the moves   
def FirstMove4(choice):
    global rounds
    global ComputerLet
    XorO = rounds % 2
    if XorO == 1:
        if choice == "X":
            PlayerMove4()
        elif choice == "O":
            ComputerMove4()
            check(board,ComputerLet)
            DisplayBoard(board)
    elif XorO == 0:
        if choice == "X":
            ComputerMove4()
            check(board,ComputerLet)
            DisplayBoard(board)
        elif choice == "O":
            player = choice
            PlayerMove4()

#function to make player's move
def PlayerMove0():
    global player
    global rounds
    XorO = rounds % 2
    #this prints out what round the game is currently on odd rounds would be X's turn whilst even rounds are O's turn
    print("round", rounds)
    #the selctive statment for decideing which players move it is.
    if XorO == 1:
        player = "X"
        #implementing Try and accept funtion to code to make it more robust
        try:
            move = int(input("X's move: enter a value between 1 and 9 for a point on the board:\n"))
            while (move < 1 or move > 9) :
                print("invalid move enter a value between 1 and 9")
                move = int(input())
                Empty(move, player)
            while Empty(move, player) == False:
                move = int(input("SpaceTaken! reenter move:\n"))
                Empty(move,player)
            board[move] = player
            rounds = rounds + 1
            check3()
            DisplayBoard(board)
        except:
            print("not a legal move try again the value you entered must be a number")
    else:
        player = "O"
        try:
            move = int(input("O's move: enter a value between 1 and 9 for a point on the board:\n"))
            while (move < 1 or move > 9) :
                print("invalid move enter a value between 1 and 9")
                move = int(input())
                Empty(move, player)
            while Empty(move, player) == False:
                move = int(input("SpaceTaken! reenter move:\n"))
                Empty(move,player)
            board[move] = player
            rounds = rounds + 1
            check3()
            DisplayBoard(board)
        except:
            print("not a legal move try again the value you entered must be a number")

#code behind Player's movement
#comments are just for the chnges that i mad to simple tic tac to game 
def PlayerMove1():
    global rounds
    global board
    global player
    print("round: ",rounds)
    print("player move!:")
    XorO = rounds % 2
    if XorO == 1:
        player = "X"
        #implementing Try and accept funtion to code to make it more robust
        try:
            move = int(input("X's move: enter a value between 1 and 9 for a point on the board:\n"))
            while (move < 1 or move > 9) :
                print("invalid move enter a value between 1 and 9")
                move = int(input())
                Empty(move, player)
            while Empty(move, player) == False:
                move = int(input("SpaceTaken! reenter move:\n"))
                Empty(move,player)
            board[move] = player
            rounds = rounds + 1
            check3()
            DisplayBoard(board)
        except:
            print("not a legal move try again the value you entered must be a number")
    else:
        player = "O"
        try:
            move = int(input("O's move: enter a value between 1 and 9 for a point on the board:\n"))
            while (move < 1 or move > 9) :
                print("invalid move enter a value between 1 and 9")
                move = int(input())
                Empty(move, player)
            while Empty(move, player) == False:
                move = int(input("SpaceTaken! reenter move:\n"))
                Empty(move,player)
            board[move] = player
            rounds = rounds + 1
            check3()
            DisplayBoard(board)
        except:
            print("not a legal move try again the value you entered must be a number")

def PlayerMove2():
    #makeing varibles global for later use in function
    global rounds
    global board
    global player
    print("Round:",rounds)
    print("player's move!:")
    XorO = rounds % 2
    if XorO == 1:
        player = "X"
        try:
            move = int(input("X's move: enter a value between 1 and 9 for a point on the board:\n"))
            while (move < 1 or move > 9):
                print("invalid move enter a value between 1 and 9")
                move = int(input())
            Empty(move, player)
            while Empty(move, player) == False:
                move = int(input("SpaceTaken! reenter move:\n"))
                Empty(move,player)
            board[move] = player
            rounds = rounds + 1
            check(board, player)
            DisplayBoard(board)
        except:
            print("not a legal move try again the value you entered must be a number")
    else:
        player = "O"
        try:
            move = int(input("O's move: enter a value between 1 and 9 for a point on the board:\n"))
            while (move < 1 or move > 9):
                print("invalid move enter a value between 1 and 9")
                move = int(input())
            Empty(move, player)
            while Empty(move, player) == False:
                move = int(input("SpaceTaken! reenter move:\n"))
                Empty(move,player)
            board[move] = player
            rounds = rounds + 1
            check(board,player)
            DisplayBoard(board)
        except:
            print("not a legal move try again the value you entered must be a number")


#function that allows for the player movement
def PlayerMove3():
    #makeing varibles global for later use in function
    global rounds
    global board
    global player
    print("Round:",rounds)
    print("player's move!:")
    XorO = rounds % 2
    if XorO == 1:
        player = "X"
        try:
            move = int(input("X's move: enter a value between 1 and 9 for a point on the board:\n"))
            while (move < 1 or move > 9):
                print("invalid move enter a value between 1 and 9")
                move = int(input())
            Empty(move, player)
            while Empty(move, player) == False:
                move = int(input("SpaceTaken! reenter move:\n"))
                Empty(move,player)
            board[move] = player
            rounds = rounds + 1
            check(board, player)
            DisplayBoard(board)
        except:
            print("not a legal move try again the value you entered must be a number")
    else:
        player = "O"
        try:
            move = int(input("O's move: enter a value between 1 and 9 for a point on the board:\n"))
            while (move < 1 or move > 9):
                print("invalid move enter a value between 1 and 9")
                move = int(input())
            Empty(move, player)
            while Empty(move, player) == False:
                move = int(input("SpaceTaken! reenter move:\n"))
                Empty(move,player)
            board[move] = player
            rounds = rounds + 1
            check(board,player)
            DisplayBoard(board)
        except:
            print("not a legal move try again the value you entered must be a number")

#function that allows for the player movement
def PlayerMove4():
    #makeing varibles global for later use in function
    global rounds
    global board
    global player
    print("Round:",rounds)
    print("player's move!:")
    XorO = rounds % 2
    if XorO == 1:
        player = "X"
        try:
            move = int(input("X's move: enter a value between 1 and 9 for a point on the board:\n"))
            while (move < 1 or move > 9):
                print("invalid move enter a value between 1 and 9")
                move = int(input())
            Empty(move, player)
            while Empty(move, player) == False:
                move = int(input("SpaceTaken! reenter move:\n"))
                Empty(move,player)
            board[move] = player
            rounds = rounds + 1
            check(board, player)
            DisplayBoard(board)
        except:
            print("not a legal move try again")
    else:
        player = "O"
        try:
            move = int(input("O's move: enter a value between 1 and 9 for a point on the board:\n"))
            while (move < 1 or move > 9):
                print("invalid move enter a value between 1 and 9")
                move = int(input())
            Empty(move, player)
            while Empty(move, player) == False:
                move = int(input("SpaceTaken! reenter move:\n"))
                Empty(move,player)
            board[move] = player
            rounds = rounds + 1
            check(board,player)
            DisplayBoard(board)
        except:
            print("not a legal move try again the value u entered must be a number")

#funtion to make the computer's move
def ComputerMove1():
    global rounds
    global board
    global player
    #diaplay the round that the game is on
    print("round: ",rounds)
    print("computer move!:")
    XorO = rounds % 2
    if XorO == 1:
        #how the computer's X player is coded
        player = "X"
        #a random numerical valueis calculated between 1 and 9 to represent the posible possitions on the board
        move = random.randint(1,9)
        #checks if move picked is available on the board
        Empty(move, player)
        #if the moove is not available continue to pick a random number untill available move is picked
        while Empty(move, player) == False:
            move = random.randint(1,9)
            Empty(move,player)
        #mark the board with the computer's letter
        board[move] = player
        print("computer moved to = ",move)
        rounds = rounds + 1
        check3()
        DisplayBoard(board)
    else:
        #repeat X for O
        player = "O"
        move = random.randint(1,9)
        Empty(move, player)
        while Empty(move, player) == False:
            move = random.randint(1,9)
            Empty(move,player)
        board[move] = player
        print("computer moved to = ",move)
        rounds = rounds + 1
        check3()
        DisplayBoard(board)

def ComputerMove2():
    global rounds
    global board
    global player
    global ComputerLet
    print("Round:",rounds)
    print("Computer's move!:")
    XorO = rounds % 2
    if XorO == 1:
        rounds = rounds + 1
        ComputerLet = "X"#computer letter
        PlayerLet = "O"#player letter 
        #make a list of possible moves
        possiblemoves = []
        for place, possible in enumerate(board):#enumerate gives me the value that is a possition of th elist
            if (possible != "O" and possible != "X") and (place != 0):#value in list possition is saved to possible place in list is saved toi place
                possiblemoves.append(place)

        #checking if the player can win or computer can win
        for player in [ComputerLet,PlayerLet]:
            for place in possiblemoves: # goes thriugh all possible moves on the board
                boardcopy = board[:] #make a copy of board
                boardcopy[place] = player
                if check2(boardcopy,player):
                    board[place] = ComputerLet #this still works even if both the
                    print("computer moved to = ",place)
                    return 

        move = SelectRandom(possiblemoves)
        #mark the board with the computer's letter
        board[move] = ComputerLet
        print("computer moved to = ",move)
        return
            
    else:
        rounds = rounds + 1
        ComputerLet = "O"#computer letter
        PlayerLet = "X"#player letter 
        #make a list of possible moves
        possiblemoves = []
        for place, possible in enumerate(board):#enumerate gives me the value that is a possition of th elist
            if (possible != "O" and possible != "X") and (place != 0):#value in list possition is saved to possible place in list is saved toi place
                possiblemoves.append(place)

        #checking if the player can win or computer can win
        for player in [ComputerLet,PlayerLet]:
            for place in possiblemoves:
                boardcopy = board[:]
                boardcopy[place] = player
                if check2(boardcopy,player):
                    board[place] = ComputerLet #this still works even if both the
                    print("computer moved to = ",place)
                    return
        
        move = SelectRandom(possiblemoves)
        #mark the board with the computer's letter
        board[move] = ComputerLet
        print("computer moved to = ",move)
        return


def ComputerMove3():
    global rounds
    global board
    global player
    global ComputerLet
    print("Round:",rounds)
    print("Computer's move!:")
    XorO = rounds % 2
    if XorO == 1:
        rounds = rounds + 1
        ComputerLet = "X"#computer letter
        PlayerLet = "O"#player letter 

        #make a list of possible moves
        possiblemoves = []
        for place, possible in enumerate(board):#enumerate gives me the value that is a possition of th elist
            if (possible != "O" and possible != "X") and (place != 0):#value in list possition is saved to possible place in list is saved toi place
                possiblemoves.append(place)

        #checking if the player can win or computer can win
        for player in [ComputerLet,PlayerLet]:
            for place in possiblemoves: # goes thriugh all possible moves on the board
                boardcopy = board[:] #make a copy of board
                boardcopy[place] = player
                if check2(boardcopy,player):
                    board[place] = ComputerLet #this still works even if both the
                    print("computer moved to = ",place)
                    return 
        #get a good random moove
        GoodRandomMove(possiblemoves)
        print("computer moved to = ",move)
        return 
            
    else:
        rounds = rounds + 1
        ComputerLet = "O"#computer letter
        PlayerLet = "X"#player letter 

        #make a list of possible moves
        possiblemoves = []
        for place, possible in enumerate(board):#enumerate gives me the value that is a possition of th elist
            if (possible != "O" and possible != "X") and (place != 0):#value in list possition is saved to possible place in list is saved toi place
                possiblemoves.append(place)

        #checking if the player can win or computer can win
        for player in [ComputerLet,PlayerLet]:
            for place in possiblemoves:
                boardcopy = board[:]
                boardcopy[place] = player
                if check2(boardcopy,player):
                    board[place] = ComputerLet #this still works even if both the
                    print("computer moved to = ",place)
                    return 
        GoodRandomMove(possiblemoves)
        print("computer moved to = ",move)
        return

#computer move generator
def ComputerMove4():
    global rounds
    global board
    global player
    global ComputerLet
    print("Round:",rounds)
    print("Computer's move!:")
    count = 0
    XorO = rounds % 2
    if XorO == 1:
        rounds = rounds + 1
        nextmoves = possiblemoves(board)
        depth = len(nextmoves)
        ComputerLet = "X"#computer letter -maxplayer
        PlayerLet = "O"#player letter - min player
        if rounds < 3:
            GoodRandomMove(nextmoves)
        else:
            state = board
            best = 1-1000000000001
            move = MiniMax(state,depth,ComputerLet,best)
            print("computer moved to = ",move)
            board[move] = ComputerLet   
    else:
        rounds = rounds + 1
        nextmoves = possiblemoves(board)
        depth = len(nextmoves)
        ComputerLet = "O"#computer letter
        PlayerLet = "X"#player letter
        print("actual round =", rounds)
        if rounds < 4 :
            if rounds == 3:
                stopit = False
                corners = [7,9,1,3]
                for places in corners:
                    if board[places] == PlayerLet:
                        stopit = True
                if stopit == True:
                    board[5] = ComputerLet
                else:
                    GoodRandomMove(nextmoves)
            else:
                GoodRandomMove(nextmoves)
        else:
            state = board
            best = 100000000000
            move = MiniMax(state,depth,ComputerLet,best)
            print("computer moved to = ",move)
            board[move] = ComputerLet


def MiniMax(state,depth,ComputerLet,best):
    #print(count)
    if count == 0:
        if ComputerLet == "X":
            best = 1-1000000000001
        else:
            best = 1000000000000
    Bbest = best
    #print(Bbest)
    move = SimulateGoodMoves(board,Bbest,ComputerLet)
    return move

def SimulateGoodMoves(state,best,ComputerLet):
    global count
    count = count + 1
    boardcopy = state[:]
    if ComputerLet == "X":
        PlayerLet = "O"
    else:
        PlayerLet = "X"
    PossiblePlaces = possiblemoves(boardcopy)
    #checking if the player can win or computer can win
    for player in [ComputerLet,PlayerLet]:
        for place in PossiblePlaces: # goes thriugh all possible moves on the board
            boardcopy = state[:] #make a copy of board
            boardcopy[place] = player
            if GameOver(boardcopy,player) == "Player":
                move = place #this still works even if both the
                return move
    depth = len(boardcopy)
    for player in ["X","O"]:
        for places in PossiblePlaces:
            boardcopy[places] = places
            boardcopyCon = boardcopy[:]
            boardcopyCon.remove(places)
            depth = len(boardcopy)
            if count < 1000:
                MiniMax(boardcopyCon,depth,player,best)
                if (depth == 0) or (GameOver(boardcopy,player) != "Not Ended") or count == 100:
                    bestscore = Evaluate(boardcopy,depth,player)
                    #print("bestscore = ",bestscore)
                    if ComputerLet == "X":
                        if bestscore > best:
                            move = places
                            best = bestscore
                            return move, best
                    else :
                        if bestscore < best:
                            move = places
                            best = bestscore
                            return move, best
            else:
                move = places
                return move

#generate score of game state.
def Evaluate(state,depth,Player):
    board = state[:]
    if GameOver(board,Player)!= "Draw":
        if Player == "X":
            score = 1*(depth)
        elif Player == "O":
            score = -1*(depth)
        return score
    else:
        score = 0
        return score

#make list of all the possible moves
def possiblemoves(state):
    places = [place for place, possible in enumerate(state) if (possible != "O" and possible != "X") and (place != 0)]
    return places

#function for the computer to make a decisive random move
def GoodRandomMove(possiblemoves):
    global board
    global ComputerLet
    #check if corner open
    opencorners = []
    #make the list of open corners
    for place in possiblemoves:
        if place in [7,9,1,3]:
            opencorners.append(place)
    #pick a random corner from the list
    if len(opencorners) > 0:
        move = SelectRandom(opencorners)
        board[move] = ComputerLet
        print("computer moved to = ",move)
        return    
    #check if center open
    elif 5 in possiblemoves:
        move = 5
        board[move] = ComputerLet
        print("computer moved to = ",move)
        return   
    #check if side open
    opensides = []
    #make the list of open side
    for place in possiblemoves:
        if place in [8,4,6,2]:
            opensides.append(place)
    #pick a random side
    if len(opensides) > 0:
        move = SelectRandom(opensides)
        board[move] = ComputerLet
        print("computer moved to = ",move)
        return  

#function to pick a random place in the posiblemoves list
def SelectRandom(spaces):
    length = len(spaces)
    index = random.randint(0,(length-1))
    picked = spaces[index]
    return picked
    
#function to detecting if space on board it empty or taken
def Empty(move, player):
    if board[move] == "X" or board[move] == "O":
        return False
    elif board[move] != "X" or board[move] != "O":
        return True        

#check if board is full funtion        
def Full(board):
    spaces = False#sets free paces to false
    for i in range(1,9):
        if board[i] != "X" and board[i] != "O":#used to go through the whole board
            spaces = True #changes to true if there is space only if ther is a space

    if spaces == False:
        return True
    else:
        return False

#this check if there is winner on board
def ThreeInRow(board):
    for i in ["O","X"]:
        # straight middle row
        if ((board[4] == board[5] and board[5] == board[6] and board[4] == i)        
        # straight top row
        or (board[7] == board[8] and board[8] == board[9] and board[7] == i)        
        # straight bottom row
        or (board[1] == board[2] and board[2] == board[3] and board[1] == i)
        # diagonal 1
        or (board[7] == board[5] and board[5] == board[3] and board[7] == i)
        # diagonal 2
        or (board[1] == board[5] and board[5] == board[9] and board[1] == i)        
        # straight column middle
        or( board[8] == board[5] and board[5] == board[2] and board[8] == i)        
        # straight column right
        or (board[7] == board[4] and board[4] == board[1] and board[7] == i)        
        # straight column left
        or (board[9] == board[6] and board[6] == board[3]) and board[9] == i):
            winner = i
            return winner
    return False

def GameOver(board, winner):
    global playing
    #checking if the borard is full
    if Full(board):
        return "Draw"
    if ThreeInRow(board) == winner:#check if there is a winer on the board and that winner is the perosn who make the last move
        return "Player"
    elif (ThreeInRow(board) != winner) and (ThreeInRow(board) != False):
        return "Other Player"
    else:
        return "Not Ended"            

#end of game chekc funtion
def check3():
    global playing
    #checking if the borard is full
    if Full(board):
        print("it is a draw End of Game!! thanks for playing")
        playing = False
    
    # straight middle row
    if board[4] == board[5] and board[5] == board[6]:
        print(player, "wins")
        playing = False
    # straight top row
    elif board[7] == board[8] and board[8] == board[9]:
        print(player, "wins")
        playing = False
    # straight bottom row
    elif board[1] == board[2] and board[2] == board[3]:
        print(player, "wins")
        playing = False

    # diagonal 1
    elif board[7] == board[5] and board[5] == board[3]:
        print(player, "wins")
        playing = False
    # diagonal 2
    elif board[1] == board[5] and board[5] == board[9]:
        print(player, "wins")
        playing = False

    # straight column middle
    elif board[8] == board[5] and board[5] == board[2]:
        print(player, "wins")
        playing = False
    # straight column right
    elif board[7] == board[4] and board[4] == board[1]:
        print(player, "wins")
        playing = False
    # straight column left
    elif board[9] == board[6] and board[6] == board[3]:
        print(player, "wins")
        playing = False
        
#this check if there is winner on board
def check2(board,player):
    # straight middle row
    if ((board[4] == board[5] and board[5] == board[6])        
    # straight top row
    or (board[7] == board[8] and board[8] == board[9])        
    # straight bottom row
    or (board[1] == board[2] and board[2] == board[3])
    # diagonal 1
    or (board[7] == board[5] and board[5] == board[3])
    # diagonal 2
    or (board[1] == board[5] and board[5] == board[9])        
    # straight column middle
    or( board[8] == board[5] and board[5] == board[2])        
    # straight column right
    or (board[7] == board[4] and board[4] == board[1])        
    # straight column left
    or (board[9] == board[6] and board[6] == board[3])):
        return True
    else:
        return False
        

#function to check if the board has come to and ending state
def check(board, player):
    global playing
    #checking if the borard is full
    if Full(board) and (ThreeInRow(board) == False):
        print("it is a draw End of Game!! thanks for playing")
        playing = False
    if check2(board,player):
        print(player, "wins")
        playing = False






#make screenclearing function
def Clear_screen():
    #print("     \n"*100)
    Cls = lambda: os.system('cls')
    Cls()
#make the main menue
def MainGame():
    global playing
    while True:
        playing = True
        sleep(1)
        Clear_screen()
        print("""
                         Weclome to tick tac toe!
                   Pick which level you would like to play:

                             0) Level 0 - Two-player
                             1) Level 1 - Easy
                             2) Level 2 - Medium
                             3) Level 3 - Hard
                             4) Level 4 - Really Hard(ish)

            Enter number 1 to 4 to pick the level you would liek to play
                    or enter "exit" to leave the game\n
                                         """)
        menuchoice = input("").upper()
        if menuchoice == "0":
            Level0()
        elif menuchoice == "1":
            Level1()
        elif menuchoice == "2":
            Level2()
        elif menuchoice == "3":
            Level3()
        elif menuchoice == "4":
            Level4()
        elif menuchoice == "EXIT":
            print("thank you for playing the game hope you enjoyed it!!")
            exit()
        else:
            print("you have entered an invaild choice!\nPlease enter a number between 1 and 4 or enter exit to leave the game.")

#make level 0
def Level0():
    global board
    global rounds
    global playing
    playing = True
    #calling the main funtions of the code 
    welcome0()
    #while loop to keep the game going
    while playing:
        PlayerMove0()
    board = ["Ignore me!", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    rounds = 0
    MainGame()
    
#make level 1
def Level1():
    global board
    global rounds
    global playing
    playing = True
    welcome1()
    while playing:
        FirstMove1(choice)
    board = ["Ignore me!", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    rounds = 0
    MainGame()
	
#make level 2
def Level2():
    global rounds
    global board
    global player
    welcome2() #displayes welcome message
    while playing:
        FirstMove2(choice)
    board = ["Ignore me!", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    rounds = 0
    MainGame()

#make level 3
def Level3():
    global rounds
    global board
    global player
    welcome3() #displayes welcome message
    while playing:
        FirstMove3(choice)
    board = ["Ignore me!", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    rounds = 0
    MainGame()

#make level 4
def Level4():
    global rounds
    global board
    global player
    welcome4() #displayes welcome message
    while playing:
        FirstMove4(choice)
    board = ["Ignore me!", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    rounds = 0
    MainGame()

MainGame()



