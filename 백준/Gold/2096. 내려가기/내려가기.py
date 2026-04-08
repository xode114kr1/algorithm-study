import sys
input = sys.stdin.readline

n = int(input())
first = list(map(int, input().split()))

min_ans = first[:]
max_ans = first[:]

for _ in range(n - 1):
    row = list(map(int, input().split()))

    min_tmp = [0] * 3
    max_tmp = [0] * 3

    min_tmp[0] = min(min_ans[0], min_ans[1]) + row[0]
    min_tmp[1] = min(min_ans[0], min_ans[1], min_ans[2]) + row[1]
    min_tmp[2] = min(min_ans[1], min_ans[2]) + row[2]

    max_tmp[0] = max(max_ans[0], max_ans[1]) + row[0]
    max_tmp[1] = max(max_ans[0], max_ans[1], max_ans[2]) + row[1]
    max_tmp[2] = max(max_ans[1], max_ans[2]) + row[2]

    min_ans = min_tmp
    max_ans = max_tmp

print(max(max_ans), min(min_ans))