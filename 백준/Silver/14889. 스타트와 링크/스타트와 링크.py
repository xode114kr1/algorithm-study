def divide_team(idx, lst):
    global gap
    if idx == n:
        return
    
    if len(lst) == n // 2:
        team1 = 0
        team2 = 0
        other = [i for i in range(n) if i not in lst]

        for i in range(n // 2):
            for j in range(n // 2):
                team1 += mat[lst[i]][lst[j]]
                team2 += mat[other[i]][other[j]]

        gap = min(gap, abs(team1 - team2))
        return

    for i in range(idx, n):
        divide_team(i + 1, lst + [i])

n = int(input())
gap = float('inf')
mat = [list(map(int, input().split())) for _ in range(n)]

divide_team(0, [])
print(gap)