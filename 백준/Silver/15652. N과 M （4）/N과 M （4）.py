# https://www.acmicpc.net/problem/15652

n, m = map(int, input().split())

def f(start, lst):
    if len(lst) == m:
        print(*lst)
        return

    for i in range(start - 1, n + 1):
        if i == 0:
            continue
        f(i + 1, lst + [i])

f(1, [])