def solution(stones, k):
    def can(num):
        cnt = 0
        for stone in stones:
            if stone - num < 0:
                cnt += 1
                if cnt == k:
                    return False
            else:
                cnt = 0
        return True
    left = 0
    right = max(stones)
    while left <= right:
        mid = (left + right) // 2
        
        if can(mid):
            left = mid + 1
        else:
            right = mid - 1
    return right