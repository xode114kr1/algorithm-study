from collections import deque

n = int(input())
arr = [i for i in range(1, n + 1)]
deq = deque(arr)

while len(deq) > 1:
    deq.popleft()
    tmp = deq.popleft()
    deq.append(tmp)
print(deq[0])