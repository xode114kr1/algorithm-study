L, P = map(int, input().split())
nums = list(map(int, input().split()))

real = L * P
result = [x - real for x in nums]

print(*result)
