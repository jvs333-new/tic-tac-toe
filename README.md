# Tic Tac Toe

This is a simple `Tic Tac Toe` game written in Python. It includes an engine that uses the minimax algorithm to calculate the best move for the AI.

## File Overview

### `tic_tac_toe_engine.py`

This script contains the logic for the `Tic Tac Toe` game, including functions to check for a winner, determine if the board is full, and calculate the best move using the minimax algorithm.

#### Functions

- `is_board_full(board)`: Checks if the board is full.
- `check_winner(board, ai=False)`: Checks if there is a winner.
- `minimax(board, depth, is_maximizing, player, ai)`: Implements the minimax algorithm to calculate the best move.
- `best_move(board, ai, player)`: Calculates the best move for the AI.

## Usage

To play the game or use the functions, import the `tic_tac_toe_engine.py` module and call the desired functions.

Example:
```python
from TicTacToe import tic_tac_toe_engine

# Initial board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Players
player = "X"
ai = "O"

# Determine the best move for the AI
move = tic_tac_toe_engine.best_move(board, ai, player)
print(f"The best move for the AI is: {move}")
