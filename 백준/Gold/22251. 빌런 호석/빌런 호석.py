# n : 층수 k : 숫자 수 p : 반전 개수 x : 현재 층
N, K, P, X = map(int, input().split())

def make_str(num):
    return str(num).zfill(K)

def can(num):
    cnt = 0
    for n1, n2 in zip(cur, num):
        n1 = int(n1)
        n2 = int(n2)
        cnt += mapping[n1][n2]
        if cnt > P:
            return False
    return True

mapping = [[0, 4, 3, 3, 4, 3, 2, 3, 1, 2], [4, 0, 5, 3, 2, 5, 6, 1, 5, 4], [3, 5, 0, 2, 5, 4, 3, 4, 2, 3], [3, 3, 2, 0, 3, 2, 3, 2, 2, 1], [4, 2, 5, 3, 0, 3, 4, 3, 3, 2], [3, 5, 4, 2, 3, 0, 1, 4, 2, 1], [2, 6, 3, 3, 4, 1, 0, 5, 1, 2], [3, 1, 4, 2, 3, 4, 5, 0, 4, 3], [1, 5, 2, 2, 3, 2, 1, 4, 0, 1], [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]]

cur = make_str(X)
ans = 0
for i in range(1, N + 1):
    str_i = make_str(i)
    if can(str_i):
        ans += 1
print(ans - 1)