from array import *

global board, count, game_running, turn_count, player, correct
board = [['*','*','*'], ['*','*','*'], ['*','*','*']]
count = 0
game_running = True
player = 1
running = True
correct = False
turn_count = 0


def print_board():
    print(board[0][0] + "|" + board[0][1] + "|" + board[0][2])
    print("- - -")
    print(board[1][0] + "|" + board[1][1] + "|" + board[1][2])
    print("- - -")
    print(board[2][0] + "|" + board[2][1] + "|" + board[2][2])


def reset_board():
    for i in range(3):
        for j in range(3):
            board[i][j] = "*"

    count = 0
    turn_count = 0
    game_running = True
    player = 1
    correct = False


def player_turn(player_turn):
    if player_turn == 1:
        return "X"
    else:
        return "O"




print("      Hello welcome to The Tic Tac Toe Game!")
print("-------Who will be the Winner in this game-------")
print("-------------------------------------------------")

while running:
    user_start = input("Do you want to start the game? y or n? ")
    if user_start == "n":
        break
    else:
        print("X will start the game off and will be player one!")
        while game_running:
            correct = False
            while not correct:
                user_answer = input("Enter in corrdinates: (example: 1 1 is the top left and 3 3 is the bottom right)")
                try:
                    answer = user_answer.split(' ')
                    row = int(answer[0]) - 1
                    col = int(answer[1]) - 1
                    #print(row)
                    #print(col)
                    #print(row in range(3))
                    if row in range(3):
                        if col in range(3):
                            print("in 2d array")
                            if board[row][col] == "*":
                                print("made it into the equals *")
                                board[row][col] = player_turn(player)
                                print("Should've changed the board")
                                if player == 1:
                                    player = 2
                                else:
                                    player = 1
                                correct = True
                                count = count+1
                            else:
                                print("Try again!")
                        else:
                            print("Try again!")
                    else:
                        print("Try again!")
                except:
                    print("Try again!")
            print_board()