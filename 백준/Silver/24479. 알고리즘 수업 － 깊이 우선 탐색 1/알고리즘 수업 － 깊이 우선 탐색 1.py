from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
dic = defaultdict(list)
visited = [False] * (n + 1)
order = [0] * (n + 1)
cnt = 1
def dfs(cur):
    global cnt
    visited[cur] = True
    order[cur] = cnt
    cnt += 1
    for node in dic[cur]:
        if visited[node]: continue
        dfs(node)

for _ in range(m):
    n1, n2 = map(int, input().split())
    dic[n1].append(n2)
    dic[n2].append(n1)
for i in range(1, n + 1):
    dic[i].sort()

dfs(r)
print('\n'.join(map(str, order[1:])))