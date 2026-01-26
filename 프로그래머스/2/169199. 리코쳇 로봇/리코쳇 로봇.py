from collections import deque

def solution(board):
    n, m = len(board), len(board[0])

    def streat_go(x, y, dx, dy):
        while 1:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m or board[nx][ny] == "D":
                return [nx - dx, ny - dy]
            x, y = nx, ny

    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    isVisited = [[False] * m for _ in range(n)]
    q = deque()
    ex, ey = 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                isVisited[i][j] = True
                q.append([i, j, 0])
            if board[i][j] == "G":
                ex, ey = i, j
    ans = -1
    while q:
        x, y, cnt = q.popleft()

        if x == ex and y == ey:
            ans = cnt
            break

        for dx, dy in direction:
            nx, ny = streat_go(x, y, dx, dy)
            if not isVisited[nx][ny]:
                isVisited[nx][ny] = True
                q.append([nx, ny, cnt + 1])
    return ans