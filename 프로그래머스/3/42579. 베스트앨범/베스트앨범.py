from collections import defaultdict

def solution(genres, plays):
    n = len(genres)
    dic = defaultdict(list)
    dic_cnt = defaultdict(int)

    for i in range(n):
        genre, play = genres[i], plays[i]
        dic_cnt[genre] += play
        dic[genre].append((play, i))

    lst_dic_cnt = list(dic_cnt.items())
    lst_dic_cnt.sort(key = lambda x : -x[1])
    
    ans = []
    for g, _ in lst_dic_cnt:
        lst = dic[g]
        lst.sort(key = lambda x : (-x[0], x[1]))
        for i, (num, idx) in enumerate(lst):
            if i >= 2 : break
            ans.append(idx)
    return ans