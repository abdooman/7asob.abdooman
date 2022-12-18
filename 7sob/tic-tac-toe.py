from unittest import mock


Board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}

def printBoard(board):
    print('----------')
    print(board['7']+ '|' + board['8'] + '|' + board['9'])
    print('-+-+-+-+-+')
    print(board['4']+ '|' + board['5'] + '|' + board['6'])
    print('-+-+-+-+-+')
    print(board['1']+ '|' + board['2'] + '|' + board['3'])
    print('----------')

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(Board)
        print("it's your turn," + turn +".Move to wich place?")
        
        move = input()
        if move not in Board.keys():
            print('Worng choice, please enter number only')
            continue


        if Board[move] == ' ':
            Board[move] = turn
            count += 1
        else:
            print("That place is already filled.\n Move to which place?")
            continue

        if count >= 5:
            if Board['7'] == Board['8'] == Board['9'] != ' ':  # The Top
                printBoard(Board)
                print("\nGame Over.\n")
                print(" ***** " + turn + " won. *****")
                break
            elif  Board['4'] == Board['5'] == Board['6'] != ' ':  # The Middel
                printBoard(Board)
                print("\nGame Over.\n")
                print(" ***** " + turn + " won. *****")
                break
            elif Board['1'] == Board['2'] == Board['3'] != ' ':  # The Bottom
                printBoard(Board)
                print("\nGame Over.\n")
                print(" ***** " + turn + " won. *****")
                break
            elif Board['1'] == Board['4'] == Board['7'] != ' ':  # The left side
                printBoard(Board)
                print("\nGame Over.\n")
                print(" ***** " + turn + " won. *****")
                break
            elif Board['2'] == Board['5'] == Board['8'] != ' ':  # The middel side 
                printBoard(Board)
                print("\nGame Over.\n")
                print(" ***** " + turn + " won. *****")
                break
            elif Board['3'] == Board['6'] == Board['9'] != ' ':  # The right side 
                printBoard(Board)
                print("\nGame Over.\n")
                print(" ***** " + turn + " won. *****")
                break
            elif Board['1'] == Board['5'] == Board['9'] != ' ':  # Diagonal
                printBoard(Board)
                print("\nGame Over.\n")
                print(" ***** " + turn + " won. *****")
                break
            elif Board['7'] == Board['5'] == Board['3'] != ' ':  # Diagonal
                print("\nGame Over.\n")
                print(" ***** " + turn + " won. *****")
                break
            

        if count == 9:
            print("\nGame Over.\n")
            print("it's a Tie!!")


        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

if __name__ == "__main__":
    while True:
        game()
        end = input('press y to playing agin or n to end the game  ')
        if end == 'y':
            continue
        else:
            break

