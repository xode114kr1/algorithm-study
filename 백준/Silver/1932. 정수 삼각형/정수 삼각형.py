n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            mat[i][j] += mat[i - 1][j]
        elif j == i:
            mat[i][j] += mat[i - 1][j - 1]
        else:
            mat[i][j] += max(mat[i - 1][j], mat[i - 1][j - 1])
print(max(mat[n - 1]))