from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    u, v = map(int,input().split())
    isVisited = [[False]*2 for _ in range(u + 1)]
    dic = defaultdict(list)

    for _ in range(v):
        start, end = map(int, input().split())
        dic[start].append(end)
        dic[end].append(start)

    for key in dic.keys():
        dic[key].sort()

    ok = True

    for start_node in range(1, u + 1):
        if isVisited[start_node][0] or isVisited[start_node][1]: continue

        q = deque()
        isVisited[start_node][0] = True
        q.append((start_node, 0))

        while q and ok:
            cur, state = q.popleft()

            for next_node in dic[cur]:
                if isVisited[next_node][state]:
                    ok = False
                    break

                if not isVisited[next_node][not state]:
                    isVisited[next_node][not state] = True
                    q.append((next_node, not state))
        if not ok:
            break
    print("YES" if ok else "NO")

