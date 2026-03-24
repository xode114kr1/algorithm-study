h, w = map(int, input().split())
lst = list(map(int, input().split()))

max_h, min_h = max(lst), min(lst)
ans = 0
for ch in range(min_h, max_h + 1):
    cnt = 0
    left, right = float('inf'), 0
    for idx, n in enumerate(lst):
        if n >= ch:
            left = min(left, idx)
            right = max(right, idx)
            cnt += 1
    ans += right + 1 - cnt - left
print(ans)