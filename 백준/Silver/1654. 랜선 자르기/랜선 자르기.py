import sys
input = sys.stdin.readline

n, k = map(int, input().split())

lst = [int(input()) for _ in range(n)]

s = 1
e = max(lst)
while s < e:
    mid = (s + e + 1) // 2
    cnt = 0
    for num in lst:
        cnt += num // mid
    if cnt >= k:
        s = mid
    elif cnt < k:
        e = mid - 1
print(s)