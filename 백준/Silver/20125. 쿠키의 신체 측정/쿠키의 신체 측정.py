n = int(input())
mat = [list(input() + "_") for _ in range(n)]
mat.append(list("_" * (n + 1)))

def find_heart():
    for i in range(n):
        for j in range(n):
            if mat[i][j] == "*":
                return i + 1, j

def count_left_arm(heart_i, heart_j):
    count = 0
    i,j = heart_i,heart_j
    while(mat[i][j] == "*"):
        count += 1
        j -= 1
    return count

def count_right_arm(heart_i, heart_j):
    count = 0
    i,j = heart_i,heart_j
    while(mat[i][j] == "*"):
        count += 1
        j += 1
    return count

def count_y(st_i, st_j):
    count = 0
    i,j = st_i,st_j
    while(mat[i][j] == "*"):
        count += 1
        i += 1
    return count

heart_i, heart_j = find_heart()
print(heart_i + 1, heart_j + 1)
left_arm_length = count_left_arm(heart_i, heart_j - 1)
right_arm_length = count_right_arm(heart_i, heart_j + 1)
body_length = count_y(heart_i + 1, heart_j)
left_leg_length = count_y(heart_i + body_length + 1, heart_j - 1)
right_leg_length = count_y(heart_i + body_length + 1, heart_j + 1)
print(left_arm_length, right_arm_length, body_length, left_leg_length, right_leg_length)