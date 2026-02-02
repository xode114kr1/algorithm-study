from collections import deque

def solution(queue1, queue2):
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    target_sum = (q1_sum + q2_sum) // 2
    deq1 = deque(queue1)
    deq2 = deque(queue2)
    
    if (q1_sum + q2_sum) % 2 == 1:
        return -1
    
    limit = 3 * len(queue1)
    cnt = 0
    while deq1 and deq2:
        if limit < cnt:return -1
        if q1_sum > q2_sum:
            poped = deq1.popleft()
            deq2.append(poped)
            q1_sum -= poped
            q2_sum += poped
            cnt += 1
        elif q1_sum < q2_sum:
            poped = deq2.popleft()
            deq1.append(poped)
            q1_sum += poped
            q2_sum -= poped
            cnt += 1
        else:
            return cnt
    return -1