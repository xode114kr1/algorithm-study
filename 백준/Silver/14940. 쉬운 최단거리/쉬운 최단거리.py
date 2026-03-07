from collections import deque

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

n, m = map(int, input().split())

ans = [[0] * m for _ in range(n)]
isVisited = [[False] * m for _ in range(n)]
mat = [list(map(int, input().split())) for _ in range(n)]

sx, sy = -1, -1
for i in range(n):
    ok = True
    for j in range(m):
        if mat[i][j] == 2:
            ok = False
            sx, sy = i, j
            break
    if not ok:
        break

q = deque()
q.append((sx, sy, 0))
isVisited[sx][sy] = True

while q:
    cx, cy, cnt = q.popleft()
    ans[cx][cy] = cnt

    for dx, dy in direction:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < n and 0 <= ny < m and isVisited[nx][ny] == False and mat[nx][ny] == 1:
            isVisited[nx][ny] = True
            q.append((nx, ny, cnt + 1))

for i in range(n):
    for j in range(m):
        if ans[i][j] == 0 and mat[i][j] != 0:
            ans[i][j] = -1

ans[sx][sy] = 0
for row in ans:
    print(*row)
