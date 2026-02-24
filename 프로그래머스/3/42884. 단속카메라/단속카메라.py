def solution(routes):
    cnt = 0
    cur = float('-inf')
    routes.sort(key = lambda x : x[1])
    for s, e in routes:
        if cur < s:
            cnt += 1
            cur = e
    return cnt