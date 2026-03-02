def solution(play_time, adv_time, logs):
    def str_to_time(st):
        h, m, s = map(int, st.split(":"))
        return h * 60 * 60 + m * 60 + s
        
    def time_to_str(time):
        h, m, s = time // 3600, (time % 3600) // 60, time % 60
        print(h, m, s)
        h = ("00" + str(h))[-2:]
        m = ("00" + str(m))[-2:]
        s = ("00" + str(s))[-2:]
        return h + ":" + m + ":" + s
        
    prefix = [0] * (str_to_time(play_time) + 1)
    lst = []
    for log in logs:
        s_time, e_time = log.split("-")
        lst.append([str_to_time(s_time), str_to_time(e_time)])
    
    for s, e in lst:
        prefix[s] += 1
        prefix[e] -= 1
    
    for i in range(len(prefix) - 1):
        prefix[i + 1] += prefix[i]
    
    slide_len = str_to_time(adv_time)
    max_pre = sum(prefix[:slide_len])
    pre = sum(prefix[:slide_len])
    ans = 0
    for i in range(1, len(prefix) - slide_len + 1):
        pre -= prefix[i - 1]
        pre += prefix[i + slide_len - 1]
        if pre > max_pre:
            max_pre = pre
            ans = i
    
    return time_to_str(ans)

    
        
        
        
        
        
        
        
        
        
