def solution(n, s):
    if n > s:
        return [-1]
    d = s // n
    
    plus_cnt = s % n
    av_cnt = n - plus_cnt
    
    
    
    
    ans = [d] * av_cnt + [d + 1] * plus_cnt
    return ans