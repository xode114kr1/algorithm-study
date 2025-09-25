n, k = map(int, (input().split()))
dp = [[0] * (k + 1) for _ in range(n + 1)]
w_list = []
v_list = []

for _ in range(n):
    w, v = map(int, input().split())
    w_list.append(w)
    v_list.append(v)

for i in range(1, n + 1):
    for j in range(1, k + 1):
        cur_w = w_list[i - 1]
        cur_v = v_list[i - 1]
        if j < cur_w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cur_w] + cur_v)
print(dp[n][k])