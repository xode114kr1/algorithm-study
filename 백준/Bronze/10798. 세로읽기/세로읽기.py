mat = [[-1] * 15 for _ in range(5)]

for row in range(5):
    st = input()
    for col in range(len(st)):
        mat[row][col] = st[col]

for col in range(15):
    for row in range(5):
        if mat[row][col] != -1:
            print(mat[row][col], end="")
