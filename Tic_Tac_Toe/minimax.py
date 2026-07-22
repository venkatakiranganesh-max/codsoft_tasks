from game import check_winner


def minimax(board, is_ai_turn):

    if check_winner(board, "O"):
        return 1

    if check_winner(board, "X"):
        return -1

    if " " not in board:
        return 0


    if is_ai_turn:
        best_score = -100

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(board, False)

                board[i] = " "

                best_score = max(score, best_score)

        return best_score


    else:
        best_score = 100

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                score = minimax(board, True)

                board[i] = " "

                best_score = min(score, best_score)

        return best_score



def best_move(board):

    best_score = -100
    move = 0

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(board, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move