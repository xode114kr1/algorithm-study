n, m = map(int, input().split())
mat1 = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
mat2 = [list(map(int, input().split())) for _ in range(m)]

ans = [[0] * k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for z in range(m):
            ans[i][j] += mat1[i][z] * mat2[z][j]
for i in range(n):
    print(*ans[i])
# print(*ans)