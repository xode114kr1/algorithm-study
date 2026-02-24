from collections import defaultdict, deque

def solution(n, costs):
    def isConnect(a, b):
        dic = defaultdict(list)
        for s, e, c in lst:
            dic[s].append(e)
            dic[e].append(s)
            
        q = deque()
        isVisited = [False] * n
        isVisited[a] = True
        q.append(a)
        
        while q:
            cur = q.popleft()
            nxts = dic[cur]
            if cur == b:
                return True
            for nxt in nxts:
                if not isVisited[nxt]:
                    isVisited[nxt] = True
                    q.append(nxt)
        return False
    
    costs.sort(key = lambda x:x[2])
    lst = []
    for s, e, c in costs:
        if len(lst) == n - 1:break
        if not isConnect(s, e):
            lst.append([s, e, c])
    ans = 0
    for _, _, c in lst:
        ans += c
    return ans
    # lst = [[0, 1, 1], [1, 3, 1], [0, 2, 2]]
    # print(isConnect(1, 2))