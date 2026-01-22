def solution(info, n, m):
    size = len(info)
    # dp[i][j] = a, 물건 i고 b의 무게가 j 일때 a의 최소값
    dp = [[float('inf')] * m for _ in range(size + 1)]
    dp[0][0] = 0
    for i in range(size):
        a, b = info[i]
        for j in range(m):
            if dp[i][j] == float('inf'):
                continue

            if dp[i][j] + a < n:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + a)

            if j + b < m:
                dp[i + 1][j + b] = min(dp[i + 1][j + b], dp[i][j])

    ans = min(dp[size])
    return -1 if ans == float('inf') else ans