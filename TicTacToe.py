import random
from colorama import Fore, Style
from colorama import init
init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == "X":

            return Fore.RED + cell + Style.RESET_ALL
        elif cell == "O":
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.WHITE + cell + Style.RESET_ALL
    print(' ' + colored(board[0]) + '|' + colored(board[1]) + '|' + colored(board[2]))
    print(' ' + colored(board[3]) + '|' + colored(board[4]) + '|' + colored(board[5]))
    print(' ' + colored(board[6]) + '|' + colored(board[7]) + '|' + colored(board[8]))
    print()

def player_choice():
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(Fore.YELLOW + "Choose your symbol (X or O): ").upper()
        if symbol == 'X':
            return ('X', 'O')
        elif symbol == 'O':
            return ('O', 'X')

def player_move(board, symbol):
    move = -1
    while move not in range(1, 10) or not board[move - 1].isdigit(): 
        try:
            move = int(input(Fore.YELLOW + "Enter your move (1-9): "))
            if move not in range(1, 10):
                print(Fore.RED + "Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number between 1 and 9.")
    board[move - 1] = symbol
    
def ai_move(board,ai_symbol, player_symbol):
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board[i] = ai_symbol
            if check_winner(board_copy, ai_symbol):
                board[i] = ai_symbol
                return
    possible_moves = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(possible_moves)
    board[move] = ai_symbol

def check_winner(board, symbol):
    win_conditions=[(0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == symbol and board[condition[1]] == symbol and board[condition[2]] == symbol:
            return True
    return False
def check_full(board):
    return all(cell in ['X', 'O'] for cell in board)
def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    print("You are playing against an AI.")
    board = [str(i) for i in range(1, 10)]
    player_symbol, ai_symbol = player_choice()
    current_player = 'Player'
    display_board(board)
    game_on = True
    
    while game_on:
        if current_player == 'Player':
            player_move(board, player_symbol)
            if check_winner(board, player_symbol):
                display_board(board)
                print(Fore.GREEN + "Congratulations! You win!")
                break
            current_player = 'AI'
        else:
            ai_move(board, ai_symbol, player_symbol)
            if check_winner(board, ai_symbol):
                display_board(board)
                print(Fore.RED + "AI wins!")
                break
            current_player = 'Player'
        
        display_board(board)
        if check_full(board):
            print(Fore.YELLOW + "It's a draw!")
            break
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print(Fore.CYAN + "Thanks for playing!")
            break
if __name__ == "__main__":
    tic_tac_toe()