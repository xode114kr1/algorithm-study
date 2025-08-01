def cut(mat, x, y, size):
    global white, blue
    isSameColor = True
    cur = mat[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if mat[i][j] != cur:
                isSameColor = False

    if isSameColor:
        if cur == 0:
            white += 1
        else:
            blue += 1
    else:
        cut(mat, x, y, size // 2)
        cut(mat, x + size // 2, y, size // 2)
        cut(mat, x, y + size // 2, size // 2)
        cut(mat, x + size // 2, y + size // 2, size // 2)

white, blue = 0, 0
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
cut(mat, 0, 0, n)
print(white)
print(blue)

