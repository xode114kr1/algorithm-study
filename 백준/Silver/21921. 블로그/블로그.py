n, x = map(int,input().split())
visited_lst = list(map(int, input().split()))

max_visited = sum(visited_lst[:x])
cur_visited = sum(visited_lst[:x])
cnt = 1
for i in range(n - x):
    cur_visited = cur_visited - visited_lst[i] + visited_lst[i + x]
    if max_visited < cur_visited:
        max_visited = cur_visited
        cnt = 1
    elif max_visited == cur_visited:
        cnt += 1

if max_visited == 0:
    print("SAD")
else:
    print(max_visited, cnt)