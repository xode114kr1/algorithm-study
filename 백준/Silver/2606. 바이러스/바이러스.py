def dfs(node):
    if isVisited[node]:
        return
    isVisited[node] = True
    for next_node in node_dict[node]:
        dfs(next_node)

n = int(input())
m = int(input())
node_dict = { x : [] for x in range(1, n + 1)}
isVisited = [False] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    node_dict[x].append(y)
    node_dict[y].append(x)

dfs(1)



print(sum(isVisited) - 1)
