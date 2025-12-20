n, d = map(int, input().split())
shortcuts = [[] for _ in range(d + 1)]
dp = [0] + [float("inf")] * d
for _ in range(n):
    start, end, cost = map(int, input().split())
    if end > d or cost >= end - start: continue
    shortcuts[start].append([end, cost])

for i in range(d):
    dp[i + 1] = min(dp[i + 1], dp[i] + 1)

    for end, cost in shortcuts[i]:
        dp[end] = min(dp[end], dp[i] + cost)
print(dp[-1])