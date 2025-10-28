import sys
from collections import defaultdict

input = sys.stdin.readline

def sort_by_count(item):
    key, value = item
    return (-value, -len(key), key)

n, m = map(int, input().split())
dic = defaultdict(int)
for _ in range(n):
    key = input().strip()
    if len(key) >= m:
        dic[key] += 1

sorted_items = sorted(dic.items(), key = sort_by_count)
for item in sorted_items:
    print(item[0])


