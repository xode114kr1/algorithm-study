n = int(input())
lst = [int(input()) for _ in range(n)]

if n == 1:
    print(lst[0])
elif n == 2:
    print(lst[0] + lst[1])
else:
    ans = [0] * n
    ans[0] = lst[0]
    ans[1] = lst[0] + lst[1]
    ans[2] = max(lst[0] + lst[2], lst[1] + lst[2])
    for i in range(3, n):
        ans[i] = max(ans[i - 2] + lst[i], ans[i - 3] + lst[i - 1] + lst[i])
    print(ans[-1])
