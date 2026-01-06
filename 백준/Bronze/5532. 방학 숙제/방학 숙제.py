import sys

L = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())

days_kor = (A + C - 1) // C
days_math = (B + D - 1) // D
print(L - max(days_kor, days_math))
