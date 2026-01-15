from collections import deque

n, m = map(int, input().split())
isVisited = [[[False]*2 for _ in range(m)] for _ in range(n)]
mat = [list(map(int, list(input()))) for _ in range(n)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

isClear = False

q = deque()
q.append([0, 0, 1, 1])

while q:
    cur = q.popleft()
    cur_x, cur_y = cur[0], cur[1]
    cnt, life = cur[2], cur[3]

    if cur_x == n - 1 and cur_y == m - 1:
        print(cnt)
        exit()

    for dx, dy in direction:
        nx = cur_x + dx
        ny = cur_y + dy

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if mat[nx][ny] == 0 and not isVisited[nx][ny][life]:
            isVisited[nx][ny][life] = True
            q.append([nx, ny, cnt + 1, life])

        if mat[nx][ny] == 1 and life == 1 and not isVisited[nx][ny][0]:
            isVisited[nx][ny][0] = True
            q.append([nx, ny, cnt + 1, 0])

print(-1)