##Roles
    #Leader : Devyn
    #Problem Solver : Yuji Wexler
    #Researcher : Hunter
    #Reporter : Lucas

##Libraries
import os



##Variables
one = "1"
two = "2"
three = "3"
four = "4"
five = "5"
six = "6"
seven = "7"
eight = "8"
nine = "9"

playerTurn = "x"
chooseMove = ""

beginningInput = ""


##Intro
def introScreen():
    print("------------------")
    print("Absolute Tic-Tac-Toe\nDeluxe")
    print("------------------")
    print("Write \"Learn\" \nto learn how to play")
    print('Write "Begin" to \nstart the game!')
    print("If you want to see \nthe Absolute Units, \ntype \"Credits\".")
    beginningInput = str(input(">"))


##Puts you to the screen that you want to be in
    if(beginningInput == "Learn"):
        os.system('clear')
        howToPlay()

    if(beginningInput == "Begin"):
        os.system('clear')
        update()

    if(beginningInput == "Credits"):
        os.system('clear')
        credits()

    if(beginningInput == "Press f to pay respects"):
        print("-f-f-f-f-f-f-f-f-f-f-f-f-")


    if(beginningInput != ("Learn" or "Begin" or "Credits" or "Press f to pay respects")):
        print("")
        print("------------------")
        print("I dont understand.\nPlease try again.")
        os.system('clear')
        introScreen()


##How to play
def howToPlay():
    print("------------------")
    print("Absolute Tic-Tac-Toe\nDeluxe")
    print("------------------")
    print("Rules:\nPlayer 1 (x) and player 2 (o) must take turns filling in the grid with their symbol. To place your symbol, type and enter the number of the square you want to place it in on your turn. Once a symbol is placed, it cannot be replaced by another symbol.\n\nGoal:\nFill 3 squares in a row with your symbol to win (vertically, horizontally, or diagonaly). ")
    print("")
    print("")
    print('Type "Return" to go back.\nType "Begin" to begin!')

    beginningInput = str(input(">"))

    if(beginningInput == "Return"):
        os.system('clear')
        introScreen()
    if(beginningInput == "Begin"):
        os.system('clear')
        update()
    if((beginningInput != ("Return" or "Begin"))):
        print("")
        print("------------------")
        print("I dont understand.\nPlease try again.")
        os.system('clear')
        howToPlay()


##Credits
def credits():
    print("")
    print("------------------")
    print("Team leader: Devyn Montanye\nTroubleshooter: Yuji Wexler\nResearcher: Hunter Winfrey\nReporter: Lucas Stokoszynski")

    print("")
    print("An Absolute Unit Production")
    print("------------------")
    print('Type "Return" to go back to the menu.\nType "Begin" to begin!')


    beginningInput = str(input(">"))
    if(beginningInput == "Return"):
        os.system('clear')
        introScreen()
    if(beginningInput == "Begin"):
        os.system('clear')
        update()

    if((beginningInput != ("Return" or "Begin" or "Absolute"))):
        print("")
        print("------------------")
        print("I dont understand.\nPlease try again.")
        os.system('clear')
        howToPlay()




#Updates the Tic Toes Screen
def update():

##Globalization of Variables
    global one
    global two
    global three
    global four
    global five
    global six
    global seven
    global eight
    global nine

    global playerTurn
    global chooseMove

##Tic-Tac-Toe Board
    print("------------------")
    print("Absolute Tic-Tac-Toe\nDeluxe")
    print("------------------")
    print("Press return to go back!")
    print("")
    print("   "+one+" | "+two+" | "+three+"\n  ___|___|___\n   "+four+" | "+five+" | "+six+"\n  ___|___|___\n   "+seven+" | "+eight+" | "+nine+"\n     |   |")
    print("")
    print("It is "+playerTurn+"'s turn")
    print("------------------")

##Check for win

    if((one == "x" and two == "x" and three == "x") or (one == "o" and two == "o" and three == "o")):
        if(playerTurn == "x"):
            playerTurn = "o"
        else:
            playerTurn = "x"
        print (playerTurn + " won! Return to menu? (Type \"Return\")")
        chooseMove = str((input(">")))


    if((four == "x" and five == "x" and six == "x") or (four == "o" and five == "o" and six == "o")):
        if(playerTurn == "x"):
            playerTurn = "o"
        else:
            playerTurn = "x"
        print (playerTurn + " won! Return to menu? (Type \"Return\")")
        chooseMove = str((input(">")))


    if((seven == "x" and eight == "x" and nine == "x") or (seven == "o" and eight == "o" and nine == "o")):
        if(playerTurn == "x"):
            playerTurn = "o"
        else:
            playerTurn = "x"
        print (playerTurn + " won! Return to menu? (Type \"Return\")")
        chooseMove = str((input(">")))


    if((one == "x" and four == "x" and seven == "x") or (one == "o" and four == "o" and seven == "o")):
        if(playerTurn == "x"):
            playerTurn = "o"
        else:
            playerTurn = "x"
        print (playerTurn + " won! Return to menu? (Type \"Return\")")
        chooseMove = str((input(">")))


    if((two == "x" and five == "x" and eight == "x") or (two == "o" and five == "o" and eight == "o")):
        if(playerTurn == "x"):
            playerTurn = "o"
        else:
            playerTurn = "x"
        print (playerTurn + " won! Return to menu? (Type \"Return\")")
        chooseMove = str((input(">")))


    if((three == "x" and six == "x" and nine == "x") or (three == "o" and six == "o" and nine == "o")):
        if(playerTurn == "x"):
            playerTurn = "o"
        else:
            playerTurn = "x"
        print (playerTurn + " won! Return to menu? (Type \"Return\")")
        chooseMove = str((input(">")))


    if((one == "x" and five == "x" and nine == "x") or (one == "o" and five == "o" and nine == "o")):
        if(playerTurn == "x"):
            playerTurn = "o"
        else:
            playerTurn = "x"
        print (playerTurn + " won! Return to menu? (Type \"Return\")")
        chooseMove = str((input(">")))

    if((three == "x" and five == "x" and seven == "x") or (three == "o" and five == "o" and seven == "o")):
        if(playerTurn == "x"):
            playerTurn = "o"
        else:
            playerTurn = "x"
        print (playerTurn + " won! Return to menu? (Type \"Return\")")
        chooseMove = str((input(">")))


##Reset Board
    if(chooseMove == "Return"):
        one = "1"
        two = "2"
        three = "3"
        four = "4"
        five = "5"
        six = "6"
        seven = "7"
        eight = "8"
        nine = "9"

        playerTurn = "x"
        chooseMove = ""

        beginningInput = ""
        playerWon = ""

        os.system('clear')
        introScreen()





##Player chooses where they go
    chooseMove = str((input("Press the number\nthat is your move\n   (player " + playerTurn + ")\n>")))


    if(chooseMove == "1" and one == "1"):
        one = playerTurn
        if(playerTurn == "x"):
            playerTurn = "o"
        else:
            playerTurn = "x"
        os.system('clear')
        update()

    if(chooseMove == "2" and two == "2"):
        two = playerTurn
        if(playerTurn == "x"):
            playerTurn = "o"
        else:
            playerTurn = "x"
        os.system('clear')
        update()

    if(chooseMove == "3" and three == "3"):
        three = playerTurn
        if(playerTurn == "x"):
            playerTurn = "o"
        else:
            playerTurn = "x"
        os.system('clear')
        update()

    if(chooseMove == "4" and four == "4"):
        four = playerTurn
        if(playerTurn == "x"):
            playerTurn = "o"
        else:
            playerTurn = "x"
        os.system('clear')
        update()

    if(chooseMove == "5" and five == "5"):
        five = playerTurn
        if(playerTurn == "x"):
            playerTurn = "o"
        else:
            playerTurn = "x"
        os.system('clear')
        update()

    if(chooseMove == "6" and six == "6"):
        six = playerTurn
        if(playerTurn == "x"):
            playerTurn = "o"
        else:
            playerTurn = "x"
        os.system('clear')
        update()

    if(chooseMove == "7" and seven == "7"):
        seven = playerTurn
        if(playerTurn == "x"):
            playerTurn = "o"
        else:
            playerTurn = "x"
        os.system('clear')
        update()

    if(chooseMove == "8" and eight == "8"):
        eight = playerTurn
        if(playerTurn == "x"):
            playerTurn = "o"
        else:
            playerTurn = "x"
        os.system('clear')
        update()

    if(chooseMove == "9" and nine == "9"):
        nine = playerTurn
        if(playerTurn == "x"):
            playerTurn = "o"
        else:
            playerTurn = "x"
        os.system('clear')
        update()






    #If a incorrrect character is typed
    if(chooseMove != "1", "2", "3", "4", "5", "6", "7", "8", "9", "Return"):

        print("")
        print("")
        print("------------------")
        print("Please type a number\nthat corresponds with\na square between 1 and 9")
    os.system('clear')
    update()


introScreen()
