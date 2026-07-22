from game import create_board, display_board, check_winner, is_draw
from minimax import best_move


def play_game():

    board = create_board()

    print("Welcome to Tic-Tac-Toe AI")
    print("You are X and AI is O")

    while True:

        display_board(board)

        move = int(input("Enter your move (1-9): ")) - 1

        if board[move] != " ":
            print("Position already filled!")
            continue

        board[move] = "X"

        if check_winner(board, "X"):
            display_board(board)
            print("You Win!")
            break

        if is_draw(board):
            display_board(board)
            print("Game Draw!")
            break


        print("AI is thinking...")

        ai_move = best_move(board)

        board[ai_move] = "O"


        if check_winner(board, "O"):
            display_board(board)
            print("AI Wins!")
            break

        if is_draw(board):
            display_board(board)
            print("Game Draw!")
            break


play_game()