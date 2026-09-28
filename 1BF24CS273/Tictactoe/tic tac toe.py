
board = [' ' for _ in range(9)]

player_name = input("Enter your name: ")

def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(b, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]
    return any(all(b[i] == player for i in cond) for cond in win_conditions)

def is_full(b):
    return ' ' not in b

def minimax(b, is_maximizing):
    if check_winner(b, 'O'):
        return 1
    if check_winner(b, 'X'):
        return -1
    if is_full(b):
        return 0

    if is_maximizing:
        best_score = -float('inf')

        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, False)
                b[i] = ' '
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = float('inf')

        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, True)
                b[i] = ' '
                best_score = min(score, best_score)

        return best_score

def ai_move(b):
    best_score = -float('inf')
    move = None

    for i in range(9):
        if b[i] == ' ':
            b[i] = 'O'
            score = minimax(b, False)
            b[i] = ' '

            if score > best_score:
                best_score = score
                move = i

    b[move] = 'O'


# Game Loop
print(f"Welcome, {player_name}!")
print(f"{player_name} is X, AI is O.")
print_board(board)

while True:

    # Human Move
    try:
        pos = int(input(f"{player_name}, enter move position (0-8): "))

        if pos < 0 or pos > 8:
            print("Invalid position! Enter a number from 0 to 8.")
            continue

        if board[pos] == ' ':
            board[pos] = 'X'
        else:
            print("Invalid move! Try again.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    if check_winner(board, 'X'):
        print_board(board)
        print(f"Congratulations {player_name}, you win!")
        break

    if is_full(board):
        print_board(board)
        print("It's a tie!")
        break

    # AI Move
    ai_move(board)
    print("AI played:")
    print_board(board)

    if check_winner(board, 'O'):
        print(f"AI wins! Better luck next time, {player_name}.")
        break

    if is_full(board):
        print("It's a tie!")
        break
