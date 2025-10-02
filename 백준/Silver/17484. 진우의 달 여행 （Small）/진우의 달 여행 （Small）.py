n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * m for _ in range(n)] for _ in range(3)]

# 0 : 왼, 1 : 정, 2 : 오

for d in range(3):
    for j in range(m):
        dp[d][0][j] =  mat[0][j]

for i in range(1, n):
    for j in range(m):
        if j == 0:
            dp[0][i][j] = float('inf')
            dp[1][i][j] = min(dp[0][i - 1][j], dp[2][i - 1][j])
            dp[2][i][j] = min(dp[0][i - 1][j + 1], dp[1][i - 1][j + 1])
        elif j == m - 1:
            dp[0][i][j] = min(dp[1][i - 1][j - 1], dp[2][i - 1][j - 1])
            dp[1][i][j] = min(dp[0][i - 1][j], dp[2][i - 1][j])
            dp[2][i][j] = float('inf')
        else:
            dp[0][i][j] = min(dp[1][i - 1][j - 1], dp[2][i - 1][j - 1])
            dp[1][i][j] = min(dp[0][i - 1][j], dp[2][i - 1][j])
            dp[2][i][j] = min(dp[0][i - 1][j + 1], dp[1][i - 1][j + 1])
        for d in range(3):
            dp[d][i][j] += mat[i][j]
print(min(min(dp[0][-1]), min(dp[1][-1]), min(dp[2][-1])))

