from collections import deque

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(x, y):
    group = [(x, y)]

    q = deque()
    q.append((x, y))
    isVisited[x][y] = True
    while q:
        cx, cy = q.popleft()
        for dx, dy in direction:
            nx, ny= cx + dx, cy + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if isVisited[nx][ny]:
                continue
            if L <= abs(mat[cx][cy] - mat[nx][ny]) <= R:
                group.append((nx, ny))
                q.append((nx, ny))
                isVisited[nx][ny] = True
    return group

N, L, R = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while 1:
    isVisited = [[False] * N for _ in range(N)]
    groups = []
    for i in range(N):
        for j in range(N):
            if not isVisited[i][j]:
                groups.append(bfs(i, j))

    if len(groups) == N * N:
        break
    for group in groups:
        people = 0
        for x, y in group:
            people += mat[x][y]
        avg = people // len(group)
        for x, y in group:
            mat[x][y] = avg
    ans += 1
print(ans)