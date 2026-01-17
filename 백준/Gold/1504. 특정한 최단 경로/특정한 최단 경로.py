import sys
import heapq
input = sys.stdin.readline


def dijkstra(s_node, e_node):

    dists = [float("inf")] * (n + 1)
    dists[s_node] = 0
    pq = [(0, s_node)]

    while pq:
        cur_weight, cur_node  = heapq.heappop(pq)

        if cur_weight > dists[cur_node]:
            continue

        for next_node, next_weight in graph[cur_node]:
            if next_weight + dists[cur_node] < dists[next_node]:
                dists[next_node] = next_weight + dists[cur_node]
                heapq.heappush(pq, (next_weight + dists[cur_node], next_node))
    return dists[e_node]

n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(e):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

v1, v2 = map(int, input().split())

start_to_v1 = dijkstra(1, v1)
v1_to_v2 = dijkstra(v1, v2)
v2_to_n = dijkstra(v2, n)

start_to_v2 = dijkstra(1, v2)
v1_to_n = dijkstra(v1, n)

path_1 = start_to_v1 + v1_to_v2 + v2_to_n
path_2 = start_to_v2 + v1_to_v2 + v1_to_n


if path_1 == float("inf") and path_2 == float('inf'):print(-1)
else: print(min(path_1, path_2))
    