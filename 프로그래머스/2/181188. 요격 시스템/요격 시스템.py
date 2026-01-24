def solution(targets):
    targets.sort(key=lambda x: x[1]) 
    cnt = 0
    last = -1 

    for s, e in targets:

        if last <= s:
            cnt += 1
            last = e
    return cnt
