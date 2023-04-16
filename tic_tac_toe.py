def printBoard(board):
    print('-------------')
    print('| ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + ' |')
    print('-------------')
    print('| ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2] + ' |')
    print('-------------')
    print('| ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2] + ' |')
    print('-------------')

def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[2][0] == board[1][1] == board[0][2] != ' ':
        return True
    return False
def bestOfThree(score):
    if score.get('X') == 3 or score.get('O') == 3:
        return True

def tic_tac_toe(score):
    board = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
    player = 'X'
    while True:
        printBoard(board)
        row = int(input("Enter in a row number 1-3 for " + player + ": "))-1
        col = int(input("Enter in a col number 1-3 for " + player + ": "))-1
        if board[row][col] != ' ':
            print("This selection is already occupied, please try again!")
            continue
        board[row][col] = player
        if check_win(board):
            printBoard(board)
            print("Congratulations " + player + ", you win this round!")
            score[player]+=1
            print("The score is now " + str(score['X']) + ':' + str(score['O']))
            return (player, score)
            break
        if all([cell != ' ' for row in board for cell in row]):
            printBoard(board)
            print("It's a tie!")
            return (player, score)
            break
        player = 'O' if player == 'X' else 'X'
score = {'X':0, 'O':0}
while True:
    (player, score) = tic_tac_toe(score)
    if bestOfThree(score):
        print("Congratulations player " + player + " you won best out of three with a scoreboard of " + str(score['X']) + ":" + str(score['O']) + "!" )
        break
    