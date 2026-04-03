n = int(input())
st = []
cnt = 0

for _ in range(n):
    x, y = map(int, input().split())

    while st:
        if st[-1] > y:
            st.pop()
            cnt += 1
        else:
            break

    if st and st[-1] == y:
        continue

    if y != 0:
        st.append(y)

cnt += len(st)
print(cnt)