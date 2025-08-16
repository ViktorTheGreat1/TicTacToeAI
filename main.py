import random
from colorama import init, Fore, Style
init(autoreset = True)
Winner = ""
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
def displayboard(board):
    print()
    def colored(cell):
        if cell == "X":
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == "O":
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    print(" "+colored(board[0])+"|"+colored(board[1])+"|"+colored(board[2]))
    print(Fore.CYAN+"-------"+Style.RESET_ALL)
    print(" "+colored(board[3])+"|"+colored(board[4])+"|"+colored(board[5]))
    print(Fore.CYAN+"-------"+Style.RESET_ALL)
    print(" "+colored(board[6])+"|"+colored(board[7])+"|"+colored(board[8]))
    print()
def playerchoice():
    symbol=""
    while symbol not in ["X", "O"]:
        symbol = input(Fore.GREEN+"Choose X or O: "+Style.RESET_ALL).upper()
        if symbol == "X":
            return ("X", "O")
        else:
            return ("O", "X")
def playermove(board, symbol):
    move = 0
    while move not in range(1, 10) or not board[move-1].isdigit():
        try:
            move = int(input("Enter a number between 1 and 9: "))
            if move not in range(1, 10) or not board[move-1].isdigit():
                print("Invalid Move")
        except ValueError:
            print("Please enter a number between 1 and 9.")
    board[move-1] = symbol
def check_win(board):
    global Winner
    winning_lists = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    check_scoreX = 0
    check_scoreO = 0
    for list in winning_lists:
        for index in list:
            if board[index] == "X":
                check_scoreX += 1
            elif board[index] == "O":
                check_scoreO += 1
            else:
                continue
        if check_scoreO == 3:
            Winner = "O"
            return "O won"
        elif check_scoreX == 3:
            Winner = "X"
            return "X won"
        else:
            check_scoreX = 0
            check_scoreO = 0
def AImove(board, AIsymbol, playersymbol):
    for i in range(9):
        if board[i].isdigit():
            boardcopy = board.copy()
            boardcopy[i] = AIsymbol
            check_win(boardcopy)
            if  Winner == AIsymbol:
                board[i] = AIsymbol
                return
    for i in range(9):
        if board[i].isdigit():
            boardcopy = board.copy()
            boardcopy[i] = playersymbol
            check_win(boardcopy)
            if  Winner == playersymbol:
                board[i] = AIsymbol
                return
    possible_moves = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(possible_moves)
    board[move] = AIsymbol
def gameplay():
    symbols = playerchoice()
    mysymbol = symbols[0]
    computersymbol = symbols[1]
    displayboard(board)
    while True:
        playermove(board, mysymbol)
        if check_win(board) == "X won" or check_win(board) == "O won":
            if check_win(board) == "X won":
                if mysymbol == "X":
                    displayboard(board)
                    print("Congratulations, Player, you won!")
                else:
                    displayboard(board)
                    print("Computer wins! Better Luck Next Time!")
            elif check_win(board) == "O won":
                if mysymbol == "O":
                    displayboard(board)
                    print("Congratulations, Player, you won!")
                else:
                    displayboard(board)
                    print("Computer wins! Better Luck Next Time!")
            else:
                print("This was a tie, restart the program to try again.")
            break
        AImove(board, computersymbol, mysymbol)
        displayboard(board)
        check_win(board)
        if check_win(board) == "X won" or check_win(board) == "O won":
            if check_win(board) == "X won":
                if mysymbol == "X":
                    print("Congratulations, Player, you won!")
                else:
                    print("Computer wins! Better Luck Next Time!")
            elif check_win(board) == "O won":
                if mysymbol == "O":
                    print("Congratulations, Player, you won!")
                else:
                    print("Computer wins! Better Luck Next Time!")
            else:
                print("This was a tie, restart the program to try again.")
            break
gameplay()