N, S = map(int, input().split())
lst = list(map(int, input().split()))
ans = N + 1

l, r = 0, 0
cur_sum = 0
while 1:
    if cur_sum >= S:
        ans = min(ans, r - l)
        cur_sum -= lst[l]
        l += 1

    elif r == N:
        break
    else:
        cur_sum += lst[r]
        r += 1

if ans == N + 1:
    print(0)
else:
    print(ans)