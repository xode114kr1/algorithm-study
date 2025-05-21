n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
com = [[(2, 1), (3, 1)], [(1, 2), (3, 2)], [(1, 3), (2, 3)]]

before = mat[0].copy()
for i in range(1, n):
    a = mat[i][0] + min(before[1], before[2])
    b = mat[i][1] + min(before[0], before[2])
    c = mat[i][2] + min(before[0], before[1])
    before = [a,b,c]
print(min(before))
