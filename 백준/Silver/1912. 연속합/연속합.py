n = int(input())
lst = list(map(int, input().split()))

cur = lst[0]
max_sum = lst[0]

for i in range(1, n):
    cur = max(lst[i], cur + lst[i])
    max_sum = max(max_sum, cur)

print(max_sum)