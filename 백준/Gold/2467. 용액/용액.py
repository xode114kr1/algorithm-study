n = int(input())
lst = list(map(int, input().split()))

best = float('inf')
ans1, ans2 = 0, 0
left, right = 0, n - 1

lst.sort()

while left < right:
    s = lst[left] + lst[right]

    if abs(s) < best:
        best = abs(s)
        ans1, ans2 = lst[left], lst[right]

    if s < 0:
        left += 1
    elif s > 0:
        right -= 1
    else:
        break

print(ans1, ans2)
