def TicTacDraw(board):
    L = len(board)
    for i in range (L):
        n = ''
        for j in range (L):
            if board [i][j] == 0:
                k = 'O'
            if board [i][j] == 1:
                k = 'X'
            if board [i][j] == 2:
                k = ' '
            if j == L-1:
                n = n + k 
            else:
                n = n + k + ' | '
        print (n)
        if i != L - 1:
            print (''.join(['-' for s in range(4*L-1)]))


TicTacDraw([[0,1,2],[2,0,0],[1,1,2]])  
