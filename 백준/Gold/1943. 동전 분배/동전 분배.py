for _ in range(3):
    n = int(input())
    coins = []
    total = 0

    for _ in range(n):
        c, k = map(int, input().split())
        coins.append((c, k))
        total += c * k

    if total % 2 == 1:
        print(0)
        continue

    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True

    for coin, cnt in coins:
        for i in range(target, -1, -1):
            if dp[i]:
                for k in range(1, cnt + 1):
                    if i + coin * k > target:break
                    dp[i + coin * k] = True
    if dp[target]:
        print(1)
    else:
        print(0)