from collections import deque

def solution(begin, target, words):
    def can(w1, w2):
        diff = 0
        for c1, c2 in zip(w1, w2):
            if c1 != c2: diff += 1
        return diff == 1
    
    n = len(words)
    q = deque()
    q.append((0, begin))
    isVisited = [False] * n
    while q:
        cnt, w = q.popleft()
        if w == target:return cnt
        for idx, word in enumerate(words):
            if can(w, word) and not isVisited[idx]:
                isVisited[idx] = True
                q.append((cnt + 1, word))
    return 0
