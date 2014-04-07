# -*- coding: utf-8 -*-
from random import randint
from math import floor, ceil
from time import sleep

you = '''
 ▄         ▄       ▄▄▄▄▄▄▄▄▄▄▄       ▄         ▄
▐░▌       ▐░▌     ▐░░░░░░░░░░░▌     ▐░▌       ▐░▌
▐░▌       ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌       ▐░▌
▐░▌       ▐░▌     ▐░▌       ▐░▌     ▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄█░▌     ▐░▌       ▐░▌     ▐░▌       ▐░▌
▐░░░░░░░░░░░▌     ▐░▌       ▐░▌     ▐░▌       ▐░▌
 ▀▀▀▀█░█▀▀▀▀      ▐░▌       ▐░▌     ▐░▌       ▐░▌
     ▐░▌          ▐░▌       ▐░▌     ▐░▌       ▐░▌
     ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌     ▐░█▄▄▄▄▄▄▄█░▌
     ▐░▌          ▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌
      ▀            ▀▀▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀ '''
win = '''
 ▄         ▄       ▄▄▄▄▄▄▄▄▄▄▄       ▄▄        ▄ 
▐░▌       ▐░▌     ▐░░░░░░░░░░░▌     ▐░░▌      ▐░▌
▐░▌       ▐░▌      ▀▀▀▀█░█▀▀▀▀      ▐░▌░▌     ▐░▌
▐░▌       ▐░▌          ▐░▌          ▐░▌▐░▌    ▐░▌
▐░▌   ▄   ▐░▌          ▐░▌          ▐░▌ ▐░▌   ▐░▌
▐░▌  ▐░▌  ▐░▌          ▐░▌          ▐░▌  ▐░▌  ▐░▌
▐░▌ ▐░▌░▌ ▐░▌          ▐░▌          ▐░▌   ▐░▌ ▐░▌
▐░▌▐░▌ ▐░▌▐░▌          ▐░▌          ▐░▌    ▐░▌▐░▌
▐░▌░▌   ▐░▐░▌      ▄▄▄▄█░█▄▄▄▄      ▐░▌     ▐░▐░▌
▐░░▌     ▐░░▌     ▐░░░░░░░░░░░▌     ▐░▌      ▐░░▌
 ▀▀       ▀▀       ▀▀▀▀▀▀▀▀▀▀▀       ▀        ▀▀'''

play = raw_input("Type 'Help' for instructions, or press Enter to play ")

if play == 'Maoman':
    debug = True #Debug removes all pauses so everything's instant, and gives debug info.
else:  
    debug = False

if play.lower() == 'help': #How much instructions could "Battleship" need?
    print '''
This is a single-player game based off the popular board game, "Battleship."

In this game, after picking your difficulty, you will begin trying to guess
where the enemy ship is on the board. With each guess, you fire a shot at
that spot in the ocean.

If it hits a ship, then you start firing near there to find the rest of the
ship. You must hit every "spot" in a ship to sink it.

The difficulty determins the size of the board, how many tries you get, and
how many ships of different sizes are hidden on the board.

When you sink a ship, you are told by name which one you sank. This way you
know you can stop searching nearby for the rest of the ship and move on to
guessing around for the next ship.

Ship names and lengths:
Patrol Boat ------- 2 tiles
Destroyer --------- 3 tiles
Battleship -------- 4 tiles
Aircraft Carrier -- 5 tiles

Once you have sunk every ship, you win!
''' #More than expected, it turns out.

    raw_input("When you have finished reading, press enter to continue. ")

shipNames = ['Patrol Boat', 'Destroyer', 'Battleship', 'Aircraft Carrier']

def randPos(board):
    return randint(0,len(board)-1)

def printBoard(board):
    '''Prints the array of arrays in a clean, pretty format.'''
    print '\n'
    for row in board:
        print ' '.join(row)

def shipSunk(ship):
    '''Takes an int and checks if the ship with that number
       in ocean[] has been sunk. Returns True if it has.'''
    for i in range(0, size):
        for x in ocean[i]:
            if x == str(ship):
                return False
    return True

def playerWon():
    '''Retuns True if the player has sunk every single ship.'''
    temp = 0
    for i in range(0, size):
        done = True
        for x in ocean[i]:
            if x in label:
                done = False
                break
        if done == True:
            temp +=1
        if debug:
            print done
            print temp
        if temp == size:
            print you
            sleep(pause*0.2)
            print win
            sleep(pause*0.2)
            return True
            break

def makeShip(length):
    '''Makes a ship in a random place on the board. Will not overlap ships.'''
    for i in range(1, 10):
        used = False
        for x in range(0, len(board)):
            if str(i) in ocean[x]:
                used = True
        if not used:
            temp = randint(0,1)
            pos = randPos(board)
            start = randint(0, (len(board)-length))
            if temp == 0:
                for x in range(0, length):
                    if ocean[pos][start+x] in label:
                        makeShip(length)
                        used = True
                        break
                if used:
                    return
                    makeShip(length)
                elif not used:
                    for x in range(0, length):
                        ocean[pos][start+x] = str(i)
                    return
            if temp == 1:
                for x in range(0, length):
                    if ocean[start+x][pos] in label:
                        makeShip(length)
                        used = True
                        break
                if used:
                    return
                    makeShip(length)
                elif not used:
                    for x in range(0, length):
                        ocean[start+x][pos] = str(i)
                    return

def replay():
    '''Asks if the player wants to play again and returns True if so.
       Also allows you to toggle debug as you restart the game.'''
    global debug
    if debug:
        again = raw_input("\nAgain? ") 
        if again == 'Maoman':
            debug = False
            return True
        return again
    else:
        again = raw_input("\nWould you like to play again? 'Yes' or 'No' : ")
    if again == 'Maoman':
        debug = True
        return True
    if again.lower() == 'yes' or again.lower() == 'y':
        return True
    elif again.lower() == 'no' or again.lower() == 'n':
        return False
    else:
        print "\nIf you can't type 'Yes' or 'No' then play again anyways!"
        sleep(pause)
        return True

def main():
    
    global pause, board, ocean, label, hit, size
    board = [] #The board the players see
    ocean = [] #The "enemy" board, i.e. the board containing locations of the ships
    sunk  = ''
    turn  = 0
    hit   = 'abcd' #number of characters in hit and label is...
    label = '1234' #...the max number of ships that can be made

    if debug: #When debug is active, you can set the board size and number of turns to anything
        print "\nDebug Active" 
        size  = int(raw_input("\nSize: ")) #There are no checks. You must enter an even int. 
        turns = int(raw_input("\nTurns: ")) #Also must be an int, but it can be odd.
        pause = 0 #This makes everything instantaneous while in debug.
        diff  = int(ceil(0.5*size)) 
    else:
        pause = 1
        sleep(pause*1.5)
        diff = int(floor(float(raw_input("\nChoose your difficulty as a whole number between 1 and 5: "))))
        if diff > 5:
            diff = 5
            print "\nNow that's getting a bit ridiculous. How about 5?"
        if diff < 1:
            diff = 1
            print "\n...We'll go with 1, that's the easiest setting."
        sleep(float(diff)/5)
        size = diff * 2
        turns = ((size**2)/2)+(size/2) #Enough turns to check half the board plus size/2.

    for x in range(size):
        board.append(['.']*size)
        ocean.append(['.']*size)

    for x in range(0, diff): #Makes 1 ship per difficulty up to a limit of 4 ships.
        if x == 4:
            break 
        makeShip(x+2)
        bigShip = x

    sleep(pause*0.5)
    print "\nThe ocean is %s wide and tall." %size
    sleep(pause*1.5)
    if diff == 1:
        print "\nThe only ship is a little Patrol Boat."
        sleep(pause*2)
    elif diff == 2:
        print "\nThere are 2 ships: a Destroyer and a Patrol Boat."
        sleep(pause*2.5)
    else:
        print "\nThere are %s ships ranging from a %s to a little Patrol Boat." % (diff, shipNames[bigShip])
        sleep(pause*3)
    if turns == 1:
        print "\nYou have 1 turn."
    else:
        print "\nYou have %s turns total." %turns
    sleep(pause*1.25)
    
    printBoard(board)
    
    if debug: 
        printBoard(ocean)

    while (turn < turns): #Main game loop
        
        if playerWon():
            print "\nYou sunk every battleship!"
            break
        if turn+1 == turns:
            print "\nThis is your FINAL TURN. Turn number %s." % (turn+1)
            sleep(pause*1)
        else:
            print "\nTurn number %s" % (turn+1)
            sleep(pause*0.5)
        if turn == 0: #A little extra explanation for the very first round.
            gRow = raw_input("\nGuess which row to check, counting from the top: ")
            if gRow == 'Maoman': #Enter "Maoman" to instantly end this game and exit main().
                return           #Can only be done in this first turn. Useful for debugging.
            gCol = raw_input("\nGuess which column to check, counting from the left: ")
        else:
            gRow = raw_input("\nGuess Row: ")
            gCol = raw_input("\nGuess Column: ")
        
        try:
            gRow = int(gRow)-1
            gCol = int(gCol)-1
        except ValueError:
            print "\nYou must enter a whole number between 1 and %s!" %size
            continue
        if gRow < 0 or gRow > len(board)-1 or gCol < 0 or gCol > len(board[0])-1:
            print "\nThat's not even inside the ocean."
            sleep(pause)
            print "\nEnter a number between 1 and %s." % size
            sleep(pause)
            continue #Each "continue" means you won't lose a turn for making a mistake.
        elif board[gRow][gCol] == 'O':
            print "\nYou already hit the battleship there!"
            sleep(pause)
            continue
        elif ocean[gRow][gCol] in label:
            ocean[gRow][gCol] = hit[int(ocean[gRow][gCol])-1]
            board[gRow][gCol] = "O"
            print "\nYou hit my Battleship!"
            sleep(pause*1.5)
        elif board[gRow][gCol] == "x":
            print "\nYou've already checked that spot, there's nothing there."
            sleep(pause)
            continue
        else:
            print "\nYou missed my Battleship!"
            board[gRow][gCol] = "x"
            sleep(pause*0.5)
            
        printBoard(board)
        if debug:
            printBoard(ocean)
        turn += 1

        for x in range(1, diff+1):
            if x == 5:
                break
            if shipSunk(x):
                if str(x) not in sunk:
                    print '\nYou sunk my %s!' % shipNames[x-1]
                    sunk += str(x)
        
        if playerWon():
            print "\nYou sunk every battleship!"
            break
        
    print "\nGame Over!"
    sleep(pause)
    return

main()

while(True): #I don't yet understand the whole __name__ == __main__ thing, so this is my workaround.
    if replay():
        print "\nRestarting..."
        sleep(pause*1.5)
        main()
    else:
        print "\nThank you for playing."
        break

