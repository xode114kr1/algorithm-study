import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, v = map(int, input().split())
g = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(1, n + 1):
    g[i].sort()

visited = [False] * (n + 1)
dfs_result = []

def dfs(cur: int):
    visited[cur] = True
    dfs_result.append(cur)
    for nxt in g[cur]:
        if not visited[nxt]:
            dfs(nxt)

dfs(v)

visited = [False] * (n + 1)
bfs_result = []
q = deque([v])
visited[v] = True

while q:
    cur = q.popleft()
    bfs_result.append(cur)
    for nxt in g[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append(nxt)

print(*dfs_result)
print(*bfs_result)
