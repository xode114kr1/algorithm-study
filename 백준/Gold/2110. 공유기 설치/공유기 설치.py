def set_router(d): # d거리로 세팅 가능한지
    last = lst[0]
    cnt = c - 1
    for idx, home in enumerate(lst[1:]):
        if home - last >= d:
            cnt -= 1
            last = home
    if cnt > 0:
        return False
    return True

n, c = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()

left = 1
right = lst[-1] - lst[0]

while left <= right:
    mid = (left + right) // 2

    if set_router(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right)