n = int(input())
lst = list(map(int, input().split()))

cnt = [0] * n
near = [0] * n

stack = []

for i in range(n):
    while stack and stack[-1][0] <= lst[i]:
        stack.pop()

    cnt[i] += len(stack)

    if stack:
        near[i] = stack[-1][1]

    stack.append((lst[i], i + 1))

stack = []

for i in range(n - 1, -1, -1):
    while stack and stack[-1][0] <= lst[i]:
        stack.pop()

    cnt[i] += len(stack)

    if stack:
        if near[i] == 0:
            near[i] = stack[-1][1]
        else:
            left_dist = abs(near[i] - (i + 1))
            right_dist = abs(stack[-1][1] - (i + 1))

            if right_dist < left_dist:
                near[i] = stack[-1][1]
            elif right_dist == left_dist:
                near[i] = min(near[i], stack[-1][1])

    stack.append((lst[i], i + 1))

for i in range(n):
    if cnt[i] == 0:
        print(0)
    else:
        print(cnt[i], near[i])