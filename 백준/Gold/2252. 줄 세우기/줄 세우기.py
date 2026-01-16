import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n, m = map(int, input().split())

dic = defaultdict(list)
degree = [0] * (n + 1)

for _ in range(m):
    start, end = map(int, input().split())
    dic[start].append(end)
    degree[end] += 1

q = deque()
for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    print(cur, end = " ")

    for next_node in dic[cur]:
        degree[next_node] -= 1
        if degree[next_node] == 0:
            q.append(next_node)

