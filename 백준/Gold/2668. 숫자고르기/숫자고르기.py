def dfs(st, cur, cnt, route):
    isVisited[cur] = True
    nxt = lst[cur]
    if st == nxt:
        for r in route:
            s.add(r)
        return cnt
    if isVisited[nxt]:
        return 0
    return dfs(st, nxt, cnt + 1, route[:] + [nxt])

n = int(input())
lst = [0] + [int(input()) for _ in range(n)]
s = set()

for idx in range(1, n + 1):
    isVisited = [False] * (n + 1)
    dfs(idx, idx, 1, [idx])
ans = list(s)
ans.sort()
print(len(s))
for i in ans:
    print(i)