from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
mat = [list(map(int, list(input().strip()))) for _ in range(n)]

q = deque()
q.append([0, 0, 1])
isVisited = [[False] * m for _ in range(n)]
isVisited[0][0] = True


while q:
    cur = q.popleft()
    cx, cy, depth = cur[0], cur[1], cur[2]
    if cx == n - 1 and cy == m - 1:
        print(depth)
        break



    for dx, dy in direction:
        nx = dx + cx
        ny = dy + cy
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if mat[nx][ny] == 1 and not isVisited[nx][ny]:
            isVisited[nx][ny] = True
            q.append([nx, ny, depth + 1])