import sys

burgers = [int(sys.stdin.readline()) for _ in range(3)]
drinks = [int(sys.stdin.readline()) for _ in range(2)]

print(min(burgers) + min(drinks) - 50)
