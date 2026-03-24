n = int(input())
lst = list(map(int, input().split()))

ans = [0] * n
st = [] # (num, idx)
for i, num in enumerate(lst[::-1]):
    idx = n - i - 1
    while st:
        cur_num, cur_idx = st[-1]
        if num < cur_num:
            break
        else:
            st.pop()
            ans[cur_idx] = idx + 1
    st.append((num, idx))
print(*ans)

