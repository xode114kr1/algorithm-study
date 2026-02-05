def solution(arr):
    ans = [0, 0] # 0, 1
    def rec(size, x, y):
        cur = arr[x][y]
        ok = True
        for i in range(x, x + size):
            if not ok : break
            for j in range(y, y + size):
                if arr[i][j] != cur:
                    ok = False
                    break
                    
        if ok:
            ans[cur] += 1
        else:
            new_size = size // 2
            rec(new_size, x, y)
            rec(new_size, x + new_size , y)
            rec(new_size, x, y + new_size)
            rec(new_size, x + new_size, y + new_size)
    n = len(arr)
    rec(n, 0, 0)
    return ans