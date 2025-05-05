n = int(input())
arr = [['*' for _ in range(n)] for _ in range(n)]

def f(x, y, size):
    if size == 1:
        return
    off = size // 3
    # 가운데 부분 공백 처리
    for i in range(x + off, x + 2 * off):
        for j in range(y + off, y + 2 * off):
            arr[i][j] = ' '
    # 9개 구역 중 가운데 빼고 재귀 호출
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            f(x + i * off, y + j * off, off)

f(0, 0, n)

for row in arr:
    print(''.join(row))
