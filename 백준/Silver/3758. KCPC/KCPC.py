import sys
input = sys.stdin.readline

zzzz = int(input())

for _ in range(zzzz):
    n, k, me, m = map(int, input().split()) # 팀수, 문제 수, 내id, 로그 수
    mat_pt = [[0] * (k + 1) for _ in range(n + 1)] # id, 번호
    mat_sum = [[0, 0, 0] for _ in range(n + 1)] # id, 총합, 제출 개수, 마지막 제출 idx
    for idx in range(m):
        i, j, s = map(int, input().split()) # id, 번호, 점수
        mat_sum[i][1] -= 1
        mat_sum[i][2] = -idx

        if s > mat_pt[i][j]:
            mat_sum[i][0] = mat_sum[i][0] - mat_pt[i][j] + s
            mat_pt[i][j] = s
    my_team = mat_sum[me]
    cnt = 1
    for team in mat_sum[1:]:
        if my_team < team:
            cnt += 1
    print(cnt)