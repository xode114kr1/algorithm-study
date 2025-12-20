t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    ans = 0
    max_sum = lst[-1]
    for k in lst[::-1]:
        if k > max_sum :
            max_sum = k
        else:
            ans += max_sum - k
    print(ans)