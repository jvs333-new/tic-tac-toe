def is_board_full(board):
    for row in board:
        for col in row:
            if col == " ":
                return 0
            
    return 1

def check_winner(board, ai=False):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def minimax(board, depth, is_maximizing, player, ai):
    winner = check_winner(board, True)
    if winner == ai:
        return 1
    elif winner == player:
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = ai
                    score = minimax(board, depth + 1, False, player, ai)
                    board[row][col] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = player
                    score = minimax(board, depth + 1, True, player, ai)
                    board[row][col] = " "
                    best_score = min(score, best_score)
        return best_score

def best_move(board, ai, player):
    best_score = -float('inf')
    move = (-1, -1)
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = ai
                score = minimax(board, 0, False, player, ai)
                board[row][col] = " "
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move