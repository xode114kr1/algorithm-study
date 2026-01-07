n = int(input())
lst = list(map(int, input().split()))

ans = [0] * n

for idx, num in enumerate(lst):
    k = 0
    for j in range(n):
        if ans[j] == 0:
            if k == num:
                ans[j] = idx + 1
                break
            k += 1
print(*ans)
