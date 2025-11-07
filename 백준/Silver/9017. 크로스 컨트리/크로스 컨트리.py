import sys
from collections import defaultdict

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = 1
    dic = defaultdict(list)
    dic_team =defaultdict(int)
    s = set()

    for k in lst:
        dic_team[k] += 1
    for t in dic_team.items():
        if t[1] == 6 : s.add(t[0])

    for k in lst:
        if k in s:
            dic[k].append(cnt)
            cnt += 1

    min_cnt = float('inf')
    win_team = 1
    five_cnt = 0
    for team, count in dic.items():
        if len(count) < 6: continue
        c = sum(count[:4])
        if c < min_cnt:
            min_cnt = c
            win_team = team
            five_cnt = count[4]
        elif min_cnt == c and count[4] < five_cnt:
            min_cnt = c
            win_team = team
            five_cnt = count[4]

    print(win_team)