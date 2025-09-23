def make_dp(lst, n):
    dp = [0] * n
    for i in range(len(lst)):
        idx_lst = [idx for idx, x in enumerate(lst[:i + 1]) if x < lst[i]]
        key = 0
        for idx in idx_lst:
            if key < dp[idx]:
                key = dp[idx]
        dp[i] = key + 1
    return dp
n = int(input())
lst = list(map(int, input().split(" ")))

dp_inc = make_dp(lst, n)
dp_dec = make_dp(lst[::-1], n)

ans = 0
for i in range(n):
    ans = max(ans, dp_inc[i] + dp_dec[n - 1 - i] - 1)
print(ans)

