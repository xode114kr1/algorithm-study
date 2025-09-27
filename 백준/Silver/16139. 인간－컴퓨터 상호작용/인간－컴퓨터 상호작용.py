import sys
input = sys.stdin.readline

s = input().strip()
n = int(input())

mat = [[0] * (len(s) + 1) for _ in range(26)]

for i in range(1, len(s) + 1):
    ch_idx = ord(s[i - 1]) - ord('a')
    for k in range(26):
        mat[k][i] = mat[k][i - 1]
    mat[ch_idx][i] += 1

for _ in range(n):
    c, st, en = input().split()
    st, en = int(st), int(en)
    idx = ord(c) - ord('a')
    print(mat[idx][en + 1] - mat[idx][st])
