def solution(players, m, k):
    size = len(players)
    server = [m - 1] * (size + k)
    ans = 0
    for i in range(size):
        gap = players[i] - server[i]
        if gap >= 0:
            added = gap // m if gap % m == 0 else gap // m + 1
            for j in range(i, i + k):
                server[j] += added * m
            ans += added
    return ans