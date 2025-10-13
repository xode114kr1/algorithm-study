n, m = map(int, input().split())
lst = list(map(int,input().split()))

sum_lst = [0] * m
s = 0
for i, num in enumerate(lst):
    s += num
    sum_lst[s % m] += 1

ans = sum_lst[0]
for i in range(m):
    ans += sum_lst[i] * (sum_lst[i] - 1) // 2
print(ans)