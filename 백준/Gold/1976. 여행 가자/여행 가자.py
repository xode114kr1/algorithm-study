from collections import deque, defaultdict

def bfs(start):
    rt = set()
    rt.add(start)
    q = deque()
    q.append(start)
    while q:
        cur = q.popleft()
        nxts = graph[cur]
        for nxt in nxts:
            if nxt not in rt:
                q.append(nxt)
                rt.add(nxt)
    return rt


n = int(input())
m = int(input())
graph = defaultdict(list)
for i in range(n):
    tmp = list(map(int, input().split()))
    for j, t in enumerate(tmp):
        if t == 1:
            graph[i + 1].append(j + 1)

route = list(map(int, input().split()))
seen = set(route)

print("YES" if len(seen - bfs(route[0])) == 0 else "NO")

