def solution(n, computers):
    def dfs(cur):
        nxt = computers[cur]
        for idx, node in enumerate(nxt):
            if isVisited[idx] or node == 0: continue
            isVisited[idx] = True
            dfs(idx)
        
    dic = {}
    isVisited = [False] * n
    for i in range(n):
        dic[i] = computers[i]
    ans = 0
    for i in range(n):
        if not isVisited[i]:
            isVisited[i] = True
            dfs(i)
            ans += 1
    return ans