n = int(input())
num_lst = list(map(int, input().split()))
oper_lst = list(map(int, input().split()))

max_num = float('-inf')
min_num = float('inf')

def f(idx, cur):
    global max_num, min_num
    if sum(oper_lst) == 0:
        min_num = min(min_num, cur)
        max_num = max(max_num, cur)
        return
    for i in range(4):
        if oper_lst[i] > 0:
            oper_lst[i] -= 1
            tmp = cur
            if i == 0:
                tmp = cur + num_lst[idx]
            elif i == 1:
                tmp = cur - num_lst[idx]
            elif i == 2:
                tmp = cur * num_lst[idx]
            elif i == 3:
                if cur < 0:
                    tmp = -(-cur // num_lst[idx])
                else:
                    tmp = cur // num_lst[idx]

            f(idx + 1, tmp)
            oper_lst[i] += 1

f(1, num_lst[0])
print(max_num)
print(min_num)
