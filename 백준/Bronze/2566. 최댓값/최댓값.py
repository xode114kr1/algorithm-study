mat = [list(map(int,input().split())) for _ in range(9)]

ans_i, ans_j = 0, 0
ans = mat[0][0]
for i in range(9):
    for j in range(9):
        if ans < mat[i][j]:
            ans_i, ans_j = i, j
            ans = mat[i][j]

print(ans)
print(ans_i + 1, ans_j + 1)