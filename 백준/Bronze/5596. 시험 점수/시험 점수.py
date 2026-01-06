import sys

s = sum(map(int, sys.stdin.readline().split()))
t = sum(map(int, sys.stdin.readline().split()))
print(max(s, t))
