from collections import defaultdict, deque

def solution(n, results):
    def bfs(cur, dic):
        q = deque()
        cnt = 0
        isVisited = [False] * (n + 1)
        q.append(cur)
        while q:
            c = q.popleft()
            nxts = dic[c]
            for nxt in nxts:
                if isVisited[nxt] : continue
                isVisited[nxt] = True
                q.append(nxt)
                cnt += 1
        return cnt
                
    # 내 뒤에 있는 사람의 수 + 내 앞에 있는 사람의 수 = n - 1이면 알 수 있겠지?
    dic_before = defaultdict(list)
    dic_after = defaultdict(list)
    for a, b in results:
        dic_before[a].append(b)
        dic_after[b].append(a)
    
    ans = 0
    for i in range(1, n + 1):
        if bfs(i, dic_before) + bfs(i, dic_after) == n - 1:
            ans += 1
        
    return ans