def solution(diffs, times, limit):
    def cal_time(level):
        cnt = 0
        for i in range(len_times):
            if diffs[i] <= level:
                cnt += times[i]
            else:
                gap =  diffs[i] - level
                cnt += gap * wrong_times[i] + times[i]
            if cnt > limit: return cnt
        return cnt

    len_times = len(times)
    wrong_times = [0] * len_times
    for i in range(len_times):
        if i == 0:
            wrong_times[i] = times[i]
        else:
            wrong_times[i] = times[i] + times[i - 1]


    l = min(diffs)
    r = max(diffs)
    while l < r:
        mid = (l + r) // 2
        c = cal_time(mid)
        print(mid, c)
        if c > limit:
            l = mid + 1
        elif c < limit:
            r = mid
        else:
            l = mid
            break
    return l