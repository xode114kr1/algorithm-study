s = 0
for _ in range(5):
    score = int(input())
    s += max(score, 40) 
print(s // 5)