import random
from colorama import Fore, init, Style
init(autoreset=True)

def display_board(board):
    print()
    def coloured(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    print(' ' + coloured(board[0]) + ' | ' + coloured(board[1]) + ' | ' + coloured(board[2]))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + coloured(board[3]) + ' | ' + coloured(board[4]) + ' | ' + coloured(board[5]))
    print(f"{Fore.CYAN}----------{Style.RESET_ALL}")
    print(' ' + coloured(board[6]) + ' | ' +coloured(board[7]) + ' | ' + coloured(board[8]))
    print()

def player_choice():
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(f"{Fore.GREEN}Do you want to be X or O? {Style.RESET_ALL}").upper()
    if symbol == 'X':
        return('X', 'O')
    else:
        return('O', 'X')
    
def player_move(board, symbol):
    move = -1
    while move not in range(1, 10) or not board[move - 1].isdigit():
        try:
            move = int(input("Enter your move(1-9):"))
            if move not in range(1, 10) or not board[move - 1].isdigit():
                print("Invalid move. Please Try Again.")
        except ValueError:
            print("Please enter a number between 1-9")
    board[move - 1] = symbol

def AI_move(board, AI_symbol, player_symbol):
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = AI_symbol
            if check_win(board_copy, AI_symbol):
                board[i] = AI_symbol
                return
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = player_symbol
            if check_win(board_copy, player_symbol):
                board[i] = AI_symbol
                return
    possible_moves = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(possible_moves)
    board[move] = AI_symbol

def check_win(board, symbol):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # Horizontal
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), # Vertical
                      (0, 4, 8), (2, 4, 6)]            # Diagonal
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == symbol:
            return True
    return False

def check_board(board):
    return all(not spot.isdigit() for spot in board)

def tic_tac_toe():
    print('Welcome to TIC-TAC-TOE!')
    player_name = input(f"{Fore.GREEN}Enter your name: {Style.RESET_ALL}")
    while True:
        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        player_symbol, AI_symbol = player_choice()
        turn = "Player"
        game_on = True

        while game_on:
            display_board(board)
            if turn == 'Player':
                player_move(board, player_symbol)
                if check_win(board, player_symbol):
                    display_board(board)
                    print(f"Congrats! {player_name} you have won the game!")
                    game_on = False
                else:
                    if check_board(board):
                        display_board(board)
                        print("It's a tie!")
                        break
                    else:
                        turn = 'AI'
            else:
                AI_move(board, AI_symbol, player_symbol)
                if check_win(board, AI_symbol):
                    display_board(board)
                    print("AI has won the game!")
                    game_on = False
                else:
                    if check_board(board):
                        display_board(board)
                        print("It's a tie!")
                        break
                    else:
                        turn = "Player"
        play_again = input("Do you want to play again(yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    tic_tac_toe()