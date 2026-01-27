def solution(board):
    # 잘못 되었음을 판단해보자
    # O < X가 많으면 잘못됨
    # OOO가 XXX가 동시에 있으면 잘못됨
    # OOO 가 있을 때는 O = X + 1
    # XXX 가 있을 때는 O = X
    win_lists = [[[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]],
                [[0, 0], [1, 0], [2, 0]], [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]],
                [[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]]]
    isOWin = False
    isXWin = False
    oCount = 0
    xCount = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O": oCount += 1
            if board[i][j] == "X": xCount += 1
    for win_list in win_lists:
        cur = board[win_list[0][0]][win_list[0][1]]
        isWin = True
        if cur == "." : continue
        
        for x, y in win_list:
            if board[x][y] != cur:
                isWin = False
                continue
            
        if isWin and cur == "O": 
            isOWin = True
        if isWin and cur == "X": 
            isXWin = True
    
    if isOWin == False and isXWin == False:
        if (oCount == xCount) or (oCount == xCount + 1):
            return 1
        else:
            return 0
    elif isOWin == True and isXWin == False:
        if oCount == xCount + 1:
            return 1
        else:
            return 0
    elif isOWin == False and isXWin == True:
        if oCount == xCount:
            return 1
        else:
            return 0
    else:
        return 0
            
        
        