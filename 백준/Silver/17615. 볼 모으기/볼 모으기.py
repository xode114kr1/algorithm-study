n = int(input())
lst = input()

left_ball = lst[0]
right_ball = lst[-1]

dic = {"R" : 0, "B" : 0}

for ball in lst:
    dic[ball] += 1

# 3가지 경우의 수가 있을 듯
# 1. 왼쪽 ball과 같은 공 왼쪽 ball을 다 옮기기
# 2. 오른쪽 ball과 같은 공 오른쪽 ball을 다 옮기기
# 3. 좌우가 같을 경우 사이에 있는 공 개수

leftBalls = 0
rightBalls = 0
for ball in lst:
    if ball != left_ball: break
    leftBalls += 1

for ball in lst[::-1]:
    if ball != right_ball: break
    rightBalls += 1

toLeft = dic[left_ball] - leftBalls
toRight = dic[right_ball] - rightBalls
ans = min(toLeft, toRight, dic["R"], dic["B"])
print(ans)
