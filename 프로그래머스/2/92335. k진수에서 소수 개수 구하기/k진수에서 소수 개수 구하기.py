def solution(n, k):
    def is_prime(num):
        if num < 2 : return False
        for i in range(2, int(num ** (0.5) + 1)):
            if num % i == 0:
                return False
        return True
    
    trans = ""
    while n > 0:
        trans += str(n % k)
        n = n // k
    
    trans = trans[::-1]
    lst = trans.split("0")

    ans = 0
    for num in lst:
        if num == "": continue
        if is_prime(int(num)): ans += 1
    return ans
    