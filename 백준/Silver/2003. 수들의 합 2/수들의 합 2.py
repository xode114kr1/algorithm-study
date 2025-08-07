n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
st = 0
nd = 0
n_sum = 0

while 1:
    if n_sum >= m:
        n_sum -= arr[st]
        st += 1
    elif nd == n:
        break
    else:
        n_sum += arr[nd]
        nd += 1

    if n_sum == m:
        cnt += 1
print(cnt)