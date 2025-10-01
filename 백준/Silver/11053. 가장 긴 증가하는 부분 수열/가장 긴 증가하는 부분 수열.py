from collections import defaultdict

n = int(input())
lst = list(map(int, input().split(" ")))

d = defaultdict()
d[1] = lst[0]


for i in range(1, len(lst)):
    key = max([k for k, v in d.items() if v < lst[i]], default=0)
    d[key + 1] = lst[i]
print(max(d.keys()))

