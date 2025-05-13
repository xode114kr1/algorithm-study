n = int(input())

for _ in range(n):
    k = int(input())
    lst = [1, 1, 1, 2, 2]

    if k <= 5:
        print(lst[k - 1])
    else:
        for _ in range(5, k):
            lst.append(lst[-1] + lst[-5])
        print(lst[-1])
