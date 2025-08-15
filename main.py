import random
from colorama import init, Fore, Style
init(autoreset = True)
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
    print(Fore.CYAN+"---------------------------"+Style.RESET_ALL)
    print(" "+colored(board[3])+"|"+colored(board[4])+"|"+colored(board[5]))
    print(Fore.CYAN+"---------------------------"+Style.RESET_ALL)
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
    move -= 1
    while move not in range(1, 10) or not board[move-1].isdigit():
        try:
            move = int(input("Enter a number between 1 and 9: "))
            if move not in range(1, 10) or not board[move-1].isdigit():
                print("Invalid Move")
        except ValueError:
            print("Please enter a number between 1 and 9.")
    board[move-1] = symbol
def AImove(board, AIsymbol):
    for i in range(9):
        if board[i].isdigit():
            boardcopy = board.copy()
            boardcopy[i] = AIsymbol
            if check_win(boardcopy, AIsymbol):
                board[i] = AIsymbol
                return
    for i in range(9):
        if board[i].isdigit():
            boardcopy = board.copy()
            boardcopy[i] = playersymbol
            if check_win(boardcopy, playersymbol):
                board[i] = AIsymbol
                return
    possible_moves = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(possible_moves)