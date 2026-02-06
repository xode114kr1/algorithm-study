def solution(n):
    board = [[0] * n for _ in range(n)]
    
    x, y = -1, 0
    cnt = 1
    
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
    
            board[x][y] = cnt        
            cnt += 1
    ans = []
    for i in range(n):
        for j in range(i + 1):
            ans.append(board[i][j])
    return ans