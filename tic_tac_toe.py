"""_summary_
1 display game board with 9 positions 
2 make sure the board is empty
3 raise error if position already taken
4 display winner if all three in sraight line
5 provide nubers for each cell on the game dashboard
"""
theBoard = {'7':' ','8':' ','9':' ',
            '4':' ','5':' ','6':' ',
            '1':' ','2':' ','3':' ',}

boardKeys = []

for key in theBoard:
    boardKeys.append(key)
    
def display(board):
    print(board['7'] + '|' +board['8'] + '|' +board['9'])
    print('-+-+-')
    print(board['4'] + '|' +board['5'] + '|' +board['6'])
    print('-+-+-')
    print(board['1'] + '|' +board['2'] + '|' +board['3'])
    
def Game():
    turn = 'X'
    count = 'O'
    
    for i in range(10):
        display(theBoard)
        print(f'its turn of {turn} specify the place you want. ')
        
        move = input()
        if theBoard[move] == ' ':
            theBoard[move] = turn
        else:
            print('the position is already filled, please chose another one.')
            continue
        
        if count >= '5':
            #  following the --- format
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                theBoard(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + 'won the game!!')
                break
            
            if theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                theBoard(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + 'won the game!!')
                break
            
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                theBoard(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + 'won the game!!')
                break
            
            #  following the X format
            if theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                display(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + 'won the game!!')
                break
            
            if theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                display(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + ' won the game!!')
                break
            
            #  following | format
            if theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                display(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + 'won the game!!')
                break
            
            if theBoard['7'] == theBoard['4'] == theBoard['1'] != ' ':
                display(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + 'won the game!!')
                break
            
            if theBoard['2'] == theBoard['4'] == theBoard['8'] != ' ':
                display(theBoard)
                print('\nGame Over\n')
                print('Player ' + turn + 'won the game!!')
                break
            
        if count == '9':
            print('\nGame Over\n')
            print('the Game is a Tie')
            
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
    restart = input('Do you want to restart the Game? (Y/N)').lower()
    
    if restart == "y" or restart == 'n':
        for key in boardKeys:
            theBoard[key] == ' '
        Game()
             
if __name__ == '__main__':
    Game()
        