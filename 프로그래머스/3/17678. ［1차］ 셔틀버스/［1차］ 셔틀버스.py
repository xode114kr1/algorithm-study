import heapq
        
def str_to_time(s):
    h, m = s.split(":")
    h, m = int(h), int(m)
    return 60 * h + m

def time_to_str(ti):
    h, m = ti // 60, ti % 60
    h, m = "00" + str(h), "00" + str(m)
    h, m = h[-2:], m[-2:]
    return h + ":" + m

def solution(n, t, m, timetable):
    def can(cur):
        lst = []
        for tt in times:
            lst.append([tt, 0])
        lst.append([cur, 1])
        lst.sort()
        
        time = str_to_time("09:00")
        idx = 0
        for _ in range(n):
            for _ in range(m):
                if lst[idx][0] <= time:
                    if lst[idx][1] == 1:
                        return True
                    idx += 1
                else:
                    break
            time += t
        return False
                    
        
    times = []
    for time in timetable:
        times.append(str_to_time(time))
    
    left = 0
    right = str_to_time("23:59")
    while left <= right:
        mid = (left + right) // 2
        if can(mid):
            left = mid + 1
        else:
            right = mid - 1
    return time_to_str(right)

