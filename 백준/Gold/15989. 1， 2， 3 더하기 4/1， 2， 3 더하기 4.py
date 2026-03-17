import sys
input = sys.stdin.readline

T = int(input())

max_num = 0
lst = []
for _ in range(T):
    n = int(input())
    lst.append(n)
    max_num = max(n, max_num)

dp = [0] * (max_num + 1)
dp[0] = 1

for num in [1, 2, 3]:
    for i in range(num, max_num + 1):
        dp[i] += dp[i - num]

for i in lst:
    print(dp[i])

