import sys
from collections import deque

input = sys.stdin.readline

m,n = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

direct = [(-1,0), (0, -1), (1, 0), (0, 1)]
que = deque()
isVisited = [[False] * m for _ in range(n)]
cnt = 0
isAllEven = True
for row in range(n):
    for col in range(m):
        if mat[row][col] == 1:
            que.append((row, col))
        else:
            isAllEven = False

if isAllEven:
    print(0)
    sys.exit()

while que:
    cnt += 1
    old_que = que.copy()
    for x, y in old_que:
        isVisited[x][y] = True
        for dx, dy in direct:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if mat[nx][ny] == -1 or isVisited[nx][ny]:
                continue
            isVisited[nx][ny] = True
            que.append((nx, ny))
        que.popleft()

isSuccess = True
for i in range(n):
    for j in range(m):
        if isVisited[i][j] == False and mat[i][j] == 0:
            isSuccess = False
            break
    if not isSuccess:break
if isSuccess:
    print(cnt - 1)
else:
    print(-1)
