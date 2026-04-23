def solution(n):
    cnt = 0
    l, r = 1, 1
    cnt = 0
    prefix = 1
    
    while l <= n:
        if prefix == n:
            cnt += 1
            prefix -= l
            l += 1
        elif prefix < n:
            r += 1
            if r > n:
                break
            prefix += r
        else:
            prefix -= l
            l += 1
    return cnt