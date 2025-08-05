n = int(input())
arr = list(map(int, input().split()))
sort_arr = sorted(set(arr))
d = {value:idx for idx, value in enumerate(sort_arr)}
for i in arr:
    print(d[i], end=' ')