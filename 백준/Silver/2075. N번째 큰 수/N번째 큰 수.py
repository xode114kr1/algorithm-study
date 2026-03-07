import sys
input = sys.stdin.readline

n = int(input())
lst = [0] * (n * n)
for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(len(nums)):
        lst[i * n + j] = nums[j]
lst.sort()
print(lst[-n])