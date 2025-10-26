n, k = map(int, input().split())
num_lst = [int(input()) for _ in range(n)]
num_lst.sort(reverse=True)

cnt = 0
for c in num_lst:
    cnt += k // c
    k = k % c
print(cnt)