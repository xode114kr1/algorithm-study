def solution(n, times):
    def can(m):
        cnt = 0
        for t in times:
            cnt += m // t
        return cnt >= n
    
    min_m, max_m = min(times), max(times)
    left, right = min_m * n // len(times), max_m * n // len(times)
    print(left, right)
    while left <= right:
        mid = (left + right) // 2
        
        if can(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left