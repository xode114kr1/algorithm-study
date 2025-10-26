n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]
sorted_lst = sorted(lst, key = lambda x : (x[1], x[0]))

cur_time = sorted_lst[0][1]
cnt = 1
for tup in sorted_lst[1:]:
    if cur_time <= tup[0]:
        cur_time = tup[1]
        cnt += 1
print(cnt)