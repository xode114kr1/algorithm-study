import math
from functools import reduce


def solution(arrayA, arrayB):
    def fun(arr1, arr2):
        gcd = reduce(math.gcd, arr1)
        if gcd == 1 : return 0
    
        primarys = [gcd]
        d = 2
        for i in range(2, int(gcd ** (0.5) + 1)):
            if gcd % i == 0:
                primarys.append(i)
                primarys.append(gcd // i)
            
        primarys.sort(reverse = True)
    
        for primary in primarys :
            isClear = True
            for b in arr2:
                if b % primary == 0:
                    isClear = False
                    break
            if isClear:
                return primary
        return 0
    
    return max(fun(arrayA, arrayB), fun(arrayB, arrayA))
                
                
        
        
        
        
        
        