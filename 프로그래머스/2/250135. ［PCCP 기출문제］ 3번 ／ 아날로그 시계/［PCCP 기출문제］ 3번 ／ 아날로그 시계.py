def solution(h1, m1, s1, h2, m2, s2):
    def count_time(time): # 0시 정각부터 time까지의 cnt
        m_count = (59 * time) // 3600
        h_count = (719 * time) // (3600 * 12)
        
        if time >= 3600 * 12:
            return m_count + h_count - 1
        return m_count + h_count
        
    
    start_time = h1 * 60 * 60 + m1 * 60 + s1
    end_time = h2 * 60 * 60 + m2 * 60 + s2
    ans = count_time(end_time) - count_time(start_time)
    if (59 * start_time) % 3600 == 0 or (719 * start_time) % (3600 * 12) == 0: # 겹쳐서 시작이면
        ans += 1
    return ans