n = int(input())
mat = []
lst = []
max_x = 0
for _ in range(n):
   x, y = map(int, input().split())
   max_x = max(max_x, x)
   mat.append([x, y])
lst = [0] * (max_x + 1)
mat.sort(key = lambda x:x[0])

for idx, h in mat:
    lst[idx] = h

max_height = max(lst)
left_max_idx = lst.index(max_height)

right_max_idx = len(lst) - 1 - lst[::-1].index(max_height)
ans = 0
cur = 0
for i in range(left_max_idx):
    cur = max(cur, lst[i])
    ans += cur


ans += (right_max_idx - left_max_idx + 1) * max_height
cur = 0
for i in range(len(lst) - 1, right_max_idx, -1):
    cur = max(cur, lst[i])
    ans += cur
print(ans)
