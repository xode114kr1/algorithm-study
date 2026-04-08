def dfs(x, y, mod): # x, y, mod에서 갈 수 도착할 수 있는 개수를 반환
    if x == n - 1 and y == n - 1:
        return 1
    if dp[x][y][mod] != -1:
        return dp[x][y][mod]

    dp[x][y][mod] = 0

    # mod 0 : 가로, 1 : 세로, 2 : 대각
    match mod:
        case 0:
            if 0 <= y + 1 < n:
                if mat[x][y + 1] == 0:
                    dp[x][y][0] += dfs(x, y + 1, 0)
            if 0 <= x + 1 < n and 0 <= y + 1 < n:
                if mat[x][y + 1] == 0 and mat[x + 1][y] == 0 and mat[x + 1][y + 1] == 0:
                    dp[x][y][0] += dfs(x + 1, y + 1, 2)
        case 1:
            if 0 <= x + 1 < n:
                if mat[x + 1][y] == 0:
                    dp[x][y][1] += dfs(x + 1, y, 1)
            if 0 <= x + 1 < n and 0 <= y + 1 < n:
                if mat[x][y + 1] == 0 and mat[x + 1][y] == 0 and mat[x + 1][y + 1] == 0:
                    dp[x][y][1] += dfs(x + 1, y + 1, 2)
        case 2:
            if 0 <= y + 1 < n:
                if mat[x][y + 1] == 0:
                    dp[x][y][2] += dfs(x, y + 1, 0)
            if 0 <= x + 1 < n:
                if mat[x + 1][y] == 0:
                    dp[x][y][2] += dfs(x + 1, y, 1)
            if 0 <= x + 1 < n and 0 <= y + 1 < n:
                if mat[x][y + 1] == 0 and mat[x + 1][y] == 0 and mat[x + 1][y + 1] == 0:
                    dp[x][y][2] += dfs(x + 1, y + 1, 2)
    return dp[x][y][mod]
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
dp = [[[-1] * 3 for _ in range(n)] for _ in range(n)] # x, y, mod에서 갈 수 있는 개수 dp


print(dfs(0, 1, 0))
