s1 = input()
s2 = input()
# s1의 i번 s2의j번까지 비교했을 때 최대 공통 뭐시기
dp = [[""] * (len(s2) + 1) for _ in range(len(s1) + 1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
        else:
            c1 = dp[i - 1][j]
            c2 = dp[i][j - 1]
            if len(c1) > len(c2):
                dp[i][j] = c1
            else:
                dp[i][j] = c2
max_cnt = 0
ans = ''
for row in dp:
    for cell in row:
        if max_cnt < len(cell):
            max_cnt = len(cell)
            ans = cell
print(max_cnt)
print(ans)