import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
s = int(input())

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))

dist = [float("inf")] * (v + 1)
dist[s] = 0
pq = [(0, s)]

while pq:
    cur_dist, cur_node = heapq.heappop(pq)

    if cur_dist > dist[cur_node]:
        continue

    for next_node, weight in graph[cur_node]:
        d = cur_dist + weight

        if d < dist[next_node]:
            dist[next_node] = d
            heapq.heappush(pq, (d, next_node))

for w in dist[1:]:
    if w == float('inf'):
        print("INF")
    else: print(w)