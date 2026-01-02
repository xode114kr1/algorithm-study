def solution(n, m, section):
    cnt = 0
    idx = 0
    for i in section: 
        if i >= idx:
            idx = i
            idx += m
            cnt += 1
    return cnt