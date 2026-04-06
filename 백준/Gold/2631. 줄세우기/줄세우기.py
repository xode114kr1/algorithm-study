n = int(input())
lst = [int(input()) for _ in range(n)]
dp = [1] * n
for i in range(n):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))