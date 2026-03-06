import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
lst = []
for _ in range(n):
    name, under = input().split()
    under = int(under)
    if under not in dic:
        dic[under] = name
    lst.append(under)

for _ in range(m):
    num = int(input())
    left = 0
    right = len(lst)
    while left <= right:
        mid = (left + right) // 2
        if num > lst[mid]:
            left = mid + 1
        else:
            right = mid - 1
    print(dic[lst[left]])