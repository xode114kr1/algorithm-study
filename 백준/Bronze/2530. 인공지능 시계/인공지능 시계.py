A, B, C = map(int, input().split()) 
D = int(input())                    

total_seconds = A * 3600 + B * 60 + C
total_seconds += D

total_seconds %= 24 * 3600

A = total_seconds // 3600
total_seconds %= 3600
B = total_seconds // 60
C = total_seconds % 60

print(A, B, C)
