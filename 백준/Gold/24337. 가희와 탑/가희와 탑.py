n, l, r = map(int, input().split())
max_num = max(l, r)

if l + r - 1 > n:
    print(-1)
else:
    acs_lst = [x for x in range(1, l)]
    decs_lst = [x for x in range(r - 1, 0, -1)]
    onces = [1] * (n - len(acs_lst) - len(decs_lst) - 1)

    if l == 1:
        ans = [max_num] + onces + decs_lst 
        print(*ans)
    else:
        ans = onces + acs_lst + [max_num] + decs_lst
        print(*ans)