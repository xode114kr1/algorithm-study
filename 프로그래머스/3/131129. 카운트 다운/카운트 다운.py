INF = 10 ** 6

def solution(target):
    cnt_dp = [(INF, INF)] * 61
    cnt_dp[0] = (0, 0)
    
    for i in range(1, 21): # 2배
        cnt_dp[i * 2] = (1, 0)
    for i in range(1, 21): # 3배
        cnt_dp[i * 3] = (1, 0)
    for i in range(1, 21): # 1배
        cnt_dp[i] = (1, 1)
    
    cnt_dp[50] = (1, 1)
    
    dp = [[INF, -INF]] * (target + 1)
    dp[0] = (0, 0)
    
    for i in range(1, target + 1):
        for j in range(1, 61):
            if j > i:
                break
            if cnt_dp[j][0] == INF:
                continue
            
            prev_cnt, prev_s_cnt = dp[i - j]
            cur_cnt = prev_cnt + 1
            cur_s_cnt = prev_s_cnt + cnt_dp[j][1]
            
            if cur_cnt < dp[i][0]:
                dp[i] = (cur_cnt, cur_s_cnt)
            elif cur_cnt == dp[i][0] and cur_s_cnt > dp[i][1]:
                dp[i] = (cur_cnt, cur_s_cnt)
    
    return (list(dp[target]))