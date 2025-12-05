def numtomap(n, size):
    ans = ""
    for i in range(size):
        if n % 2 == 1: 
            ans += "#"
        else: 
            ans += " "
        n = n // 2
    return ans[::-1]
def solution(n, arr1, arr2):
    arr = []
    for x,y in zip(arr1, arr2):
        arr.append(numtomap(x | y, n))
    return arr
    
