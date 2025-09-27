s = input()
n = int(input())

mat = [[0] * (len(s) + 1) for _ in range(26)]

for i in range(1, len(s) + 1):
    ch_idx = ord(s[i - 1]) - ord('a')
    mat[ch_idx][i] += 1
    for j in range(i, len(s) + 1):
        mat[ch_idx][j] = mat[ch_idx][i]

for _ in range(n):
    c, st, en = input().split()
    st, en = int(st), int(en)
    print(mat[ord(c) - ord('a')][en + 1] - mat[ord(c) - ord('a')][st])

