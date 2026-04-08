import sys
sys.setrecursionlimit(10**6)

def dfs(cx, cy): # cx, cy에서 갈 수 있는 값 반환
    if cx == n - 1 and cy == m - 1:
        return 1

    if dp[cx][cy] != -1:
        return dp[cx][cy]

    dp[cx][cy] = 0

    for dx, dy in direction:
        nx, ny = cx + dx, cy + dy
        if not(0 <= nx < n) or not(0 <= ny < m):
            continue

        if mat[nx][ny] < mat[cx][cy]:
            dp[cx][cy] += dfs(nx, ny)

    return dp[cx][cy]

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
print(dfs(0, 0))

