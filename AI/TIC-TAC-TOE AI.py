import math

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def is_moves_left(board):
    for row in board:
        if "_" in row:
            return True
    return False

def evaluate(board):
    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] == "X":
                return 10
            elif row[0] == "O":
                return -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == "X":
                return 10
            elif board[0][col] == "O":
                return -10

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            return 10
        elif board[0][0] == "O":
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            return 10
        elif board[0][2] == "O":
            return -10

    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10:
        return score - depth

    if score == -10:
        return score + depth

    if not is_moves_left(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "X"
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = "_"
        return best

    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "O"
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = "_"
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = "X"
                move_val = minimax(board, 0, False)
                board[i][j] = "_"

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def is_game_over(board):
    return evaluate(board) != 0 or not is_moves_left(board)

def play_game():
    board = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
    ]

    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O' and the AI is 'X'.")
    print("lets begin")
    print_board(board)

    while True:
        row = int(input("Enter your move (row 0-2): "))
        col = int(input("Enter your move (col 0-2): "))

        if board[row][col] != "_":
            print("Invalid move! Try again.")
            continue

        board[row][col] = "O"
        print_board(board)

        if is_game_over(board):
            break

        print("AI's move:")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = "X"
        print_board(board)

        if is_game_over(board):
            break

    score = evaluate(board)
    if score == 10:
        print("AI wins!")
    elif score == -10:
        print("You win!")
    else:
        print("It's a tie!")

play_game()
