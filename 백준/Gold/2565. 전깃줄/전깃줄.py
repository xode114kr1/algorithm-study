def func(l, n):
    dp = [0] * n
    for i in range(len(l)):
        idx_lst = [idx for idx, v in enumerate(l[:i + 1]) if v < l[i]]
        key = 0
        for idx in idx_lst:
            key = max(key, dp[idx])
        dp[i] = key + 1
    return dp

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

lst.sort()
b_list = [y for x, y in lst]


print(n - max(func(b_list, n)))