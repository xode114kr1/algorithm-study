from collections import defaultdict

def solution(user_id, banned_id):
    def isBanned(user, ban):
        if len(user) != len(ban):
            return False
        
        for c1, c2 in zip(user, ban):
            if c2 == "*":
                continue
            elif c1 == c2:
                continue
            return False
        return True
    
    def dfs(idx, chose):
        if idx == len(banned_id):
            res.add(frozenset(chose))
            return
        for user in lst[idx]:
            if user not in chose:
                dfs(idx + 1, chose + [user])
    
    lst = []
    
    dic = defaultdict(int)
    for b_id in banned_id:
        tmp = []
        for u_id in user_id:
            if isBanned(u_id, b_id):
                tmp.append(u_id)
        lst.append(tmp)
    res = set()

    dfs(0, [])
    return len(res)