# bord game
board = [' ' for x in range(10)]
#פונקציה שמגדירה את הלוח ואת הבורדים
def print_board(board):
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("-----------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("-----------")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
# פונקציה שמגדירה את המצבים בהם שחקן כלשהו מנצח
def is_winner(board, player):
    return (
        (board[1] == player and board[2] == player and board[3] == player) or
        (board[4] == player and board[5] == player and board[6] == player) or
        (board[7] == player and board[8] == player and board[9] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player) or
        (board[3] == player and board[6] == player and board[9] == player) or
        (board[1] == player and board[5] == player and board[9] == player) or
        (board[3] == player and board[5] == player and board[7] == player)
    )
# פונקציה שבודקת אם הלוח מלא כדי שנוכל לסיים את המשחק
def is_board_full(board):
    return ' ' not in board[1:]
# פונקציה שבעזרתה אנחנו מקבלים את הבחירה של השחקן למיקום של התשובה שלו
def get_player_choice(board, player):
    valid_choice = False
    while not valid_choice:
        choice = input("Player " + player + ", choose a position (1-9): ")
        if choice.isdigit() and int(choice) in range(1, 10) and board[int(choice)] == ' ':
            valid_choice = True
        else:
            print("Invalid choice. Please try again.")
    return int(choice)
#פונקציה ראשית שבעצם משחקת את המשחק בעזרת הפונקציות הקודמות
def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    player1 = 'X'
    player2 = 'O'
    current_player = player1

    while not is_board_full(board):
        choice = get_player_choice(board, current_player)
        board[choice] = current_player
        print_board(board)
        if is_winner(board, current_player):
            print("Player " + current_player + " wins!")
            return
        current_player = player2 if current_player == player1 else player1

    print("Tie game!")

play_game()