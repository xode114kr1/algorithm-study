import sys
sys.setrecursionlimit(10 ** 6)

def solution(maps):
    def dfs(x, y):
        total = int(maps[x][y])
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if not isVisited[nx][ny] and maps[nx][ny] != "X":
                isVisited[nx][ny] = True
                total += dfs(nx, ny)
        return total
    n, m = len(maps), len(maps[0])
    isVisited = [[False] * m for _ in range(n)]
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ans = []
    for i in range(n):
        for j in range(m):
            if not isVisited[i][j] and maps[i][j] != "X":
                isVisited[i][j] = True
                ans.append(dfs(i, j))

    return [-1] if len(ans) == 0 else sorted(ans)