import math

from collections import defaultdict

def solution(fees, records):
    default_time, default_price, count_time, count_price = fees[0], fees[1], fees[2], fees[3]
    dic = {}
    predix_dic = defaultdict(int)
    for record in records:
        time, member, cmd = record.split()
        h, m = map(int, time.split(":"))
        t = h * 60 + m
        if cmd == "IN":
            dic[member] = t
        elif cmd == "OUT":
            st = dic[member]
            del dic[member]
            predix_dic[member] += (t - st)
    for member, time in dic.items():
        predix_dic[member] += ((23 * 60 + 59) - time)
    ans = []
    for member, stay_time in predix_dic.items():
        overtime = stay_time - default_time if stay_time - default_time > 0 else 0
        price = default_price + math.ceil(overtime / count_time) * count_price
        ans.append([int(member), price])
    ans.sort()
    answer = []
    for a, b in ans:
        answer.append(b)
    return answer