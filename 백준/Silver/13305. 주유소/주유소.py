n = int(input())
lst_bridge = list(map(int, input().split()))
lst_oil = list(map(int, input().split()))

cur_idx = 0
total = 0
while cur_idx < n - 1:
    st = cur_idx
    cur_oid = lst_oil[cur_idx]
    move_count = 0
    move_bridge = 0
    for oil in lst_oil[cur_idx:]:
        if cur_oid <= oil:
            if st < n - 1:
                move_count += lst_bridge[st]
            move_bridge += 1
            st += 1
        else:
            break
    total += move_count * cur_oid
    cur_idx += move_bridge
print(total)