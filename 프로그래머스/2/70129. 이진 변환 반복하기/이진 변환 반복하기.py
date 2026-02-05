from collections import Counter

def solution(s):
    cnt = 0
    remove_cnt = 0
    while s != "1":
        c = Counter(s)
        remove_cnt += c["0"]
        s = bin(c["1"])[2:]
        cnt += 1
    return [cnt, remove_cnt]
    