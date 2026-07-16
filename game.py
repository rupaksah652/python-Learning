board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])

print("Tic Tac Toe Game")

player = "X"

for i in range(9):
    print_board()

    pos = int(input("Enter position (1-9): ")) - 1

    if board[pos] == " ":
        board[pos] = player
    else:
        print("Already filled, try again")
        continue

    # check winner (only rows for simplicity)
    if (board[0] == board[1] == board[2] != " " or
        board[3] == board[4] == board[5] != " " or
        board[6] == board[7] == board[8] != " "):
        print_board()
        print(player, "wins!")
        break

    # switch player
    if player == "X":
        player = "O"
    else:
        player = "X"

else:
    print_board()
    print("It's a draw")