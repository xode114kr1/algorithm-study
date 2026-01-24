def solution(sequence, k):
    start, end = 0, 0
    pre_sum = 0
    cnt = float('inf')
    ans = [0, 0]
    while 1:
        if end == len(sequence) and pre_sum <= k:
            if pre_sum == k and end - start < cnt:
                cnt = end - start
                ans = [start, end - 1]
            break
        
        if pre_sum == k:
            if end - start < cnt:
                cnt = end - start
                ans = [start, end - 1]
            pre_sum += sequence[end]
            end += 1
            
        elif pre_sum < k:
            pre_sum += sequence[end]
            end += 1
        elif pre_sum > k:
            pre_sum -= sequence[start]
            start += 1
    return ans
        