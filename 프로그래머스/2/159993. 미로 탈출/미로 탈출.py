from collections import deque

def solution(maps):
    def cnt(sx, sy, ex, ey):
        isVisited = [[False] * m for _ in range(n)]
        q = deque()
        isVisited[sx][sy] = True
        q.append([sx, sy, 0])
        while q:
            cx, cy, cnt = q.popleft()
            if cx == ex and cy == ey : return cnt
            for dx, dy in direction:
                nx, ny = cx + dx, cy + dy
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if maps[nx][ny] != "X" and not isVisited[nx][ny]:
                    isVisited[nx][ny] = True
                    q.append([nx, ny, cnt + 1])
                
        return -1
    start = [0, 0]
    goal = [0, 0]
    lever = [0, 0]
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    n = len(maps)
    m = len(maps[0])
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S" : start = [i, j]
            elif maps[i][j] == "E" : goal = [i, j]
            elif maps[i][j] == "L" : lever = [i, j]
    
    toLever = cnt(start[0], start[1], lever[0], lever[1])
    toGoal = cnt(lever[0], lever[1], goal[0], goal[1])
    if toLever == -1 or toGoal == -1:
        return -1
    return toLever + toGoal
        
                