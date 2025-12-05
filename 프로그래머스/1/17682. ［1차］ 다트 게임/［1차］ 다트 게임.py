import math
def solution(dartResult):
    dic = {'S' : 1, 'D' : 2, 'T' : 3}
    expression = ""
    bonus_count1 = 0
    bonus_count2 = 0
    lst = []
    dartResult = dartResult.replace('10', 'x')
    for i in dartResult:
        if i == 'x':
            lst.append('10')
        else:
            lst.append(i)
            
    for i in lst[::-1]:
        if i.isalpha():
            exponents = dic[i]
        elif i.isdigit():
            expression += str(pow(int(i), exponents))
            if bonus_count1 > 0:
                expression += '*2'
                bonus_count1 -= 1
            if bonus_count2 > 0:
                expression += '*2'
                bonus_count2 -= 1
            expression += '+'
        elif i == '#':
            expression = expression[:-1]
            expression += '-'
        elif i == '*':
            if bonus_count1 == 0:
                bonus_count1 = 2
            else:
                bonus_count2 = 2
        print(expression)
    return eval(expression[:-1])
            
    
    
        