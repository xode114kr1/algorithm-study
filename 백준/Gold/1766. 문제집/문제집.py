import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m = map(int, input().split())

dic = defaultdict(list)
degree = [0] * (n + 1)
ans = []

for _ in range(m):
    start, end = map(int, input().split())
    dic[start].append(end)
    degree[end] += 1

q = []
for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)

while q:
    cur = min(q)
    ans.append(cur)
    q.remove(cur)
    for next_node in dic[cur]:
        degree[next_node] -= 1
        if degree[next_node] == 0:
            q.append(next_node)
print(*ans)