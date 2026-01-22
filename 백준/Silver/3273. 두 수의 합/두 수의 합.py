n = int(input())
lst = list(map(int, input().split()))
x = int(input())

cnt_lst = [0] * 2000000
s = set()
for num in lst:
    cnt_lst[num] += 1
    s.add(num)
ans = 0
for num in s:
    ans += cnt_lst[num] * cnt_lst[x - num]
print(ans // 2)