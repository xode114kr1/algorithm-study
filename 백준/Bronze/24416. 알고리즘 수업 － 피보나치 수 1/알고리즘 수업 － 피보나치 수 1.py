n = int(input())

# 재귀 함수처럼 보이게 하는 용도 (호출 횟수만 계산)
def fib_counter(n):
    fib = [0] * (n + 1)
    fib[1] = fib[2] = 1
    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

print(fib_counter(n), n - 2)
