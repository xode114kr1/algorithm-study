n, b = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

def matmul(mat1,mat2):
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += mat1[i][k] * mat2[k][j]
            res[i][j] = res[i][j] % 1000
    return res


def matdiv(mat1, e):
    if e == 1:
        return [[x % 1000 for x in row] for row in mat1]
    half = matdiv(mat1, e // 2)
    res = matmul(half, half)
    if e % 2 == 1:
        res = matmul(res, mat1)
    return res

ans = matdiv(mat, b)
for i in range(n):
    print(*ans[i])