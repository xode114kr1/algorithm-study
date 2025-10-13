import sys
input = sys.stdin.readline

n, m = map(int,input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]
for row in range(1, n + 1):
    s = 0
    for col in range(1, n + 1):
        s += mat[row - 1][col - 1]
        prefix_sum[row][col] = s


for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    ans = 0
    for row in range(x1, x2 + 1):

        ans += prefix_sum[row][y2] - prefix_sum[row][y1 - 1]

    print(ans)