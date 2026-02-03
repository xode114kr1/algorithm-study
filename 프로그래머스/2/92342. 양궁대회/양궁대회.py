def solution(n, info):
    def select_same_count(lst1, lst2):
        for num1, num2 in zip(lst1[::-1], lst2[::-1]):
            if num1 > num2:
                return lst1
            elif num1 < num2:
                return lst2
    
    dic = {}
    def bt(idx, cnt, total, lst):
        if idx == 11:
            if total <= 0:
                dic[-1] = [-1]
            else:
                new_lst = lst[:]
                new_lst[-1] = cnt
                if total in dic:
                    cur_lst = dic[total]
                    dic[total] = select_same_count(cur_lst, new_lst)
                else:
                    dic[total] = new_lst
            return total
        
        apachi = info[idx]
        win_score = 10 - idx
        lose_score = 10 - idx if apachi > 0 else 0
        
        round_lose = bt(idx + 1, cnt, total - lose_score, lst[:])
        if cnt > apachi:
            new_lst = lst[:]
            new_lst[idx] = apachi + 1
            round_win = bt(idx + 1, cnt - apachi - 1, total + win_score, new_lst)
            return max(round_win, round_lose)
        return round_lose
    
    bt(0, n, 0,[0,0,0,0,0,0,0,0,0,0,0])
    max_idx = max(list(dic.keys()))
    return dic[max_idx]
        