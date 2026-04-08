n, m = map(int, input().split())
mat = [list(map(int, input())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if mat[i][j] == 1 and i > 0 and j > 0:
            mat[i][j] = min(mat[i - 1][j], mat[i][j - 1], mat[i - 1][j - 1]) + 1
ans = 0
for row in mat:
    for cel in row:
        ans = max(ans, cel)
print(ans * ans)