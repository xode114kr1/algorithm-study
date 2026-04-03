n = int(input())
lst = list(map(int, input().split()))
lst.sort()

ans = 0

for i in range(n):
    target = lst[i]
    left, right = 0, n - 1
    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue
        s = lst[left] + lst[right]
        if s == target:
            ans += 1
            break
        elif s < target:
            left += 1
        else:
            right -= 1

print(ans)