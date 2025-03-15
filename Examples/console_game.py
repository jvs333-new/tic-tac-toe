from console_extra import console
import time
import tic_tac_toe_engine as engine

DEVMOD = False
TITLE = "\033[42mTIC-TAC-TOE\033[0m"
width = 80
console = console(width)

def print_board(board:list):
    print(f"     C O L\n     0 1 2\nR 0 |{board[0][0]}|{board[0][1]}|{board[0][2]}|\nO 1 |{board[1][0]}|{board[1][1]}|{board[1][2]}|\nW 2 |{board[2][0]}|{board[2][1]}|{board[2][2]}|\n")

def check_winner(board, ai=False):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            winned = row[0]
            if not ai:
                for i in range(3): row[i] = "\033[41m"+winned+"\033[0m"
            return winned
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            winned = board[0][col]
            if not ai:
                for i in range(3): board[i][col] = "\033[41m"+winned+"\033[0m"
            return winned
    if board[0][0] == board[1][1] == board[2][2] != " ":
        winned = board[0][0]
        if not ai:
            for i in range(3): board[i][i] = "\033[41m"+winned+"\033[0m"
        return winned
    if board[0][2] == board[1][1] == board[2][0] != " ":
        winned = board[0][2]
        if not ai:
            y = 3
            for i in range(3):
                y-=1
                board[i][y] = "\033[41m"+winned+"\033[0m"
        return winned
    return None

def handel_winner(board, mode, ai=None):
    winner = check_winner(board)
    if winner:
        console.clear("\033[41mGAME OVER:\033[0m")
        print_board(board)
        input(f"{"Ai wins!" if mode == "ai" and winner == ai else f"{winner} wins!" if mode == "friend" else "You win!"}\nPress ENTER to continue.")
        return True
    elif engine.is_board_full(board):
        console.clear("\033[41mGAME OVER:\033[0m")
        print_board(board)
        input("It's a draw!\nPress ENTER to continue.")
        return True
    return False

def player_turn(board, player, mode=""):
    console.clear(TITLE)
    print_board(board)
    print(f"{"your" if mode == "ai" else player} turn!")
    print("   r,c")

    try:
        row, col = map(int, input(">>>").split(","))
        if board[row][col] != " ":
            console.clear("\033[41mERROR:\033[0m")
            input("The field you selected is already filled in, please try again.")
            return True
    except (ValueError, IndexError):
        console.clear("\033[41mERROR:\033[0m")
        input("Enter a valid value (row, column).")
        return True

    board[row][col] = player

def ai_turn(board, ai, player):
    turn = engine.best_move(board, ai, player)
    board[turn[0]][turn[1]] = "\033[42m"+ai+"\033[0m"

    console.clear(TITLE)
    print_board(board)
    print("AI's turn:")
    print("   r,c")
    input(f">>>{turn[0]},{turn[1]}\nPress ENTER to continue.")
    board[turn[0]][turn[1]] = ai

def begin():
    print("loading...")
    time.sleep(1)

    if console.question(TITLE, "Type 'start' to start!\nFor rules type 'rules'", "start", "rules") == 2:
            console.clear("TIC-TAC-TOE RULES")
            text = ["The game is played on a grid that's 3 squares by 3 squares.", "Someone is X someone else is O.", "Players take turns putting their marks in empty squares.", "The first player to get 3 of her marks in a row", "(up, down, across, or diagonally) is the winner."]
            for line in text: print(f"{line:^{width}}")
            input(f"\n{'Press ENTER to continue.':^{width}}")

    while True:
        mode = "ai" if console.question(TITLE, "Select a game mode: (Computer/Friend)", "computer", "friend") == 1 else "friend"

        if console.question(TITLE, f"Are you sure you want to play with {mode}? (Y/N)", "y", "n") == 1:
            break

    if mode == "ai":
        while True:
            ox = console.question(TITLE, "Do you want to be X or O?", "x", "o")

            player = {1:"X", 2:"O"}[ox]
            ai = {1:"O", 2:"X"}[ox]

            if console.question(TITLE, f"Are you sure you want to be {player}? (Y/N)", "y", "n") == 1:
                break

    else: player, ai = None, None

    mainloop(player, ai, mode)

def mainloop(player=None, ai=None, mode=None):
    board = [[" "for _ in range(3)]for _ in range(3)]
    if mode == "friend":
        while True:
            if player_turn(board, "x"): continue
            if handel_winner(board, mode, ai): break
            if player_turn(board, "o"): continue
            if handel_winner(board, mode, ai): break
    else:
        while True:
            if player == "X":
                if player_turn(board, player, mode): continue
                if handel_winner(board, mode, ai): break
                ai_turn(board, ai, player)
                if handel_winner(board, mode, ai): break
            else:
                ai_turn(board, ai, player)
                if handel_winner(board, mode, ai): break
                while True:
                    if not player_turn(board, player, mode): break
                if handel_winner(board, mode, ai): break

if __name__ == "__main__":
    if DEVMOD :
        player = "O"
        ai = "X"
        mainloop(player, ai, "ai")
    else: begin()
