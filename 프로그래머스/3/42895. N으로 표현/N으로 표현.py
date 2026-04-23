from collections import defaultdict

def solution(N, number):
    INF = 10 ** 6
    dp = defaultdict(set)
    
    dp[0].add(0)
    
    for i in range(1, 9):
        init = int('1' * i) * N
        dp[i].add(init)
        for x in range(1, i):
            y = i - x
            for n1 in dp[x]:
                for n2 in dp[y]:
                    dp[i].add(n1 + n2)
                    dp[i].add(n1 - n2)
                    dp[i].add(n1 * n2)
                    if n2 != 0:
                        dp[i].add(n1 // n2)
                
    dp_item = list(dp.items())
    dp_item.sort()
    for idx, nums in dp_item:
        if number in nums:
            return idx
    return -1