nums = list(map(int, input().split()))
result = sum(x * x for x in nums) % 10
print(result)