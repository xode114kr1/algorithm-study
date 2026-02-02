def solution(cards):
    def dfs(i, cnt):
        cur = cards[i]
        if isVisited[cur]:
            return cnt
        isVisited[cur] = True
        return dfs(cur, cnt + 1)
    
    n = len(cards)
    isVisited = [False] * n
    for i in range(n):
        cards[i] -= 1
    
    ans = []
    for card in cards:
        if isVisited[card]: continue
        ans.append(dfs(card, 0))
    a = max(ans)
    ans.remove(a)
    if len(ans) == 0: return 0
    b = max(ans)
    return a * b
