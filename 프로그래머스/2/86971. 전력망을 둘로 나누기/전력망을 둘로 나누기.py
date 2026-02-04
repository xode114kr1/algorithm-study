from collections import deque, defaultdict

def solution(n, wires):
    def bfs(k):
        isVisited = [False] * (n + 1)
        q = deque() # node, cnt
        q.append(k)
        isVisited[k] = True
        cnt = 1
        while q:
            cur = q.popleft()
            last = cur
            c = cnt
            nxt_list = dic[cur]
            for nxt in nxt_list:
                if isVisited[nxt] : continue
                isVisited[nxt] = True
                cnt += 1
                q.append(nxt)
        return abs(n - 2 * cnt)
    
    dic = defaultdict(list)
    for s, e in wires:
        dic[s].append(e)
        dic[e].append(s)
    
    ans = float("inf")
    for wire in wires:
        s, e = wire
        dic[s].remove(e)
        dic[e].remove(s)
        ans = min(ans, bfs(1))
        dic[s].append(e)
        dic[e].append(s)
    return ans
    
    