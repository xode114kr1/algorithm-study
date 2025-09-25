import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
acount_list = [0] * (n + 1)

for i in range(1, n + 1):
    acount_list[i] = acount_list[i - 1] + lst[i - 1]

for _ in range(m):
    st, nd = map(int, input().split())
    print(acount_list[nd] - acount_list[st - 1])
