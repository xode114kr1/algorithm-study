n = int(input())
lst = list(map(int, input().split()))
total = int(input())

lst.sort()
i = 0
while n > 0:
    if lst[i] * n <= total:
        total -= lst[i]
        n -= 1
        i += 1
        continue
    break
if n == 0:
    print(lst[n - 1])
else:
    print(total // n)