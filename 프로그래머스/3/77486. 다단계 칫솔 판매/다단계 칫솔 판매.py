from collections import defaultdict, deque

def solution(enroll, referral, seller, amount):
    dic_after = {}
    dic_amt = defaultdict(int)
    dic_ans = {"-": 0}
    for e, r in zip(enroll, referral):
        dic_after[e] = r
        dic_ans[e] = 0
    
    for s, a in zip(seller, amount):
        cur = s
        money = a * 100

        while cur != "-" and money > 0:
            nxt = dic_after[cur]
            dadan = money // 10
            money -= dadan
            
            dic_ans[cur] += money
            cur = nxt
            money = dadan
    ans = []
    for e in enroll:
        ans.append(dic_ans[e])
    return ans