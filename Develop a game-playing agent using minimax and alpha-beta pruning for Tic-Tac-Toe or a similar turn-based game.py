
import math

board = [' ' for i in range(9)]

def display():
    for i in range(0, 9, 3):
        print('|'.join(board[i:i+3]))
        print("------")

def winner(b):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b1, c in wins:
        if b[a] == b[b1] == b[c] != ' ':
            return b[a]
    return None

# Minimax with Alpha-Beta Pruning
def minimax(b, depth, alpha, beta, maximizing):
    w = winner(b)

    if w == 'X':
        return 10 - depth
    if w == 'O':
        return depth - 10
    if ' ' not in b:
        return 0

    if maximizing:
        best = -math.inf

        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, depth+1,
                                alpha, beta, False)
                b[i] = ' '

                best = max(best, score)
                alpha = max(alpha, best)

                if beta <= alpha:
                    break
        return best

    else:
        best = math.inf

        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, depth+1,
                                alpha, beta, True)
                b[i] = ' '

                best = min(best, score)
                beta = min(beta, best)

                if beta <= alpha:
                    break
        return best

# AI move
def ai_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0,
                            -math.inf, math.inf, False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                move = i

    if move != -1:
        board[move] = 'X'

# Play game
print("Tic Tac Toe")
print("AI = X, Human = O")

while True:
    ai_move()
    display()

    if winner(board) == 'X':
        print("AI Wins!")
        break

    if ' ' not in board:
        print("Draw!")
        break

    pos = int(input("Enter position (0-8): "))

    if pos < 0 or pos > 8 or board[pos] != ' ':
        print("Invalid position! Try again.")
        board[pos if 0 <= pos < 9 else 0] = board[pos if 0 <= pos < 9 else 0]
        continue

    board[pos] = 'O'

    if winner(board) == 'O':
        display()
        print("Human Wins!")
        break
