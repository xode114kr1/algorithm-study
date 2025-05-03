# https://www.acmicpc.net/problem/15650

n, m = map(int, input().split())

def f(start, lst):
    if len(lst) == m:
        print(*lst)
        return

    for i in range(start, n + 1):
        f(i + 1, lst + [i])

f(1, [])