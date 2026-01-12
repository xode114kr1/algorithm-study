import sys
sys.setrecursionlimit(10**6)

z = int(input())

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(fx, fy):
    isVisited[fx][fy] = True

    for dx, dy in direction:
        nx = fx + dx
        ny = fy + dy
        if nx >= m or ny >= n or nx < 0 or ny < 0:
            continue
        if lst[nx][ny] == 1 and not isVisited[nx][ny]:
            dfs(nx, ny)

for _ in range(z):
    m, n, k = map(int, input().split())
    lst = [[0] * (n + 1) for _ in range(m + 1)]

    isVisited = [[False] * (n + 1) for _ in range(m + 1)]
    ans = 0
    for _ in range(k):
        x, y = map(int, input().split())
        lst[x][y] = 1
    for i in range(m):
        for j in range(n):
            if lst[i][j] == 1 and not isVisited[i][j]:
                dfs(i, j)
                ans += 1
    print(ans)