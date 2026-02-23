def solution(triangle):
    n = len(triangle)
    dp = [[0] * n for _ in range(n)] 
    dp[0][0] = triangle[0][0]
    for i in range(n):
        for j in range(i + 1):
            cur = triangle[i][j]
            if j == 0: dp[i][j] = dp[i - 1][j] + cur
            elif j == n - 1: dp[i][j] = dp[i - 1][j - 1] + cur
            else: dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + cur
    return max(dp[n - 1])
    