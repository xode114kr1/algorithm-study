import sys
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
dic = defaultdict(list)
isVisited = [False] * (n + 1)
cnt = 1
ans = [0] * (n + 1)


def dfs(cur):
    global cnt
    ans[cur] = cnt
    isVisited[cur] = True

    cnt += 1
    for after in dic[cur]:
        if isVisited[after]: continue
        dfs(after)


for _ in range(m):
    start, end = map(int, input().split())
    dic[start].append(end)
    dic[end].append(start)

for key in dic.keys():
    dic[key].sort(reverse=True)

dfs(r)

print('\n'.join(map(str, ans[1:])))