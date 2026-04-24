def solution(n):
    
    dp = []
    dp.append(0)
    dp.append(1)
    dp.append(1)
    if n < 3:
        return dp[n]
    for i in range(2, n):
        dp.append(dp[i] + dp[i - 1])
    return dp[-1] % 1234567